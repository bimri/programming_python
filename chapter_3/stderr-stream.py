"Capturing the stderr Stream"
# stderr can be similarly reset to files, pipes, and objects
# by setting the sys.stderr object

'''
Python itself uses standard error for error message text (and the IDLE GUI interface
intercepts it and colors it red by default). However, no higher-level tools for standard
error do what print and input do for the output and input streams. If you wish to print
to the error stream, you’ll want to call sys.stderr.write() explicitly

Redirecting standard errors from a shell command line is a bit more complex and less portable.
'''


"Redirection Syntax in Print Calls"
# print(stuff, file=afile) # afile is an object, not a string name      #prints stuff to afile instead of to sys.stdout.

import sys
'''
will send text the standard error stream object rather than sys.stdout for the duration
of this single print call only.
'''
print('spam' * 2, file=sys.stderr)

"""
>>> from io import StringIO
>>> buff = StringIO()
>>> print(42, file=buff)
>>> print('spam', file=buff)
>>> print(buff.getvalue())

>>> from redirect import Output
>>> buff = Output()
>>> print(43, file=buff)
>>> print('eggs', file=buff)
>>> print(buff.text)
"""
