"Scanning the Standard Library Tree"
'''
The prior section’s solution works, but it’s obviously a partial answer—Python files
are usually located in more than one directory. Even within the standard library, there
are many subdirectories for module packages, and they may be arbitrarily nested. We
really need to traverse an entire directory tree. Moreover, the first output above is difficult
to read; Python’s pprint (for “pretty print”) module can help here.
'''

"""
Find the largest Python source file in an entire directory tree.
Search the Python source lib, use pprint to display results nicely.
"""

import os, sys, pprint
trace = False
if sys.platform.startswith('win'):
    dirname = r'C:\Python38\Lib'                            # Windows
else:
    dirname = '/usr/lib/python'                             # Unix, Linux, Cygwin


allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace: print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))
        

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])


'''
When run, this new version uses os.walk to search an entire tree of directories for the
largest Python source file. Change this script’s trace variable if you want to track its
progress through the tree. As coded, it searches the Python standard library’s source
tree, tailored for Windows and Unix-like locations:
'''
