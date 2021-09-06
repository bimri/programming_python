"Synchronizing access to shared objects and names"
'''
One of the nice things about threads is that they automatically come with a cross-task
communications mechanism: objects and namespaces in a process that span the life of
threads are shared by all spawned threads.

For instance, because every thread runs in
the same process, if one Python thread changes a global scope variable, the change can
be seen by every other thread in the process, main or child.

Similarly, threads can share
and change mutable objects in the process’s memory as long as they hold a reference
to them (e.g., passed-in arguments). This serves as a simple way for a program’s threads
to pass information—exit flags, result objects, event indicators, and so on—back and
forth to each other.

The downside to this scheme is that our threads must sometimes be careful to avoid
changing global objects and names at the same time.

Files and streams, for example,
are shared by all threads in a program; if multiple threads write to one stream
at the same time, the stream might wind up with interleaved, garbled data.
'''


"""
Python’s _thread module comes with its own easy-to-use tools for synchronizing
access to objects shared among threads. These tools are based on the concept
of a lock—to change a shared object, threads acquire a lock, make their changes, and
then release the lock for other threads to grab. 

Python ensures that only one thread can
hold a lock at any point in time; if others request it while it’s held, they are blocked
until the lock becomes available. 

Lock objects are allocated and processed with simple
and portable calls in the _thread module that are automatically mapped to thread locking
mechanisms on the underlying platform.
"""


# Example 5-7. PP4E\System\Threads\thread-count-mutex.py
"""
synchronize access to stdout: because it is shared global,
thread outputs may be intermixed if not synchronized
"""

import _thread as thread, time 


def counter(myId, count):                                   # function run in threads
    for i in range(count):
        time.sleep(1)                                       # simulate real work
        mutex.acquire()
        print('[%s] => %s' % (myId, i))                     # print isn’t interrupted now
        mutex.release()
    

mutex = thread.allocate_lock()                              # make a global lock object
for i in range(5):                                          # spawn 5 threads
    thread.start_new_thread(counter, (i, 5))                # each thread loops 5 times


time.sleep(6)                                               # don’t exit too early
print('Main thread exiting.')                               # don’t exit too early


'''
this script is that no two threads will ever execute a print call at the same point in time; the lock ensures mutually exclusive
access to the stdout stream.

Though somewhat platform-specific, the order in which the threads check in with their
prints may still be arbitrary from run to run because they execute in parallel (getting
work done in parallel is the whole point of threads, after all); but they no longer collide
in time while printing their text.
'''
