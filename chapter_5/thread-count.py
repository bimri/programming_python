"Running multiple threads"
"""
thread basics: start 5 copies of a function running in parallel;
uses time.sleep so that the main thread doesn't die too early--
this kills all other threads on some platforms; stdout is shared:
thread outputs may be intermixed in this version arbitrarily.
"""

import _thread as thread, time


def counter(myId, count):                                   # function run in threads
    for i in range(count):
        time.sleep(1)                                       # simulate real work
        print('[%s] => %s' % (myId, i))

    

for i in range(5):                                          # spawn 5 threads
    thread.start_new_thread(counter, (i, 5))                # each thread loops 5 times


time.sleep(6)
print('Main thread exiting.')                               # don't exit too early


'''
Each parallel copy of the counter function simply counts from zero up to four here and
prints a message to standard output for each count.
Notice how this script sleeps for 6 seconds at the end. On Windows and Linux machines
this has been tested on, the main thread shouldn’t exit while any spawned threads are
running if it cares about their work; if it does exit, all spawned threads are immediately
terminated.
'''


"""
If this looks odd, it’s because it should. In fact, this demonstrates probably the most
unusual aspect of threads. What’s happening here is that the output of the 5 threads
run in parallel is intermixed—because all the threaded function calls run in the same
process, they all share the same standard output stream (in Python terms, there is just
one sys.stdout file between them, which is where printed text is sent). The net effect
is that their output can be combined and confused arbitrarily. In fact, this script’s
output can differ on each run. This jumbling of output grew even more pronounced in
Python 3, presumably due to its new file output implementation.
"""