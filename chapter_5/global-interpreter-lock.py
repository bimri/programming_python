"More on the Global Interpreter Lock"
'''
Python, the implementation of Python’s threads can have impacts on both performance
and coding. 

Strictly speaking, Python currently uses the global interpreter lock (GIL) mechanism
introduced at the start of this section, which guarantees that one thread, at most, is
running code within the Python interpreter at any given point in time. In addition, to
make sure that each thread gets a chance to run, the interpreter automatically switches
its attention between threads at regular intervals.

This scheme avoids problems that could arise if multiple threads were to update Python
system data at the same time.

Moreover, even though the GIL prevents more than one Python thread from running
at the same time, it is not enough to ensure thread safety in general, and it does not
address higher-level synchronization issues at all.

Locks are not strictly required for all shared object access, especially if a single thread
updates an object inspected by other threads. As a rule of thumb, though, you should
generally use locks to synchronize threads whenever update rendezvous are possible
instead of relying on artifacts of the current thread implementation.
'''

"The thread switch interval"
'''
Some concurrent updates might work without locks if the thread-switch interval is set
high enough to allow each thread to finish without being swapped out. The
sys.setcheckinterval(N) call sets the frequency with which the interpreter checks for
things like thread switches and signal handlers.
This interval defines the number of bytecode instructions before a switch. It does not
need to be reset for most programs, but it can be used to tune thread performance.
Setting higher values means switches happen less often: threads incur less overhead but
they are less responsive to events. Setting lower values makes threads more responsive
to events but increases thread switch overhead.
'''

"Atomic operations"
'''
Because of the way Python uses the GIL to synchronize threads’ access to the virtual
machine, whole statements are not generally thread-safe, but each bytecode instruction
is. Because of this bytecode indivisibility, some Python language operations are threadsafe—
also called atomic, because they run without interruption—and do not require
the use of locks or queues to avoid concurrent update issues.
'''

"C API thread considerations"
'''
Also note that even though the Python code in Python threads cannot truly overlap in
time due to the GIL synchronization, the C-coded portions of threads can. Any number
may be running in parallel, as long as they do work outside the scope of the Python
virtual machine. In fact, C threads may overlap both with other C threads and with
Python language threads run in the virtual machine.
'''

"A process-based alternative: multiprocessing"
'''
multiprocessing module—a standard library tool that seeks to combine the simplicity
and portability of threads with the benefits of processes, by implementing a threadinglike
API that runs processes instead of threads. It seeks to address the portability issue
of processes, as well as the multiple-CPU limitations imposed in threads by the GIL,
but it cannot be used as a replacement for forking in some contexts, and it imposes
some constraints that threads do not, which stem from its process-based model (for
instance, mutable object state is not directly shared because objects are copied across
process boundaries, and unpickleable objects such as bound methods cannot be as
freely used).
'''