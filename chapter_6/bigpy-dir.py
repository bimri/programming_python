"""
Find the largest Python source file in a single directory.
Search Windows Python source lib, unless dir command-line arg.
"""

import os, glob, sys 
dirname = r'C:\Python38\Lib' if len(sys.argv) == 1 else sys.argv[1]

allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))


allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])


'''
When run, this script scans the Python standard library’s
source directory on Windows, unless you pass a different directory on the command
line, and it prints both the two smallest and largest files it finds
'''

"""
This script uses the glob module to run through a directory’s files and detects the largest
by storing sizes and names on a list that is sorted at the end—because size appears first
in the list’s tuples, it will dominate the ascending value sort, and the largest percolates
to the end of the list.
"""
