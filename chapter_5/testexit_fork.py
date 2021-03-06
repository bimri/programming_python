"Process Exit Status and Shared State"
"""
fork child processes to watch exit status with os.wait; fork works on Unix
and Cygwin but not standard Windows Python 3.1; note: spawned threads share
globals, but each forked process has its own copy of them (forks share file
descriptors)--exitstat is always the same here but will vary if for threads;
"""

import os 
exitstat = 0

def child():                            # could os.exit a script here
    global exitstat                     # change this process's global 
    exitstat += 1                       # exit status to parent's wait
    print('Hello from child', os.getpid(), exitstat)
    os._exit(exitstat)
    print('never reached')


def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            pid, status = os.wait()
            print('Parent got', pid, status, (status >> 8))
            if input() == 'q': break
        
    
if __name__ == '__main__': parent()


'''
If you study this output closely, you’ll notice that the exit status (the last number printed)
is always the same—the number 1. Because forked processes begin life as copies
of the process that created them, they also have copies of global memory. Because of
that, each forked child gets and changes its own exitstat global variable without
changing any other process’s copy of this variable. At the same time, forked processes
copy and thus share file descriptors, which is why prints go to the same place.
'''
