"Anonymous Pipes"
'''
Pipes, a cross-program communication device, are implemented by your operating
system and made available in the Python standard library. Pipes are unidirectional
channels that work something like a shared memory buffer, but with an interface resembling
a simple file on each of two ends. In typical use, one program writes data on
one end of the pipe, and another reads that data on the other end. Each program sees
only its end of the pipes and processes it using normal Python file calls.

Pipes are much more within the operating system, though. For instance, calls to read
a pipe will normally block the caller until data becomes available (i.e., is sent by the
program on the other end) instead of returning an end-of-file indicator. Moreover, read
calls on a pipe always return the oldest data written to the pipe, resulting in a first-infirst-
out model—the first data written is the first to be read. Because of such properties,
pipes are also a way to synchronize the execution of independent programs.

Pipes come in two flavors—anonymous and named. Named pipes (often called fifos)
are represented by a file on your computer. Because named pipes are really external
files, the communicating processes need not be related at all; in fact, they can be independently
started programs.

By contrast, anonymous pipes exist only within processes and are typically used in
conjunction with process forks as a way to link parent and spawned child processes
within an application. Parent and child converse over shared pipe file descriptors, which
are inherited by spawned processes. Because threads run in the same process and share
all global memory in general, anonymous pipes apply to them as well.
'''