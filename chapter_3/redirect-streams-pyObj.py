"Redirecting Streams to Python Objects"
'''
All of the previous standard stream redirections work for programs written in any language
that hook into the standard streams and rely more on the shell’s command-line
processor than on Python itself. Command-line redirection syntax like < filename and
| program is evaluated by the shell, not by Python. A more Pythonesque form of redirection
can be done within scripts themselves by resetting sys.stdin and sys.stdout to
file-like objects.

The main trick behind this mode is that anything that looks like a file in terms of
methods will work as a standard stream in Python. The object’s interface (sometimes
called its protocol), and not the object’s specific datatype, is all that matters. That is:
    • Any object that provides file-like read methods can be assigned to sys.stdin to
    make input come from that object’s read methods.
    • Any object that defines file-like write methods can be assigned to sys.stdout; all
    standard output will be sent to that object’s methods.

Because print and input simply call the write and readline methods of whatever objects
sys.stdout and sys.stdin happen to reference, we can use this technique to both provide
and intercept standard stream text with objects implemented as classes.

If you’ve already studied Python, you probably know that such plug-and-play compatibility
is usually called polymorphism—it doesn’t matter what an object is, and it
doesn’t matter what its interface does, as long as it provides the expected interface.
This liberal approach to datatypes accounts for much of the conciseness and flexibility
of Python code. Here, it provides a way for scripts to reset their own streams. 
 shows a utility module that demonstrates this concept.

Because print and input simply call the write and readline methods of whatever objects
sys.stdout and sys.stdin happen to reference, we can use this technique to both provide
and intercept standard stream text with objects implemented as classes.
'''
