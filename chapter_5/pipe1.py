"Anonymous pipe basics"
'''
the script in Example 5-19 uses the os.fork call to make a copy of the calling process
as usual (we met forks earlier in this chapter). After forking, the original parent process
and its child copy speak through the two ends of a pipe created with os.pipe prior to
the fork. The os.pipe call returns a tuple of two file descriptors—the low-level file identifiers
we met in Chapter 4—representing the input and output sides of the pipe. Because
forked child processes get copies of their parents’ file descriptors, writing to the
pipe’s output descriptor in the child sends data back to the parent on the pipe created
before the child was spawned.
'''

import os, time 


def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)                         # make parent wait
        msg = ('Spam %03' % zzz).encode()       # pipes are binary bytes
        os.write(pipeout, msg)                  # send to parent
        zzz = (zzz + 1) % 5                     # goto 0 after 4
    

def parent():
    pipein, pipeout = os.pipe()                 # make 2-ended pipe
    if os.fork() == 0:                          # copy this process
        child(pipeout)                          # in copy, run child
    else:
        while True:
            line = os.read(pipein, 32)          # blocks until data sent
            print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))
        

parent()


"""
Notice how the parent received a bytes string through the pipe. Raw pipes normally
deal in binary byte strings when their descriptors are used directly this way with the
descriptor-based file tools.

That’s why we also have to
manually encode to bytes when writing in the child—the string formatting operation
is not available on bytes.
"""
