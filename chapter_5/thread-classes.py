"The threading Module"
'''
The Python standard library comes with two thread modules: _thread, the basic lowerlevel
interface illustrated thus far, and threading, a higher-level interface based on
objects and classes. The threading module internally uses the _thread module to implement
objects that represent threads and common synchronization tools.
'''

"""
thread class instances with state and run() for thread's action;
uses higher-level Java-like threading module object join method (not
mutexes or shared global vars) to know when threads are done in main
parent thread; see library manual for more details on threading;
"""

import threading


class MyThread(threading.Thread):                               # subclass Thread object
    def __init__(self, myId, count, mutex):                     # run by default with __name__
        self.myId = myId
        self.count = count                                      # per-thread state information
        self.mutex = mutex                                      # shared objects, not globals
        threading.Thread.__init__(self)
    
    def run(self):                                              # run provides thread logic
        for i in range(self.count):                             # still sync stdout access
            with self.mutex:
                print('[%s] => %s' % (self.myId, i))
            
        
stdoutmutex = threading.Lock()                                  # same as thread.allocate_lock()
threads = []
for i in range(10):
    thread = MyThread(i, 100, stdoutmutex)                      # make/start 10 threads
    thread.start()                                              # start run method in a thread
    threads.append(thread)

for thread in threads:
    thread.join()                                               # wait for thread exits
print('Main thread exiting.')


'''
Using the threading module this way is largely a matter of specializing classes. Threads
in this module are implemented with a Thread object, a Python class which we may
customize per application by providing a run method that defines the thread’s action.
For example, this script subclasses Thread with its own Mythread class; the run method
will be executed by the Thread framework in a new thread when we make a Mythread
and call its start method.

In other words, this script simply provides methods expected by the Thread framework.
The advantage of taking this more coding-intensive route is that we get both per-thread
state information (the usual instance attribute namespace), and a set of additional
thread-related tools from the framework “for free.” The Thread.join method used near
the end of this script, for instance, waits until the thread exits (by default); we can use
this method to prevent the main thread from exiting before its children, rather than
using the time.sleep calls and global locks and variables we relied on in earlier threading
examples. 
'''
