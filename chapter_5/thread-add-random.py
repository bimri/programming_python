"Synchronizing access to shared objects and names revisited"
'''
threads need to synchronize their changes to any item that may be shared across thread
in a process—both objects and namespaces:
    • Mutable object in memory
    • Names in global scopes
    • The contents of modules

For instance, even simple global variables can require coordination if concurrent updates
are possible.
'''

"prints different results on different runs on Windows 7"

import threading, time
count = 0

def adder():
    global count
    count += 1                                              # update a shared name in global scope
    time.sleep(0.5)                                         # threads share object memory and global names
    count += 1

threads = []
for i in range(100):
    thread = threading.Thread(target=adder, args=())
    thread.start()
    threads.append(thread)

for thread in threads: thread.join()
print(count)


'''
This happens because threads overlap arbitrarily in time: statements, even the simple
assignment statements like those here, are not guaranteed to run to completion by
themselves (that is, they are not atomic).

As one thread updates the global, it may be
using the partial result of another thread’s work in progress. The net effect is this seemingly
random behavior. To make this script work correctly, we need to again use thread
locks to synchronize the updates
'''