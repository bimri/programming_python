"Named Pipes" # (Fifos)
'''
On some platforms, it is also possible to create a long-lived pipe that exists as a real
named file in the filesystem. Such files are called named pipes (or, sometimes, fifos)
because they behave just like the pipes created by the previous section’s programs.
Because fifos are associated with a real file on your computer, though, they are external
to any particular program—they do not rely on memory shared between tasks, and so
they can be used as an IPC mechanism for threads, processes, and independently
launched programs.

Once a named pipe file is created, clients open it by name and read and write data using
normal file operations. Fifos are unidirectional streams. In typical operation, a server
program reads data from the fifo, and one or more client programs write data to it. In
addition, a set of two fifos can be used to implement bidirectional communication just
as we did for anonymous pipes.

Because fifos reside in the filesystem, they are longer-lived than in-process anonymous
pipes and can be accessed by programs started independently. The unnamed, inprocess
pipe examples thus far depend on the fact that file descriptors (including pipes)
are copied to child processes’ memory. That makes it difficult to use anonymous pipes
to connect programs started independently. With fifos, pipes are accessed instead by
a filename visible to all programs running on the computer, regardless of any parent/
child process relationships. In fact, like normal files, fifos typically outlive the programs
that access them. Unlike normal files, though, the operating system synchronizes fifo
access, making them ideal for IPC.

Because of their distinctions, fifo pipes are better suited as general IPC mechanisms for
independent client and server programs. For instance, a perpetually running server
program may create and listen for requests on a fifo that can be accessed later by arbitrary
clients not forked by the server. In a sense, fifos are an alternative to the socket
port. Unlike sockets, though, fifos do not directly
support remote network connections, are not available in standard Windows Python
today, and are accessed using the standard file interface instead of the more unique
socket port numbers and calls.
'''