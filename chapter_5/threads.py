"Threads"
'''
Threads are another way to start activities running at the same time. In short, they run
a call to a function (or any other type of callable object) in parallel with the rest of the
program. Threads are sometimes called “lightweight processes,” because they run in
parallel like forked processes, but all of them run within the same single process. While
processes are commonly used to start independent programs, threads are commonly
used for tasks such as nonblocking input calls and long-running tasks in a GUI. They
also provide a natural model for algorithms that can be expressed as independently
running tasks.

For applications that can benefit from parallel processing, some developers
consider threads to offer a number of advantages:

Performance
Because all threads run within the same process, they don’t generally incur a big
startup cost to copy the process itself. The costs of both copying forked processes
and running threads can vary per platform, but threads are usually considered less
expensive in terms of performance overhead.

Simplicity
To many observers, threads can be noticeably simpler to program, too, especially
when some of the more complex aspects of processes enter the picture (e.g., process
exits, communication schemes, and zombie processes, covered in Chapter 12). 

Shared global memory
On a related note, because threads run in a single process, every thread shares the
same global memory space of the process. This provides a natural and easy way
for threads to communicate—by fetching and setting names or objects accessible
to all the threads. To the Python programmer, this means that things like global
scope variables, passed objects and their attributes, and program-wide interpreter
components such as imported modules are shared among all threads in a program;
if one thread assigns a global variable, for instance, its new value will be seen by
other threads. Some care must be taken to control access to shared items, but to
some this seems generally simpler to use than the process communication tools
necessary for forked processes, which we’ll meet later in this chapter and book
(e.g., pipes, streams, signals, sockets, etc.). Like much in programming, this is not
a universally shared view, however, so you’ll have to weigh the difference for your
programs and platforms yourself.

Portability
Perhaps most important is the fact that threads are more portable than forked
processes. At this writing, os.fork is not supported by the standard version of
Python on Windows, but threads are. If you want to run parallel tasks portably in
a Python script today and you are unwilling or unable to install a Unix-like library
such as Cygwin on Windows, threads may be your best bet. Python’s thread tools
automatically account for any platform-specific thread differences, and they provide
a consistent interface across all operating systems. Having said that, the relatively
new multiprocessing module described later in this chapter offers another
answer to the process portability issue in some use cases.
'''


"""
So what’s the catch? There are three potential downsides you should be aware of before
you start spinning your threads:
    Function calls versus programs
        First of all, threads are not a way—at least, not a direct way—to start up another
        program. Rather, threads are designed to run a call to a function (technically, any
        callable, including bound and unbound methods) in parallel with the rest of the
        program. As we saw in the prior section, by contrast, forked processes can either
        call a function or start a new program. Naturally, the threaded function can run
        scripts with the exec built-in function and can start new programs with tools such
        as os.system, os.popen and the subprocess module, especially if doing so is itself a
        long-running task. But fundamentally, threads run in-program functions.
        In practice, this is usually not a limitation. For many applications, parallel functions
        are sufficiently powerful. For instance, if you want to implement nonblocking input
        and output and avoid blocking a GUI or its users with long-running tasks, threads
        do the job; simply spawn a thread to run a function that performs the potentially
        long-running task. The rest of the program will continue independently.
    
    Thread synchronization and queues
        Secondly, the fact that threads share objects and names in global process memory
        is both good news and bad news—it provides a communication mechanism, but
        we have to be careful to synchronize a variety of operations. As we’ll see, even
        operations such as printing are a potential conflict since there is only one
        sys.stdout per process, which is shared by all threads. 
        Luckily, the Python queue module, described in this section, makes this simple:
        realistic threaded programs are usually structured as one or more producer (a.k.a.
        worker) threads that add data to a queue, along with one or more consumer threads
        that take the data off the queue and process it. In a typical threaded GUI, for
        example, producers may download or compute data and place it on the queue; the
        consumer—the main GUI thread—checks the queue for data periodically with a
        timer event and displays it in the GUI when it arrives. Because the shared queue is
        thread-safe, programs structured this way automatically synchronize much crossthread
        data communication.
    
    The global interpreter lock (GIL)
        Finally, as we’ll learn in more detail later in this section, Python’s implementation
        of threads means that only one thread is ever really running its Python language
        code in the Python virtual machine at any point in time. Python threads are true
        operating system threads, but all threads must acquire a single shared lock when
        they are ready to run, and each thread may be swapped out after running for a short
        period of time (currently, after a set number of virtual machine instructions, though
        this implementation may change in Python 3.2).
        Because of this structure, the Python language parts of Python threads cannot today
        be distributed across multiple CPUs on a multi-CPU computer. To leverage more
        than one CPU, you’ll simply need to use process forking, not threads (the amount
        and complexity of code required for both are roughly the same). Moreover, the
        parts of a thread that perform long-running tasks implemented as C extensions can
        run truly independently if they release the GIL to allow the Python code of other
        threads to run while their task is in progress. Python code, however, cannot truly
        overlap in time.
        The advantage of Python’s implementation of threads is performance—when it
        was attempted, making the virtual machine truly thread-safe reportedly slowed all
        programs by a factor of two on Windows and by an even larger factor on Linux.
        Even nonthreaded programs ran at half speed.
        Even though the GIL’s multiplexing of Python language code makes Python
        threads less useful for leveraging capacity on multiple CPU machines, threads are
        still useful as programming tools to implement nonblocking operations, especially
        in GUIs. Moreover, the newer multiprocessing module we’ll meet later offers another
        solution here, too—by providing a portable thread-like API that is implemented
        with processes, programs can both leverage the simplicity and
        programmability of threads and benefit from the scalability of independent processes
        across CPUs.
"""
