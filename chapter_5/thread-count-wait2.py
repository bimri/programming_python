'''
Depending on how your threads run, this could be even simpler: since threads share
global memory anyhow, we can usually achieve the same effect with a simple global
list of integers instead of locks.

the module’s namespace (scope) is
shared by top-level code and the threaded function, as before. exitmutexes refers to the
same list object in the main thread and all threads it spawns. Because of that, changes
made in a thread are still noticed in the main thread without resorting to extra locks.
'''

import _thread as thread

stdoutmutex = thread.allocate_lock()
exitmutexes = [False] * 10


def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myId, i))
        stdoutmutex.release()
    exitmutexes[myId] = True                    # signal main thread


for i in range(10):
    thread.start_new_thread(counter, (i, 100))


while False in exitmutexes: pass
print('Main thread exiting.')


"""
The output of this script is similar to the prior—10 threads counting to 100 in parallel
and synchronizing their prints along the way. In fact, both of the last two counting
thread scripts produce roughly the same output as the original thread_count.py, albeit
without stdout corruption and with larger counts and different random ordering of
output lines. The main difference is that the main thread exits immediately after (and
no sooner than!) the spawned child threads:
"""
