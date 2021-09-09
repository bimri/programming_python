"The multiprocessing Module"
'''
Python’s standard library multiprocessing module package allows
scripts to spawn processes using an API very similar to the threading module.

This relatively new package works on both Unix and Windows, unlike low-level process
forks.

It supports a process spawning model which is largely platform-neutral, and
provides tools for related goals, such as IPC, including locks, pipes, and queues. In
addition, because it uses processes instead of threads to run code in parallel, it effectively
works around the limitations of the thread GIL. 

Hence, multiprocessing allows
the programmer to leverage the capacity of multiple processors for parallel tasks, while
retaining much of the simplicity and portability of the threading model.
'''


'Why multiprocessing?'
'''
In more specific terms,
although this module’s performance may not compete with that of pure threads or
process forks for some applications, this module offers a compelling solution for many:
    • Compared to raw process forks, you gain cross-platform portability and powerful
    IPC tools.
    
    • Compared to threads, you essentially trade some potential and platformdependent
    extra task start-up time for the ability to run tasks in truly parallel fashion
    on multi-core or multi-CPU machines.

On the other hand, this module imposes some constraints and tradeoffs that threads
do not:
    • Since objects are copied across process boundaries, shared mutable state does not
    work as it does for threads—changes in one process are not generally noticed in
    the other. Really, freely shared state may be the most compelling reason to use
    threads; its absence in this module may prove limiting in some threading contexts.
    
    • Because this module requires pickleability for both its processes on Windows, as
    well as some of its IPC tools in general, some coding paradigms are difficult or
    nonportable—especially if they use bound methods or pass unpickleable objects
    such as sockets to spawned processes.    
'''

"""
For instance, common coding patterns with lambda that work for the threading module
cannot be used as process target callables in this module on Windows, because they
cannot be pickled. Similarly, because bound object methods are also not pickleable, a
threaded program may require a more indirect design if it either runs bound methods
in its threads or implements thread exit actions by posting arbitrary callables (possibly
including bound methods) on shared queues. The in-process model of threads supports
such direct lambda and bound method use, but the separate processes of
multiprocessing do not.
"""


"""
Fundamentally, though, because multiprocessing is based on separate processes, it
may be best geared for tasks which are relatively independent, do not share mutable
object state freely, and can make do with the message passing and shared memory tools
provided by this module. This includes many applications, but this module is not necessarily
a direct replacement for every threaded program, and it is not an alternative to
process forks in all contexts.
"""
