"Wrapping descriptors in file objects"
'''
We saw earlier how to go from file object to field descriptor with the fileno file object
method; given a descriptor, we can use os module tools for lower-level file access to
the underlying file. We can also go the other way—the os.fdopen call wraps a file descriptor
in a file object. Because conversions work both ways, we can generally use
either tool set—file object or os module:
'''
import os

fdfile = os.open(r'E:\practice\programming_python\dbs\mydata.txt', (os.O_RDWR | os.O_BINARY))
print(fdfile)


objfile = os.fdopen(fdfile, 'rb')
print(objfile.read())

'''
we can wrap a file descriptor in either a binary or text-mode file object: in text
mode, reads and writes perform the Unicode encodings and line-end translations
'''
fdfile = os.open(r'E:\practice\programming_python\dbs\mydata.txt', (os.O_RDWR | os.O_BINARY))
objfile = os.fdopen(fdfile, 'r')
print(objfile.read())


'''
In Python 3.X, the built-in open call also accepts a file descriptor instead of a file name
string; in this mode it works much like os.fdopen, but gives you greater control—for
example, you can use additional arguments to specify a nondefault Unicode encoding
for text and suppress the default descriptor close.
'''
import os
fdfile = os.open(r'E:\practice\programming_python\dbs\mydata.txt', (os.O_RDWR | os.O_BINARY))
print(fdfile)

objfile = open(fdfile, 'r', encoding='latin1', closefd=False)
print(objfile.read())

objfile = os.fdopen(fdfile, 'r', encoding='latin1', closefd=True)
objfile.seek(0)
print(objfile.read())
