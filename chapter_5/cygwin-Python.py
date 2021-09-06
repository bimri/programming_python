"More on Cygwin Python for Windows"   
'''
os.fork call is present in the Cygwin version of Python on Windows.
Even though this call is missing in the standard version of Python for Windows, you
can fork processes on Windows with Python if you install and use Cygwin.
the Cygwin fork call is not as efficient and does not work exactly the same as a fork on
true Unix systems.

Cygwin is a free, open source package which includes a library that attempts to provide
a Unix-like API for use on Windows machines, along with a set of command-line tools
that implement a Unix-like environment. It makes it easier to apply Unix skills and
code on Windows computers.

According to its FAQ documentation, though, “Cygwin fork() essentially works like a
noncopy on write version of fork() (like old Unix versions used to do). Because of this
it can be a little slow. In most cases, you are better off using the spawn family of calls
if possible.”
'''