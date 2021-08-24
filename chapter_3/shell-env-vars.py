"Shell Environment Variables"
'''
Shell variables, sometimes known as environment variables, are made available to Python
scripts as os.environ, a Python dictionary-like object with one entry per variable
setting in the shell. Shell variables live outside the Python system; they are often set at
your system prompt or within startup files or control-panel GUIs and typically serve
as system-wide configuration inputs to programs.

In fact, by now you should be familiar with a prime example: the PYTHONPATH module
search path setting is a shell variable used by Python to import modules. By setting it
once in your operating system, its value is available every time a Python program is run.
Shell variables can also be set by programs to serve as inputs to other programs in an
application; because their values are normally inherited by spawned programs, they
can be used as a simple form of interprocess communication.
'''

"Fetching Shell Variables"
'''
In Python, the surrounding shell environment becomes a simple preset object, not special
syntax. Indexing os.environ by the desired shell variable’s name string (e.g.,
os.environ['USER']) is the moral equivalent of adding a dollar sign before a variable
name in most Unix shells (e.g., $USER), using surrounding percent signs on DOS
(%USER%), and calling getenv("USER") in a C program.
'''

import os 

print(os.environ.keys())
print(list(os.environ.keys()))
print(os.environ['TEMP']); print()

# print(os.environ['PYTHONPATH'])
# for srcdir in os.environ['PYTHONPATH'].split(os.pathsep):
#     print(srcdir)

import sys
print(sys.path[:3]); print()

'''
As usual, sys.path is the actual search path at runtime, and reflects the
result of merging in the PYTHONPATH setting after the current directory.
'''


"Changing Shell Variables"
'''
Like normal dictionaries, the os.environ object supports both key indexing and
assignment. As for dictionaries, assignments change the value of the key:
'''
print(os.environ['TEMP'])
# os.environ['TEMP'] = r'c:\temp'
# print(os.environ['TEMP'])

"""
But something extra happens here. In all recent Python releases, values assigned to
os.environ keys in this fashion are automatically exported to other parts of the application.
That is, key assignments change both the os.environ object in the Python program
as well as the associated variable in the enclosing shell environment of the running
program’s process.
"""
