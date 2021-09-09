"IPC Tools: Pipes, Shared Memory, and Queues"
'''
the multiprocessing
module also provides portable message passing tools specifically geared to this purpose
for the processes it spawns:
    • Its Pipe object provides an anonymous pipe, which serves as a connection between
    two processes. When called, Pipe returns two Connection objects that represent the
    ends of the pipe. Pipes are bidirectional by default, and allow arbitrary pickleable
    Python objects to be sent and received.

    • Its Value and Array objects implement shared process/thread-safe memory for
    communication between processes. These calls return scalar and array objects
    based in the ctypes module and created in shared memory, with access synchronized
    by default.

    • Its Queue object serves as a FIFO list of Python objects, which allows multiple producers
    and consumers. A queue is essentially a pipe with extra locking mechanisms
    to coordinate more arbitrary accesses, and inherits the pickleability constraints of
    Pipe.
'''

"""
Because these devices are safe to use across multiple processes, they can often serve to
synchronize points of communication and obviate lower-level tools like locks, much
the same as the thread queues we met earlier. As usual, a pipe (or a pair of them) may
be used to implement a request/reply model. Queues support more flexible models; in
fact, a GUI that wishes to avoid the limitations of the GIL might use the
multiprocessing module’s Process and Queue to spawn long-running tasks that post
results, rather than threads. As mentioned, although this may incur extra start-up
overhead on some platforms, unlike threads today, tasks coded this way can be as truly
parallel as the underlying platform allows.
"""

"""
Most other Python object types, including classes and simple functions, work fine on
pipes and queues.

Also keep in mind that because they are pickled, objects transferred this way are effectively
copied in the receiving process; direct in-place changes to mutable objects’ state
won’t be noticed in the sender. This makes sense if you remember that this package
runs independent processes with their own memory spaces; state cannot be as freely
shared as in threading, regardless of which IPC tools you use.
"""
