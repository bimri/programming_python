"Scanning the Module Search Path"
"""
Find the largest Python source file on the module import search path.
Skip already-visited directories, normalize path and case so they will
match properly, and include line counts in pprinted result. It's not
enough to use os.environ['PYTHONPATH']: this is a subset of sys.path.
"""

import sys, os, pprint
trace =  0 # 1=dirs, 2=+files

visited = {}
allsizes = []
for srcdir in sys.path:
    for (thisDir, subsHere, filesHere) in os.walk(srcdir):
        if trace > 0: print(thisDir)
        thisDir = os.path.normpath(thisDir)
        fixcase = os.path.normcase(thisDir)
        if fixcase in visited: continue
        else: visited[fixcase] = True
        for filename in filesHere:
            if filename.endswith('.py'):
                if trace > 1: print('...', filename)
                pypath = os.path.join(thisDir, filename)
                try:
                    psize = os.path.getsize(pypath)
                except os.error:
                    print('skipping', pypath, sys.exc_info()[0])
                else:
                    pylines = len(open(pypath, 'rb').readlines())
                    allsizes.append((psize, pylines, pypath))
                
            
print('By size...')
allsizes.sort()
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])

pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])



'''
When run, this script marches down the module import path and, for each valid directory
it contains, attempts to search the entire tree rooted there. In fact, it nests loops
three deep—for items on the path, directories in the item’s tree, and files in the directory.
Because the module path may contain directories named in arbitrary ways, along
the way this script must take care to:
    • Normalize directory paths—fixing up slashes and dots to map directories to a
    common form.
    
    • Normalize directory name case—converting to lowercase on case-insensitive Windows,
    so that same names match by string equality, but leaving case unchanged
    on Unix, where it matters.
    
    • Detect repeats to avoid visiting the same directory twice (the same directory might
    be reached from more than one entry on sys.path).
    
    • Skip any file-like item in the tree for which os.path.getsize fails (by default
    os.walk itself silently ignores things it cannot treat as directories, both at the top
    of and within the tree).
    
    • Avoid potential Unicode decoding errors in file content by opening files in binary
    mode in order to count their lines. Text mode requires decodable content, and
    some files in Python 3.1’s library tree cannot be decoded properly on Windows.
    Catching Unicode exceptions with a try statement would avoid program exits, too,
    but might skip candidate files.

This version also adds line counts; this might add significant run time to this script too,
but it’s a useful metric to report. In fact, this version uses this value as a sort key to
report the three largest and smallest files by line counts too—this may differ from results
based upon raw file size.

Again, change this script’s trace variable if you want to track its progress through the
tree.
'''
