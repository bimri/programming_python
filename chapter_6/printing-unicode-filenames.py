'''
Python 3.X’s Unicode
orientation extends to filenames, even if they are just printed.
because filenames may contain arbitrary text, os.listdir returns filenames in two
different ways—we get back decoded Unicode strings when we pass in a normal str
argument, and still-encoded byte strings when we send a bytes:
'''

import os
print(os.listdir('.')[:8])
print(os.listdir(b'.')[:8])

 
"""
Both os.walk and glob.glob inherit this behavior for
the directory and file names they return, because they work by calling os.listdir internally
at each directory level. For all these calls, passing in a byte string argument
suppresses Unicode decoding of file and directory names. Passing a normal string assumes
that filenames are decodable per the file system’s Unicode scheme.

>>> for (dir, subs, files) in os.walk(root):
... try:
... print(dir)
... except UnicodeEncodeError:
... print(dir.encode()) # or simply punt if enocde may fail too
...
C:\py3000
C:\py3000\FutureProofPython - PythonInfo Wiki_files
C:\py3000\Oakwinter_com Code » Porting setuptools to py3k_files
b'C:\\py3000\\What\xe2\x80\x99s New in Python 3_0 \xe2\x80\x94 Python Documentation'

Moreover, this error does not occur if the script’s output is redirected to a file, either
at the shell level (bigext-tree.py c:\ > out), or by the print call itself (print(dir,
file=F)).
"""
