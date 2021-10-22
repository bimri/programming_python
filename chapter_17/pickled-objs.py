"Pickled Objects"
'''
It’s a sort of super general data formatting and de-formatting
tool—pickle converts nearly arbitrary Python in-memory objects to and from a single
linear string format, suitable for storing in flat files, shipping across network sockets
between trusted sources

This conversion from object to string is often
called serialization—arbitrary data structures in memory are mapped to a serial string
form.
'''

"""
The string representation used for objects is also sometimes referred to as a byte stream,
due to its linear format. It retains all the content and references structure of the original
in-memory object. When the object is later re-created from its byte string, it will be a
new in-memory object identical in structure and value to the original, though located
at a different memory address.
"""

'''
Pickling works on almost any Python datatype—numbers, lists, dictionaries, class instances,
nested structures, and more—and so is a general way to store data. Because
pickles contain native Python objects, there is almost no database API to be found; the
objects stored with pickling are processed with normal Python syntax when they are
later retrieved.
'''


"Using Object Pickling"
'''
For example, to pickle an object into
a serialized string, we can either make a pickler and call its methods or use convenience
functions in the module to achieve the same effect:
    P = pickle.Pickler(file)
    Make a new pickler for pickling to an open output file object file.
    
    P.dump(object )
    Write an object onto the pickler’s file/stream.
    
    pickle.dump(object, file)
    Same as the last two calls combined: pickle an object onto an open file.
    
    string = pickle.dumps(object)
    Return the pickled representation of object as a character string.
'''

"""
Unpickling from a serialized string back to the original object is similar—both object
and convenience function interfaces are available:
    U = pickle.Unpickler(file)
    Make an unpickler for unpickling from an open input file object file.
    
    object = U.load()
    Read an object from the unpickler’s file/stream.
    
    object = pickle.load(file)
    Same as the last two calls combined: unpickle an object from an open file.
    
    object = pickle.loads(string)
    Read an object from a character string rather than a file.
"""


"Pickling in Action"
table = {'a': [1, 2, 3],
        'b': ['spam', 'eggs'],
        'c': {'name':'bob'}}

import pickle

mydb = open('dbase', 'wb')
pickle.dump(table, mydb)


# to unpickle later
'''
The object you get back from unpickling has the same value and reference structure as
the original, but it is located at a different address in memory. This is true whether the
object is unpickled in the same or a future process. Again, the unpickled object is ==
but is not is:
    C:\...\PP4E\Dbase> python
    >>> import pickle
    >>> f = open('temp', 'wb')
    >>> x = ['Hello', ('pickle', 'world')] # list with nested tuple
    >>> pickle.dump(x, f)
    >>> f.close() # close to flush changes
    >>>
    >>> f = open('temp', 'rb')
    >>> y = pickle.load(f)
    >>> y
    ['Hello', ('pickle', 'world')]
    >>>
    >>> x == y, x is y # same value, diff objects
    (True, False)
'''
mydb = open('dbase', 'rb')
table = pickle.load(mydb)
print(table)

