"The queue Module"
'''
realistically scaled threaded programs are often structured
as a set of producer and consumer threads, which communicate by placing data on,
and taking it off of, a shared queue. As long as the queue synchronizes access to itself,
this automatically synchronizes the threads’ interactions.
'''

"""
The Python queue module implements this storage device. It provides a standard queue
data structure—a first-in first-out (fifo) list of Python objects, in which items are added
on one end and removed from the other.
"""

'''
Unlike normal lists, though, the queue object is automatically controlled with thread
lock acquire and release operations, such that only one thread can modify the queue
at any given point in time. Because of this, programs that use a queue for their crossthread
communication will be thread-safe and can usually avoid dealing with locks of
their own for data passed between threads.
'''
