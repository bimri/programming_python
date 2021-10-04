"Stream requirements"
"""
test effect of connecting standard streams to text and binary mode files
same holds true for socket.makefile: print requires text mode, but text
mode precludes unbuffered mode -- use -u or sys.stdout.flush() calls
"""

import sys

def reader(F):
    tmp, sys.stdin = sys.stdin, F
    line = input()
    print(line)
    sys.stdin = tmp

reader( open('test-stream-modes.py') )         # works: input() returns text
reader( open('test-stream-modes.py', 'rb') )   # works: but input() returns bytes

def writer(F):
    tmp, sys.stdout = sys.stdout, F
    print(99, 'spam')
    sys.stdout = tmp

writer( open('temp', 'w') )             # works: print() passes text str to .write()
print(open('temp').read())

writer( open('temp', 'wb') )            # FAILS on print: binary mode requires bytes
writer( open('temp', 'w', 0) )          # FAILS on open: text must be unbuffered


'''
The same rules apply to socket wrapper file objects created with a socket’s makefile
method—they must be opened in text mode for print and should be opened in text
mode for input if we wish to receive text strings, but text mode prevents us from using
fully unbuffered file mode altogether:
>>> from socket import *
>>> s = socket() # defaults to tcp/ip (AF_INET, SOCK_STREAM)
>>> s.makefile('w', 0) # this used to work in Python 2.X
Traceback (most recent call last):
File "C:\Python31\lib\socket.py", line 151, in makefile
ValueError: unbuffered streams must be binary
'''
