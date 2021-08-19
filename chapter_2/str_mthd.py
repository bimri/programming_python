"String Method Basics"
'''
Python string methods are not a system-related tool per se,
but they see action in most Python programs. String methods 
include calls for searching and replacing:
'''
mystr = 'xxxSPAMxxx'
x = mystr.find('SPAM')                          # return first offset
print(x)

mystr = 'xxaaxxaa'
x = mystr.replace('aa', 'SPAM')                 # global replacement
print(x)


'''
The find call returns the offset of the first occurrence of a substring, and replace does
global search and replacement. Like all string operations, replace returns a new string
instead of changing its subject in-place (recall that strings are immutable).
'''


""" 
In more recent Pythons, the in membership operator can often be used as an alternative
to find if all we need is a yes/no answer (it tests for a substring’s presence).
"""
mystr = 'xxxSPAMxxx'
print('SPAM' in mystr)                          # substring search/test

print('Ni' in mystr)                            # when not found
print(mystr.find('Ni'))


mystr = '\t Ni\n'
print(mystr.strip())                            # remove whitespace

print(mystr.rstrip())                           # same, but just on right side
print()


'''
String methods also provide functions that are useful for things such as case conversions,
and a standard library module named string defines some useful preset variables,
among other things:
'''
mystr = 'SHRUBBERY'
print(mystr.lower())                            # case converters

print(mystr.isalpha())                          # content tests
print(mystr.isdigit())
print()


import string                                   # case presets: for 'in', etc.
print(string.ascii_lowercase)
print(string.whitespace)                        # whitespace characters
print()


'''
There are also methods for splitting up strings around a substring delimiter and putting
them back together with a substring in between.
'''
mystr = 'aaa,bbb,ccc'
print(mystr.split(','))                         # split into substrings list

mystr = 'a b\nc\nd'
print(mystr.split())                            # default delimiter: whitespace

delim = 'NI'
print(delim.join(['aaa', 'bbb', 'ccc']))        # join substrings list

print(' '.join(['A', 'dead', 'parrot']))        # add a space between

chars = list('Lorreta')                         # convert to characters list
print(chars)
chars.append('!`')
print(''.join(chars))                           # to string: empty delimiter


# str.replace, the hard way!
mystr = 'xxaaxxaa'
print('SPAM'.join(mystr.split('aa')))


'''
For future reference, also keep in mind that Python doesn’t automatically convert
strings to numbers, or vice versa; if you want to use one as you would use the other,
you must say so with manual conversions:
'''
print(int("42"), eval("42"))                    # string to int conversions
print(str(42), repr(42))                        # int to string conversions
print(("%d" % 42), '{:d}'.format(42))           # via formatting expression, method
print("42" + str(1), int("42") + 1)             # concatenation, addition


'''
Python doesn’t assume you meant one or the other and convert automatically;
as a rule of thumb, Python tries to avoid magic—and the temptation to guess—
whenever possible.
'''
