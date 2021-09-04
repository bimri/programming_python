"Other os module file tools"
'''
The os module also includes an assortment of file tools that accept a file pathname
string and accomplish file-related tasks such as renaming (os.rename), deleting
(os.remove), and changing the file’s owner and permission settings (os.chown,
os.chmod).

>>> os.chmod('spam.txt', 0o777) # enable all accesses

This os.chmod file permissions call passes a 9-bit string composed of three sets of three
bits each. From left to right, the three sets represent the file’s owning user, the file’s
group, and all others. Within each set, the three bits reflect read, write, and execute
access permissions. When a bit is “1” in this string, it means that the corresponding
operation is allowed for the assessor. For instance, octal 0777 is a string of nine “1”
bits in binary, so it enables all three kinds of accesses for all three user groups; octal
0600 means that the file can be read and written only by the user that owns it (when
written in binary, 0600 octal is really bits 110 000 000).

>>> os.rename(r'C:\temp\spam.txt', r'C:\temp\eggs.txt')         # from, to

>>> os.remove(r'C:\temp\spam.txt')                              # delete file?
WindowsError: [Error 2] The system cannot find the file specified: 'C:\\temp\\...'

>>> os.remove(r'C:\temp\eggs.txt')
'''

"The os module also exports the stat system call:"
open(r'E:\practice\programming_python\dbs\spam', 'w').write('spam, spam, spam\n')       # create a file  

import os
info = os.stat(r'E:\practice\programming_python\dbs\spam')
print(info)
print(info.st_size)                                                                     # file size; via named-tuple item attr names
print(info.st_mtime)


import stat
print(stat.S_ISREG(info.st_mode))
print(info[stat.ST_MODE], info[stat.ST_SIZE])                                           # via stat module presets
print(stat.S_ISDIR(info.st_mode), stat.S_ISREG(info.st_mode))


# both of these operations are available in the os.path module
path = r'E:\practice\programming_python\dbs\spam'
print(
    os.path.isdir(path),
    os.path.isfile(path),
    os.path.islink(path),
    os.path.ismount(path),
    os.path.exists(path),
    os.path.lexists(path),
    os.path.getsize(path),
)
