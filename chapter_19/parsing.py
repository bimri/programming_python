"Parsing with Splits and Joins"
'''
Python’s built-in tools for splitting and joining
strings around tokens turn out to be especially useful when it comes to parsing text:

    str.split(delimiter?, maxsplits?)
        Splits a string into a list of substrings, using either whitespace (tabs, spaces, newlines)
        or an explicitly passed string as a delimiter. maxsplits limits the number of
        splits performed, if passed.
    delimiter.join(iterable)
        Concatenates a sequence or other iterable of substrings (e.g., list, tuple, generator),
        adding the subject separator string between each.

>>> 'A B C D'.split()
['A', 'B', 'C', 'D']
>>> 'A+B+C+D'.split('+')
['A', 'B', 'C', 'D']
>>> '--'.join(['a', 'b', 'c'])
'a--b--c'        
'''

"""
Despite their simplicity, they can handle surprisingly complex text-parsing tasks.
Moreover, string method calls are very fast because they are implemented in C language
code. For instance, to quickly replace all tabs in a file with four periods, pipe the file
into a script that looks like this:
    from sys import *
    stdout.write(('.' * 4).join(stdin.read().split('\t')))
"""
