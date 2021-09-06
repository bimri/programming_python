"Coding alternatives: busy loops, arguments, and context managers"
'''
Notice how the main threads of both of the last two scripts fall into busy-wait loops at
the end, which might become significant performance drains in tight applications. If
so, simply add a time.sleep call in the wait loops to insert a pause between end tests
and to free up the CPU for other tasks: this call pauses the calling thread only (in this
case, the main one).

Passing in the lock to threaded functions as an argument instead of referencing it in the
global scope might be more coherent, too. When passed in, all threads reference the
same object, because they are all part of the same process.

And while we’re at it, the with statement can be used to ensure thread operations around
a nested block of code, much like its use to ensure file closure in the prior chapter. The
thread lock’s context manager acquires the lock on with statement entry and releases
it on statement exit regardless of exception outcomes. The net effect is to save one line
of code, but also to guarantee lock release when exceptions are possible.
'''

# Example 5-10. PP4E\System\Threads\thread-count-wait3.py
"""
passed in mutex object shared by all threads instead of globals;
use with context manager statement for auto acquire/release;
sleep calls added to avoid busy loops and simulate real work
"""

import _thread as thread, time

stdoutmutex = thread.allocate_lock()
numthreads = 5
exitmutexes = [thread.allocate_lock() for i in range(numthreads)]


def counter(myId, count, mutex):                                        # shared object passed in
    for i in range(count):
        time.sleep(1 / (myId+1))                                        # diff fractions of second
        with mutex:                                                     # auto acquire/release: with
            print('[%s] => %s' % (myId, i))
    exitmutexes[myId].acquire()                                         # global: signal main thread


for i in range(numthreads):
    thread.start_new_thread(counter, (i, 5, stdoutmutex))

while not all(mutex.locked() for mutex in exitmutexes): time.sleep(0.25)
print('Main thread exiting.')
