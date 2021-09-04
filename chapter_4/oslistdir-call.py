"The os.listdir call"
'''
The os module’s listdir call provides yet another way to collect filenames in a Python
list. It takes a simple directory name string, not a filename pattern, and returns a list
containing the names of all entries in that directory—both simple files and nested
directories—for use in the calling script:
'''
import os 
print(os.listdir('.'))
print(os.listdir(os.curdir))

print(os.listdir('chapter_4'))


"""
This, too, is done without resorting to shell commands and so is both fast and portable
to all major Python platforms. function); returns base
filenames without their directory path prefixes; does not include names “.” or “..” if
present; and includes names of both files and directories at the listed level.
"""


'''
To compare all three listing techniques, let’s run them here side by side on an explicit
directory. They differ in some ways but are mostly just variations on a theme for this
task—os.popen returns end-of-lines and may sort filenames on some platforms,
glob.glob accepts a pattern and returns filenames with directory prefixes, and os.list
dir takes a simple directory name and returns names without directory prefixes:

    >>> os.popen('dir /b parts').readlines()
    ['part0001\n', 'part0002\n', 'part0003\n', 'part0004\n']
    
    >>> glob.glob(r'parts\*')
    ['parts\\part0001', 'parts\\part0002', 'parts\\part0003', 'parts\\part0004']
    
    >>> os.listdir('parts')
    ['part0001', 'part0002', 'part0003', 'part0004']

Of these three, glob and listdir are generally better options if you care about script
portability and result uniformity, and listdir seems fastest in recent Python releases.
'''
 