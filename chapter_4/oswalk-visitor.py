"The os.walk visitor"
'''
To make it easy to apply an operation to all files in a complete directory tree, Python
comes with a utility that scans trees for us and runs code we provide at every directory
along the way: the os.walk function is called with a directory root name and automatically
walks the entire tree at root and below.

Operationally, os.walk is a generator function—at each directory in the tree, it yields a
three-item tuple, containing the name of the current directory as well as lists of both
all the files and all the subdirectories in the current directory. Because it’s a generator,
its walk is usually run by a for loop (or other iteration tool); on each iteration, the
walker advances to the next subdirectory, and the loop runs its code for the next level
of the tree (for instance, opening and searching all the files at that level).
'''
import os

# dirname = r'E:\practice\programming_python'

for (dirname, subshere, fileshere) in os.walk('.'):
    print('[' + dirname + ']')
    for fname in fileshere:
        print(os.path.join(dirname, fname))                         # handle one file
