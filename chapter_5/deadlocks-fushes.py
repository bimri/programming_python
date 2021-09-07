"Output stream buffering revisited: Deadlocks and flushes"
'''
The two processes of the prior section’s example engage in a simple dialog, but it’s
already enough to illustrate some of the dangers lurking in cross-program communications.
First of all, notice that both programs need to write to stderr to display a
message; their stdout streams are tied to the other program’s input stream. Because
processes share file descriptors, stderr is the same in both parent and child, so status
messages show up in the same place.

More subtly, note that both parent and child call sys.stdout.flush after they print text
to the output stream. Input requests on pipes normally block the caller if no data is
available, but it seems that this shouldn’t be a problem in our example because there
are as many writes as there are reads on the other side of the pipe.

This output buffering is really a function of the system libraries used to access pipes,
not of the pipes themselves (pipes do queue up output data, but they never hide it from
readers!).
'''


"""
In general terms, if your programs engage in a two-way dialog like this, there are a
variety of ways to avoid buffering-related deadlock problems:
    • Flushes: As demonstrated in Examples 5-22 and 5-23, manually flushing output
    pipe streams by calling the file object flush method is an easy way to force buffers
    to be cleared. Use sys.stdout.flush for the output stream used by print.
    
    • Arguments: As introduced earlier in this chapter, the -u Python command-line flag
    turns off full buffering for the sys.stdout stream in Python programs. Setting your
    PYTHONUNBUFFERED environment variable to a nonempty value is equivalent to passing
    this flag but applies to every program run.
    
    • Open modes: It’s possible to use pipes themselves in unbuffered mode. Either use
    low-level os module calls to read and write pipe descriptors directly, or pass a buffer
    size argument of 0 (for unbuffered) or 1 (for line-buffered) to os.fdopen to disable
    buffering in the file object used to wrap the descriptor. You can use open arguments
    the same way to control buffering for output to fifo files (described in the next
    section). Note that in Python 3.X, fully unbuffered mode is allowed only for binary
    mode files, not text.
    
    • Command pipes: As mentioned earlier in this chapter, you can similarly specify
    buffering mode arguments for command-line pipes when they are created by
    os.popen and subprocess.Popen, but this pertains to the caller’s end of the pipe, not
    those of the spawned program. Hence it cannot prevent delayed outputs from the
    latter, but can be used for text sent to another program’s input pipe.
    
    • Sockets: As we’ll see later, the socket.makefile call accepts a similar buffering mode
    argument for sockets (described later in this chapter and book), but in Python 3.X
    this call requires buffering for text-mode access and appears to not support linebuffered
    mode (more on this on Chapter 12).
    
    • Tools: For more complex tasks, we can also use higher-level tools that essentially
    fool a program into believing it is connected to a terminal. These address programs
    not written in Python, for which neither manual flush calls nor -u are an option.
"""


'''
Thread can avoid blocking a main GUI, too, but really just delegate the problem (the
spawned thread will still be deadlocked). Of the options listed, the first two—manual
flushes and command-line arguments—are often the simplest solutions. In fact, because
it is so useful, the second technique listed above merits a few more words. Try
this: comment-out all the sys.stdout.flush calls in Examples 5-22 and 5-23 (the files
pipes.py and pipes-testchild.py) and change the parent’s spawn call in pipes.py to this
(i.e., add a -u command-line argument):
    spawn('python', '-u', 'pipes-testchild.py', 'spam')

Then start the program with a command line like this: python -u pipes.py. It will work
as it did with the manual stdout flush calls, because stdout will be operating in unbuffered
mode in both parent and child.
'''

"""
Anonymous pipes allow related tasks to communicate but are not directly suited for
independently launched programs.
"""
