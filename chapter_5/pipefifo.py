"Named pipe basics"
'''
named pipe files are created with the os.mkfifo call.
    which is available today
    on Unix-like platforms, including Cygwin’s Python on Windows, but is not currently
    available in standard Windows Python.

This call creates only the external file, though;
to send and receive data through a fifo, it must be opened and processed as if it were a
standard file.
'''

"""
named pipes; os.mkfifo is not available on Windows (without Cygwin);
there is no reason to fork here, since fifo file pipes are external
to processes--shared fds in parent/child processes are irrelevent;
"""

import os, time, sys
fifoname = 'E:\practice\programming_python\>'           # must open same name


def child():
    pipeout = os.open(fifoname, os.O_WRONLY)            # open fifo pipe file fd
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Spam %03d\n' % zzz).encode()            # binary as opened here
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5


def parent():
    pipein = open(fifoname, 'r')                        # open fifo as text file object
    while True:
        line = pipein.readline()[:-1]                   # blocks until data sent
        print('Parent %d got "%s" at %s' % (os.getpid(), line, time.time()))
    


if __name__ == "__main__":
    if not os.path.exists(fifoname):
        os.mkfifo(fifoname)                             # create a named pipe file
    if len(sys.argv) == 1:                              
        parent()                                        # run as parent if not args
    else:                                               # else run as child process
        child()


'''
Because the fifo exists independently of both parent and child, there’s no reason to fork
here. The child may be started independently of the parent as long as it opens a fifo file
by the same name.

# [C:\...\PP4E\System\Processes] $ python pipefifo.py # parent window

# [C:\...\PP4E\System\Processes]$ file /tmp/pipefifo # child window

# [C:\...\PP4E\System\Processes]$ python pipefifo.py -child
# ...Ctrl-C to exit...
'''



"Named pipe use cases"
'''
By mapping communication points to a file system entity accessible to all programs run
on a machine, fifos can address a broad range of IPC goals on platforms where they are
supported. For instance, although this section’s example runs independent programs,
named pipes can also be used as an IPC device by both in-process threads and directly
forked related processes.

By also supporting unrelated programs, though, fifo files are more widely applicable to
general client/server models. For example, named pipes can make the GUI and
command-line debugger integration I described earlier for anonymous pipes even more
flexible—by using fifo files to connect the GUI to the non-GUI debugger’s streams, the
GUI could be started independently when needed.
'''