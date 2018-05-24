import signal
import time
from SignalBlock import sigblock

print('Blocking SIGINT')
sigblock.block(signal.SIGINT)
print('Blocked signals:',sigblock._blocked)

print('Timer 3 seconds start')
time.sleep(3)
print('\nTimer 3 seconds end')

print('Signums of catched SIGINTs:', sigblock._pending)


print('Unblocking SIGINT')
sigblock.unblock(signal.SIGINT)
print('Blocked signals:',sigblock._blocked)

try:
    print('Timer 3 seconds start')
    time.sleep(3)
    print('Timer 3 seconds end')
except:
    print('\nSignal was not blocked')
