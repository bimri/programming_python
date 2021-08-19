"Paging Documentation Strings"
# The __doc__ built-in attribute just shown usually contains a string of documentation

import sys
# print(sys.__doc__)


'''
The print built-in function, unlike interactive displays, interprets end-line characters
correctly. Unfortunately, print doesn’t, by itself, do anything about scrolling or paging
and so can still be unwieldy on some platforms. Tools such as the built-in help function
can do better:
'''
print(help(sys))


""" 
The help function is one interface provided by the PyDoc system—standard library
code that ships with Python and renders documentation (documentation strings, as
well as structural details) related to an object in a formatted way.
"""
