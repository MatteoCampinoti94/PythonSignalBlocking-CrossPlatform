import signal

def signal_handler(signum, frame):
    sigblock._pending += (signum,)

def signal_clear():
    sigblock._pending = ()

class sigblock:
    _pending = ()

    def block(sig, handler=signal_handler):
        if type(sig) != signal.Signals:
            raise TypeError('Argument has to be of type signal.Signals')

        signal.signal(sig, handler)

    def pending(sig=None):
        if sig != None:
            if type(sig) != signal.Signals:
                raise TypeError('Argument has to be of type signal.Signals')

            return sig.value in sigblock._pending
        else:
            return sigblock._pending

    def clear():
        signal_clear()
