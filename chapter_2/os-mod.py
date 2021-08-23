"Introducing the os Module"
'''
os is the larger of the two core system modules. It contains all of the
usual operating-system calls you use in C programs and shell scripts. Its calls deal with
directories, processes, shell variables, and the like.

Technically, this module provides
POSIX tools—a portable standard for operating-system calls—along with platformindependent
directory processing tools as the nested module os.path.
'''

""" 
os serves as a largely portable interface to your computer’s system calls: scripts written
with os and os.path can usually be run unchanged on any platform.
""" 
import os 

print(dir(os))

'''
Besides all of these, the nested os.path module exports even more tools, most of which
are related to processing file and directory names portably:
'''
print(dir(os.path))


"Administrative Tools"
x = os.getpid()
print(x)

x = os.getcwd()
print(x)

x = os.chdir(r'E:/practice/programming_python/chapter_2')
print(os.getcwd())
x = os.chdir(r'E:/practice/programming_python')
print(os.getcwd())                                                  # changed back to current working directory

'''
os.getpid function gives the calling process’s process ID (a unique
system-defined identifier for a running program, useful for process control and unique
name creation), and os.getcwd returns the current working directory. The current
working directory is where files opened by your script are assumed to live, unless their
names include explicit directory paths.
'''

"""
os.chdir function to change to a new directory; your code
will run relative to the new directory for the rest of the program
"""


"Portability Constants"
'''
The os module also exports a set of names designed to make cross-platform programming
simpler. The set includes platform-specific settings for path and directory separator
characters, parent and current directory indicators, and the characters used to
terminate lines on the underlying computer.
'''
print(
    os.pathsep + "\n",
    os.sep + "\n",
    os.pardir + "\n",
    os.curdir + "\n",
    os.linesep
)

'''
os.sep is whatever character is used to separate directory components on the platform
on which Python is running; it is automatically preset to \ on Windows, / for POSIX
machines, and : on some Macs. Similarly, os.pathsep provides the character that separates
directories on directory lists, : for POSIX and ; for DOS and Windows.

By using such attributes when composing and decomposing system-related strings in
our scripts, we make the scripts fully portable.

For instance, a call of the form dir
path.split(os.sep) will correctly split platform-specific directory names into components,
though dirpath may look like dir\dir on Windows, dir/dir on Linux, and
dir:dir on some Macs. As mentioned, on Windows you can usually use forward slashes
rather than backward slashes when giving filenames to be opened, but these portability
constants allow scripts to be platform neutral in directory processing code.
'''

"""
Notice also how os.linesep comes back as \r\n here—the symbolic escape code which
reflects the carriage-return + line-feed line terminator convention on Windows, which
you don’t normally notice when processing text files in Python.
"""
 