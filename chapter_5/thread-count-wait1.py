"Waiting for spawned thread exits"
'''
Besides avoiding print collisions, thread module locks are surprisingly useful. They can
form the basis of higher-level synchronization paradigms (e.g., semaphores) and can
be used as general thread communication devices.
'''

# Example 5-8. PP4E\System\Threads\thread-count-wait1.py
"""
uses mutexes to know when threads are done in parent/main thread,
instead of time.sleep; lock stdout to avoid comingled prints;
"""

import _thread as thread

stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(10)]


def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myId, i))
        stdoutmutex.release()
    exitmutexes[myId].acquire()                     # signal main thread


for i in range(10):
    thread.start_new_thread(counter, (i, 100))


for mutex in exitmutexes:
    while not mutex.locked(): pass
print('Main thread exiting.')


"""
A lock’s locked method can be used to check its state. To make this work, the main
thread makes one lock per child and tacks them onto a global exitmutexes list (remember,
the threaded function shares global scope with the main thread).On exit,
each thread acquires its lock on the list, and the main thread simply watches for all
locks to be acquired. This is much more accurate than naïvely sleeping while child
threads run in hopes that all will have exited after the sleep.

All 10 spawned threads count up to 100 (they run in arbitrarily interleaved
order that can vary per run and platform, but their prints run atomically and do
not comingle), before the main thread exits.
"""
