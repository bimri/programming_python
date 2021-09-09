"The Basics: Processes and Locks"
"""
multiprocess basics: Process works like threading.Thread, but
runs function call in parallel in a process instead of a thread;
locks can be used to synchronize, e.g. prints on some platforms;
starts new interpreter on windows, forks a new process on unix;
"""

import os
from multiprocessing import Process, Lock

def whoami(label, lock):
    msg = '%s: name:%s, pid:%s'
    with lock:
        print(label, os.getpid())
    

if __name__ == '__main__':
    lock = Lock()
    whoami('function call', lock)

    p = Process(target=whoami, args=('process call', lock))
    p.start()
    p.join()

    for i in range(5):
        Process(target=whoami, args=('run process %s' % i, lock)).start()
    
    with lock:
        print('Main process exit.')


'Implementation and usage rules'
"""
Technically, to achieve its portability, this module currently works by selecting from
platform-specific alternatives:
    • On Unix, it forks a new child process and invokes the Process object’s run method
    in the new child.

    • On Windows, it spawns a new interpreter by using Windows-specific process creation
    tools, passing the pickled Process object in to the new process over a pipe,
    and starting a “python -c” command line in the new process, which runs a special
    Python-coded function in this package that reads and unpickles the Process and
    invokes its run method.
"""