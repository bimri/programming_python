"""
fork basics: start 5 copies of this program running in parallel with
the original; each copy counts up to 5 on the same stdout stream--forks
copy process memory, including file descriptors; fork doesn't currently
work on Windows without Cygwin: use os.spawnv or multiprocessing on
Windows instead; spawnv is roughly like a fork+exec combination;
"""

import os, time

def counter(count):                                         # run in new process
    for i in range(count):
        time.sleep(1)                                       # simulate real work
        print('[%s] => %s' % (os.getpid(), i))
    

for i in range(5):
    pid = os.fork()
    if pid != 0:
        print('Process %d spawned' % pid)
    else:
        counter(5)                                          # child process ends
        os._exit(0)                                         # run in new process
    

print('Main process exiting.')


'''
Technically, a forked process gets a copy of the original process’s global memory,
including open file descriptors. Because of that, global objects like files start out with
the same values in a child process, so all the processes here are tied to the same single
stream. But it’s important to remember that global memory is copied, not shared; if a
child process changes a global object, it changes only its own copy.
'''
