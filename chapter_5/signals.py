"Signals"
'''
For lack of a better analogy, signals are a way to poke a stick at a process. Programs
generate signals to trigger a handler for that signal in another process. The operating
system pokes, too—some signals are generated on unusual system events and may kill
the program if not handled. If this sounds a little like raising exceptions in Python, it
should; signals are software-generated events and the cross-process analog of exceptions.
Unlike exceptions, though, signals are identified by number, are not stacked, and
are really an asynchronous event mechanism outside the scope of the Python interpreter
controlled by the operating system.

In order to make signals available to scripts, Python provides a signal module that
allows Python programs to register Python functions as handlers for signal events. This
module is available on both Unix-like platforms and Windows (though the Windows
version may define fewer kinds of signals to be caught).
'''


"""
signals must be used with cautions not made obvious. For instance, some system calls don’t react well to being interrupted
by signals, and only the main thread can install signal handlers and respond to
signals in a multithreaded program.

signals provide an event-based communication mechanism.
They are less powerful than data streams such as pipes, but are sufficient in situations
in which you just need to tell a program that something important has occurred and
don’t need to pass along any details about the event itself. Signals are sometimes also
combined with other IPC tools. For example, an initial signal may inform a program
that a client wishes to communicate over a named pipe—the equivalent of tapping
someone’s shoulder to get their attention before speaking. Most platforms reserve one
or more SIGUSR signal numbers for user-defined events of this sort. Such an integration
structure is sometimes an alternative to running a blocking input call in a spawned
thread.
"""
