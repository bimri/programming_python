"Command-Line Arguments"
'''
The sys module is also where Python makes available the words typed on the command
that is used to start a Python script. These words are usually referred to as commandline
arguments and show up in sys.argv, a built-in list of strings.
'''

import sys
print(sys.argv)


'''
    C:\...\PP4E\System> python testargv.py
    ['testargv.py']

    C:\...\PP4E\System> python testargv.py spam eggs cheese
    ['testargv.py', 'spam', 'eggs', 'cheese']
    
    C:\...\PP4E\System> python testargv.py -i data.txt -o results.txt
    ['testargv.py', '-i', 'data.txt', '-o', 'results.txt']

The last command here illustrates a common convention. Much like function arguments,
command-line options are sometimes passed by position and sometimes by
name using a “-name value” word pair.    
'''


"""
Command-line arguments play the same role in programs that function arguments do
in functions: they are simply a way to pass information to a program that can vary per
program run. Because they don’t have to be hardcoded, they allow scripts to be more
generally useful.
"""
