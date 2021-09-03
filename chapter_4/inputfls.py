"Input files"
'''
Input text files are opened with either a mode
flag of r (for “read”) or no mode flag at all—it defaults to r if omitted, and it commonly
is. Once opened, we can read the lines of a text file with the readlines method:
'''
#!/usr/bin/env python3
# Path: chapter_4\inputfls.py

file = open('mydata.txt', 'r')              # 'r' is the default mode
lines = file.readlines()                    # readlines reads the individual lines into a list
for line in lines:                          # iterate through the lines
    print(line, end='')                     # line have a newline character to end('\n')


'''
The readlines method loads the entire contents of the file into memory and gives it to
our scripts as a list of line strings that we can step through in a loop. In fact, there are
many ways to read an input file:
    file.read()
        Returns a string containing all the characters (or bytes) stored in the file
    file.read(N)
        Returns a string containing the next N characters (or bytes) from the file
    file.readline()
        Reads through the next \n and returns a line string
    file.readlines()
        Reads the entire file and returns a list of line strings

>>> file.seek(0) # go back to the front of file
>>> file.read() # read entire file into string
'Hello file world!\nBye file world.\n'

>>> file.seek(0) # read entire file into lines list
>>> file.readlines()
['Hello file world!\n', 'Bye file world.\n']

>>> file.seek(0)
>>> file.readline() # read one line at a time
'Hello file world!\n'
>>> file.readline()
'Bye file world.\n'
>>> file.readline() # empty string at end-of-file
''

>>> file.seek(0) # read N (or remaining) chars/bytes
>>> file.read(1), file.read(8) # empty string at end-of-file
('H', 'ello fil')        

The seek(0) call used repeatedly here means “go back to the start of the file.”
(it is an alternative to reopening the file each time). The seek call simply lets us move to a new position
for the next transfer operation.
'''


"""
Here are a few rules of thumb about which to choose:
    • read() and readlines() load the entire file into memory all at once. That makes
    them handy for grabbing a file’s contents with as little code as possible. It also
    makes them generally fast, but costly in terms of memory for huge files—loading
    a multigigabyte file into memory is not generally a good thing to do (and might not
    be possible at all on a given computer).

    • On the other hand, because the readline() and read(N) calls fetch just part of the
    file (the next line or N-character-or-byte block), they are safer for potentially big
    files but a bit less convenient and sometimes slower. Both return an empty string
    when they reach end-of-file. If speed matters and your files aren’t huge, read or
    readlines may be a generally better choice.
"""


"Reading lines with file iterators"
file = open('mydata.txt')
for line in file:                                   # no need to call readlines()
    print(line, end='')                             # iterator reads next line each time
 
'''
Better still, you can open the file in the loop statement itself, as a temporary which will
be automatically closed on garbage collection when the loop ends (that’s normally the
file’s sole reference):

Moreover, this file line-iterator form does not load the entire file into a line’s list all at
once, so it will be more space efficient for large text files. Because of that, this is the
prescribed way to read line by line today.
'''
for line in open('mydata.txt'):                     # even shorter: temporary file object
    print(line, end='')                             # auto-closes file when garbage collected



'''
Interestingly, iterators are automatically used in all iteration contexts, including the
list constructor call, list comprehension expressions, map calls, and in membership
checks:
    >>> open('data.txt').readlines()                            # always read lines
    ['Hello file world!\n', 'Bye file world.\n']
    
    >>> list(open('data.txt'))                                  # force line iteration
    ['Hello file world!\n', 'Bye file world.\n']
    
    >>> lines = [line.rstrip() for line in open('data.txt')]    # comprehension
    >>> lines
    ['Hello file world!', 'Bye file world.']
    
    >>> lines = [line.upper() for line in open('data.txt')]     # arbitrary actions
    >>> lines
    ['HELLO FILE WORLD!\n', 'BYE FILE WORLD.\n']
    
    >>> list(map(str.split, open('data.txt')))                  # apply a function
    [['Hello', 'file', 'world!'], ['Bye', 'file', 'world.']]
    
    >>> line = 'Hello file world!\n'
    >>> line in open('data.txt')                                # line membership
    True

Iterators may seem somewhat implicit at first glance, but they’re representative of the
many ways that Python makes developers’ lives easier over time.
'''


"Other open options"
'''
a mode string, meaning "append". 
In this output mode, write methods add data to the end of the file,
and the open call will not erase the current contents of the file:
'''
file = open('mydata.txt', 'a')                          # open in append mode: doesn't erase
file.write('The Life of Brian\n')                       # added at end of existing data
file.write('Bye Brian world.\n')
file.close()

print(open('mydata.txt').read())                       # open and read entire file
