"os.open mode flags"
'''
So why the extra file tools in os? In short, they give more low-level control over file
processing. The built-in open function is easy to use, but it may be limited by the underlying
filesystem that it uses, and it adds extra behavior that we do not want. The
os module lets scripts be more specific—for example, the following opens a descriptorbased
file in read-write and binary modes by performing a binary “or” on two mode
flags exported by os:
'''
import os
fdfile = os.open(r'E:\practice\programming_python\dbs\output.txt', os.O_RDWR | os.O_BINARY)
print(os.read(fdfile, 20))


os.lseek(fdfile, 0, 0)                                          # go back to start of file
print(os.read(fdfile, 100))                                     # binary mode retains "\r\n"


os.lseek(fdfile, 0, 0)
print(os.write(fdfile, b'HELLO'))                              # override first 5 bytes


'In this case, binary mode strings rb+ and r+b in the basic open call are equivalent:'
file = open(r'E:\practice\programming_python\dbs\output.txt', 'rb+')
print(file.read(20))

file.seek(0)
file.read(100)
print(file.write(b'HELLO'))

file.seek(0)
print(file.read())


'''
But on some systems, os.open flags let us specify more advanced things like exclusive
access (O_EXCL) and nonblocking modes (O_NONBLOCK) when a file is opened. Some of
these flags are not portable across platforms (another reason to use built-in file objects
most of the time); see the library manual or run a dir(os) call on your machine for an
exhaustive list of other open flags available.

One final note here: using os.open with the O_EXCL fl ag i s the most portabl e way to lock
files for concurrent updates or other process synchronization in Python today.
'''
