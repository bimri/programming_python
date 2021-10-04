# no output for 10 seconds unless Python -u flag used or sys.stdout.flush()
# but writer's output appears here every 2 seconds when either option is used

import os
for line in os.popen('python -u pipe-unbuff-writer.py'):    # iterator reads lines
    print(line, end='')                                     # blocks without -u!


'''
The net effect is that -u still works around the steam buffering issue for connected
programs in 3.X, as long as you don’t reset the streams to other objects in the spawned
program.
'''
