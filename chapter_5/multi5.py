"Starting Independent Programs"
'''
Like threads, multiprocessing is designed to run function calls in parallel, not to start
entirely separate programs directly. Spawned functions might use tools like os.system,
os.popen, and subprocess to start a program if such an operation might block the caller,
but there’s otherwise often no point in starting a process that just starts a program

It is, however, possible to start new programs in the child processes spawned, using
tools like the os.exec* calls we met earlier—by spawning a process portably with
multiprocessing and overlaying it with a new program this way, we start a new independent
program, and effectively work around the lack of the os.fork call in standard
Windows Python.

This generally assumes that the new program doesn’t require any resources passed in
by the Process API, of course (once a new program starts, it erases that which was
running), but it offers a portable equivalent to the fork/exec combination on Unix.
'''


"Use multiprocessing to start independent programs, os.fork or not"

import os
from multiprocessing import Process

def runprogram(arg):
    os.execlp('python', 'python', 'child.py', str(arg))


if __name__ == '__main__':
    for i in range(5):
        Process(target=runprogram, args=(i,)).start()
        print('parent exit')


'''
This technique isn’t possible with threads, because all threads run in the same process;
overlaying it with a new program would kill all its threads. Though this is unlikely to
be as fast as a fork/exec combination on Unix, it at least provides similar and portable
functionality on Windows
'''        