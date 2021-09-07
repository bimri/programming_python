"Anonymous pipes and threads"
'''
Although the os.fork call required by the prior section’s examples isn’t available on
standard Windows Python, os.pipe is. Because threads all run in the same process and
share file descriptors (and global memory in general), this makes anonymous pipes
usable as a communication and synchronization device for threads, too. This is an
arguably lower-level mechanism than queues or shared names and objects, but it provides
an additional IPC option for threads.
'''

# anonymous pipes and threads, not processes; this version works on Windows

import os, time, threading

def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)                                 # make parent wait
        msg = ('Spam %03d' % zzz).encode()              # pipes are binary bytes
        os.write(pipeout, msg)                          # send to parent
        zzz = (zzz+1) % 5                               # goto 0 after 4

def parent(pipein):
    while True:
        line = os.read(pipein, 32) # blocks until data sent
        print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))

pipein, pipeout = os.pipe()
threading.Thread(target=child, args=(pipeout,)).start()
parent(pipein)
