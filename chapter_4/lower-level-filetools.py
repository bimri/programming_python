"Lower-Level File Tools in the os Module"
'''
The os module contains an additional set of file-processing functions that are distinct
from the built-in file object tools:
    os.open( path, flags, mode )
        Opens a file and returns its descriptor
    os.read( descriptor, N )
        Reads at most N bytes and returns a byte string
    os.write( descriptor, string )
        Writes bytes in byte string string to the file
    os.lseek( descriptor, position , how )
        Moves to position in the file

Technically, os calls process files by their descriptors, which are integer codes or “handles”
that identify files in the operating system. Descriptor-based files deal in raw bytes,
and have no notion of the line-end or Unicode translations for text.

In fact, apart from extras like buffering, descriptor-based files generally
correspond to binary mode file objects, and we similarly read and write bytes
strings, not str strings. However, because the descriptor-based file tools in os are lower
level and more complex than the built-in file objects created with the built-in open
function, you should generally use the latter for all but very special file-processing
needs.
'''

"Using os.open files"
'''
Although built-in file objects and os module descriptor files are processed
with distinct tool sets, they are in fact related—the file system used by file objects simply
adds a layer of logic on top of descriptor-based files.

In fact, the fileno file object method returns the integer descriptor associated with a
built-in file object. For instance, the standard stream file objects have descriptors 0, 1,
and 2; calling the os.write function to send data to stdout by descriptor has the same
effect as calling the sys.stdout.write method:
'''
import sys

for stream in (sys.stdin, sys.stdout, sys.stderr):
    print(stream.fileno())

print('-' * 40)
print(sys.stdout.write('Hello stdio world\n'))              # write via file method
print('-' * 40)


import os 
print(
    os.write(1, b'Hello descriptor world\n')                # write via os module
)
print('-' * 40)

file = open('output.txt', 'w')                              # create external file, object
file.write('Hello file world\n')                            # write via file object method
file.flush()                                                # else os.write to disk first
fd = file.fileno()                                          # get file descriptor from object
print(fd)


os.write(fd, b'Hello file descriptor world\n')               # write via os module
file.close()
print('-' * 40)

# C:\temp> type spam.txt # lines from both schemes