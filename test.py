import signal
import time
from SignalBlock import sigblock

sigblock.block(signal.SIGINT)

print('Timer 3 seconds start')
time.sleep(3)
print('\nTimer 3 seconds end')

print('Signums of catched SIGINTs:', sigblock._pending)
