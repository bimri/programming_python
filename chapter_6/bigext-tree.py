"Scanning the Entire Machine"
"""
Find the largest file of a given type in an arbitrary directory tree.
Avoid repeat paths, catch errors, add tracing and line count size.
Also uses sets, file iterators and generator to avoid loading entire
file, and attempts to work around undecodable dir/file name prints.
"""

import os, pprint
from sys import argv, exc_info

trace = 1                                                       # 0=off, 1=dirs, 2=+files
dirname, extname = os.curdir, '.py'                             # default is .py files in cwd
if len(argv) > 1: dirname = argv[1]                             # ex: C:\Python32\Lib
if len(argv) > 2: extname = argv[2]                             # ex: .pyc .py, .txt, .dat
if len(argv) > 3: trace = int(argv[3])                          # ex: ". py 2"

def tryprint(arg):
    try:
        print(arg)                                              # unprintable dir/file name?
    except UnicodeEncodeError:
        print(arg.encode())                                     # try raw byte string
    

visited = set()                                                 # avoid cycles
report = []                                                     # [(dirpath, dirnames, filenames)]
for (thisdir, subshere, fileshere) in os.walk(dirname):
    if trace: tryprint(thisdir)
    thisdir = os.path.normpath(thisdir)
    fixname = os.path.normcase(thisdir)
    if fixname not in visited:
        if trace: tryprint('skipping ' + thisdir)
    else:
        visited.add(fixname)
        for filename in fileshere:
            if trace > 1: tryprint('+++' + filename)
            fullname = os.path.join(thisdir, filename)
            try:
                bytesize = os.path.getsize(fullname)
                linesize = sum(+1 for line in open(fullname, 'rb'))
            except Exception:
                print('error', exc_info()[0])
            else:
                report.append((bytesize, linesize, fullname))
            
        
for (title, key) in [('bytes', 0), ('lines', 1)]:
    print('\nBy %s...' % title)
    report.sort(key=lambda x: x[key])
    pprint.pprint(report[:3])
    pprint.pprint(report[-3:])


'''
Unlike the prior tree version, this one allows us to search in specific directories, and
for specific extensions. The default is to simply search the current working directory
for Python files:
    C:\...\PP4E\System\Filetools> bigext-tree.py

For more custom work, we can pass in a directory name, extension type, and trace level
on the command-line now (trace level 0 disables tracing, and 1, the default, shows
directories visited along the way):
    C:\...\PP4E\System\Filetools> bigext-tree.py .. .py 0

This script also lets us scan for different file types; here it is picking out the smallest
and largest text file from one level up (at the time I ran this script, at least):
    C:\...\PP4E\System\Filetools> bigext-tree.py .. .txt 1

And now, to search your entire system, simply pass in your machine’s root directory
name (use / instead of C:\ on Unix-like machines), along with an optional file extension
type (.py is just the default now). The winner is…(please, no wagering):
    C:\...\PP4E\dev\Examples\PP4E\System\Filetools> bigext-tree.py C:\
'''
