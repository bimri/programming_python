"Running Shell Commands from Scripts"
'''
The os module is also the place where we run shell commands from within Python
scripts. Two os functions allow scripts to run any command line that you can 
type in a console window:
    os.system
        Runs a shell command from a Python script
    os.popen
        Runs a shell command and connects to its input or output streams
In addition, the relatively new subprocess module provides finer-grained control over
streams of spawned shell commands and can be used as an alternative to, and even for
the implementation of, the two calls above.
'''


"What’s a shell command?"
'''
the term shell means the system that reads and runs command-line strings
on your computer, and shell command means a command-line string that you would
normally enter at your computer’s shell prompt.
'''
# ls/dir to list directories; cat to view files


"Running shell commands"
'''
    >>> import os
    >>> os.system('dir /B')
    helloshell.py
    more.py
    more.pyc
    spam.txt
    __init__.py
    0
    
    >>> os.system('type helloshell.py')
    # a Python program
    print('The Meaning of Life')
    0
    >>> os.system('type hellshell.py')
    The system cannot find the file specified.
    1
'''


""" 
The 0s at the end of the first two commands here are just the return values of the system
call itself (its exit status; zero generally means success).
"""


"Communicating with shell commands"
'''
But what if we want to grab a command’s output within a script? The os.system call
simply runs a shell command line, but os.popen also connects to the standard input or
output streams of the command; we get back a file-like object connected to the command’s
output by default (if we pass a w mode flag to popen, we connect to the command’s
input stream instead)

By using this object to read the output of a command
spawned with popen, we can intercept the text that would normally appear in the
console window where a command line is typed:
    >>> open('helloshell.py').read()
    "# a Python program\nprint('The Meaning of Life')\n"
    
    >>> text = os.popen('type helloshell.py').read()
    >>> text
    "# a Python program\nprint('The Meaning of Life')\n"
    
    >>> listing = os.popen('dir /B').readlines()
    >>> listing
    ['helloshell.py\n', 'more.py\n', 'more.pyc\n', 'spam.txt\n', '__init__.py\n']
'''


""" 
basic DOS commands; because these calls can run any command line
that we can type at a shell prompt, they can also be used to launch other Python scripts.
"""
# import os
# os.system('python more.py')                 # run a program

# output = os.popen('python more.py').read()
# print(output)


'''
In all of these examples, the command-line strings sent to system and popen are hardcoded,
but there’s no reason Python programs could not construct such strings at
runtime using normal string operations (+, %, etc.). Given that commands can be dynamically
built and run this way, system and popen turn Python scripts into flexible and
portable tools for launching and orchestrating other programs. For example, a Python
test “driver” script can be used to run programs coded in any language (e.g., C++, Java,
Python) and analyze their output.
'''
