"The Module Search Path"
'''
The sys module also lets us inspect the module search path both interactively and
within a Python program.

sys.path is a list of directory name strings representing the
true search path in a running Python interpreter. When a module is imported, Python
scans this list from left to right, searching for the module’s file on each directory named
in the list.
'''


""" 
The sys.path list is simply initialized from your PYTHONPATH setting—the content of
any .pth path files located in Python’s directories on your machine plus system
defaults -- when the interpreter is first started up.
""" 
import sys 
print(sys.path)


"""
Surprisingly, sys.path can actually be changed by a program, too. A script can use list
operations such as append, extend, insert, pop, and remove, as well as the del statement
to configure the search path at runtime to include all the source directories to which it
needs access. Python always uses the current sys.path setting to import, no matter what
you’ve changed it to:
"""
sys.path.append(r'E:\practice')
print(sys.path)


'''
Changing sys.path directly like this is an alternative to setting your PYTHONPATH shell
variable, but not a very permanent one. Changes to sys.path are retained only until the
Python process ends, and they must be remade every time you start a new Python
program or session.

However, some types of programs (e.g., scripts that run on a web
server) may not be able to depend on PYTHONPATH settings; such scripts can instead
configure sys.path on startup to include all the directories from which they will need
to import modules
'''


# Windows Directory Paths
# use raw string constants to retain backslashes literally (e.g., r"C:\dir").
'''
Also note that most Python library calls accept either forward (/) or backward (\)
slashes as directory path separators, regardless of the underlying platform. That is, /
usually works on Windows too and aids in making scripts portable to Unix.
'''
