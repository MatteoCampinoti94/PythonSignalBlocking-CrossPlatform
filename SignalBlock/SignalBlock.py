import signal

def signal_handler(signum, frame):
    sigblock._pending += (signum,)

def signal_clear():
    sigblock._pending = ()

def blocked_clear(sig=None):
    if sig == None:
        sigblock._blocked = {}
    else:
        del sigblock._blocked[sig]

class sigblock:
    _pending = ()
    _handler = signal_handler
    _blocked = {}

    def block(sig, handler=_handler):
        if type(sig) != signal.Signals:
            raise TypeError('Argument has to be of type signal.Signals')

        if sig not in sigblock._blocked:
            sigblock._blocked[sig] = signal.getsignal(sig)
        signal.signal(sig, handler)

    def unblock(sig=None):
        if sig == None:
            for sig in sigblock._blocked:
                signal.signal(sig, sigblock._blocked[sig])
            blocked_clear()
        else:
            if type(sig) != signal.Signals:
                raise TypeError('Argument has to be of type signal.Signals')
            elif sig not in sigblock._blocked:
                return

            signal.signal(sig, sigblock._blocked[sig])
            blocked_clear(sig)

    def pending(sig=None):
        if sig != None:
            if type(sig) != signal.Signals:
                raise TypeError('Argument has to be of type signal.Signals')

            return sig.value in sigblock._pending
        else:
            return sigblock._pending

    def clear():
        signal_clear()
