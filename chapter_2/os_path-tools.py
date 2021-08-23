"Common os.path Tools"
'''
The nested module os.path provides a large set of directory-related tools of its own.
For example, it includes portable functions for tasks such as checking a file’s type
(isdir, isfile, and others); testing file existence (exists); and fetching the size of a file
by name (getsize):
'''
import os

print(os.path.isdir(r'C:\Users'))
print(os.path.isfile(r'C:\Users'))
print(os.path.isdir(r'C:\config.sys'))
print(os.path.isfile(r'E:\practice\relative_path.txt'))
print(os.path.isdir('nonesuch'), os.path.isfile('nonesuch'))
print(os.path.exists(r'c:\Users\avatar'))
print(os.path.exists(r'c:\Users\Public'))
print(os.path.getsize(r'E:\practice\relative_path.txt'))


"""
We also get calls for splitting and joining directory path strings,
which automatically use the directory name conventions on the platform on which
Python is running:
"""
print(os.path.split(r'E:\practice\relative_path.txt'))
print(os.path.join('E:\\practice', 'relative_path.txt'))

name = r'E:\practice\relative_path.txt'                                     # Windows paths
print(os.path.dirname(name), os.path.basename(name))

nm = '/home/lutz/temp/data.txt'                                           # Unix-style paths
print(os.path.dirname(nm), os.path.basename(nm))

print(os.path.splitext(r'C:\PP4thEd\Examples\PP4E\PyDemos.pyw'))
print()

'''
os.path.split separates a filename from its directory path, and os.path.join puts them
back together. The dirname and basename calls here return the first and
second items returned by a split simply as a convenience, and splitext strips the file
extension (after the last .). Subtle point: it’s almost equivalent to use string split and
join method calls with the portable os.sep string, but not exactly:
'''
print(os.sep)

pathname = r'C:\PP4thEd\Examples\PP4E\PyDemos.pyw'
print(os.path.split(pathname))                                              # split file from dir

print(pathname.split(os.sep))                                               # split on every slash
print(os.sep.join(pathname.split(os.sep)))
print(os.path.join(*pathname.split(os.sep)))

'''
The last join call require individual arguments (hence the *) but doesn’t insert a first
slash because of the Windows drive syntax; use the preceding str.join method instead
if the difference matters. 

The normpath call comes in handy if your paths become a
jumble of Unix and Windows separators:
'''
print(name)
print(os.path.normpath(name))
print(os.path.normpath(r'C:\temp\\sub\.\file.ext'))


"""
This module also has an abspath call that portably returns the full directory pathname
of a file; it accounts for adding the current directory as a path prefix, .. parent syntax,
and more:
"""
print(os.chdir(r'E:\Practice'))
print(os.getcwd())

print(os.path.abspath(''))                                          # empty string means the cwd
print(os.path.abspath(r'programming_python\chapter_2'))             # partial paths relative to cwd

print(os.path.abspath('.'))                                         # relative path syntax expanded
print(os.path.abspath('..'))
print(os.path.abspath(r'..\chapter_1'))

print(os.path.abspath(r'E:\Practice'))                              # absolute paths unchanged
print(os.path.abspath(r'E:\practice\relative_path.txt'))

'''
Because filenames are relative to the current working directory when they aren’t fully
specified paths, the os.path.abspath function helps if you want to show users what
directory is truly being used to store a file.
'''
