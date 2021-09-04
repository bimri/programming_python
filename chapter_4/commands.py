#!/usr/local/bin/python3
from sys import argv
from scanfile import scanner
class UnknownCommand(Exception): pass


def processLine(line):                              # define a function
    if line[0] == '*':                              # applied to each line
        print("Ms.", line[1:-1])
    elif line[0] == '+':
        print("Mr.", line[1:-1])                    # strip first and last char: \n
    else:
        raise UnknownCommand(line)                  # raise exception for unknown command


filename = 'cdata.txt'
if len(argv) == 2: filename = argv[1]               # allow filename cmd arg
scanner(filename, processLine)                      # start the scanner

# C:\...\PP4E\System\Filetools> python commands.py hillbillies.txt


"alternative function - for the command processor"
commands = {'*': 'Ms.', '+': 'Mr.'}                 # data is easier to expand than code?


def processLine(line):
    try:
        print(commands[line[0]], line[1:-1])
    except KeyError:
        raise UnknownCommand(line)


'''
As a rule of thumb, we can also usually speed
things up by shifting processing from Python code to built-in tools.

we can probably make our file scanner faster by using the
file’s line iterator to step through the file instead of the manual readline loop
'''
def scanner(name, function):
    for line in open(name, 'r'):                        # scan line by line
        function(line)                                  # call a function object


# minimalist’s versions
def scanner(name, function):
    list(map(function, open(name, 'r')))                # map a function to a sequence

def scanner(name, function):
    [function(line) for line in open(name, 'r')]        # list comprehension

def scanner(name, function):
    [function(line) for line in open(name, 'r')]        # generator expression
