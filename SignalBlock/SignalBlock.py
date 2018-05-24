import signal

def signal_handler(signum, frame):
    sigblock._pending += (signum,)

class sigblock:
    _pending = ()
    _handler = signal_handler
    _blocked = {}

    @classmethod
    def block(cls, sig, handler=_handler):
        if type(sig) != signal.Signals:
            raise TypeError('Argument has to be of type signal.Signals')

        if sig not in cls._blocked:
            cls._blocked[sig] = signal.getsignal(sig)
        signal.signal(sig, handler)

    @classmethod
    def unblock(cls, sig=None):
        if sig == None:
            for sig in cls._blocked:
                signal.signal(sig, cls._blocked[sig])
                del cls._blocked[sig]
        else:
            if type(sig) != signal.Signals:
                raise TypeError('Argument has to be of type signal.Signals')
            elif sig not in cls._blocked:
                return

            signal.signal(sig, cls._blocked[sig])
            cls._blocked.clear()

    @classmethod
    def pending(cls, sig=None):
        if sig != None:
            if type(sig) != signal.Signals:
                raise TypeError('Argument has to be of type signal.Signals')

            return sig.value in cls._pending
        else:
            return cls._pending

    @classmethod
    def clear(cls):
        cls._pending = ()
