"Using DBM Files"
'''
Although DBM filesystems have to do a bit of work to map chunks of stored data to
keys for fast retrieval (technically, they generally use a technique called hashing to store
data in files), your scripts don’t need to care about the action going on behind the
scenes. In fact, DBM is one of the easiest ways to save information in Python—DBM
files behave so much like in-memory dictionaries that you may forget you’re actually
dealing with a file at all. For instance, given a DBM file object:
    • Indexing by key fetches data from the file.
    • Assigning to an index stores data in the file.

DBM file objects also support common dictionary methods such as keys-list fetches
and tests and key deletions.
'''

import dbm

file = dbm.open('movie', 'c')                       # get interface: bsddb, gnu, ndbm, dumb
file['Batman'] = 'Pow'                              # store a string under key 'Batman'
file.keys()                                         # get the file's key directory
file['Batman']                                      # fetch value for key 'Batman'

who = ['Robin', 'Cat-woman', 'Joker']
what = ['Bang!', 'Splat!', 'Wham!']
for i in range(len(who)):
    file[who[i]] = what[i]                          # add 3 more "records"

file.keys()     
len(file), 'Robin' in file, file['Joker']
file.close()                                        # close sometimes required


'''
Notice how DBM files return a real list for the keys call; not shown here, their values
method instead returns an iterable view like dictionaries. Further, DBM files always
store both keys and values as bytes objects; interpretation as arbitrary types of Unicode
text is left to the client application. We can use either bytes or str strings in our code
when accessing or storing keys and values—using bytes allows your keys and values
to retain arbitrary Unicode encodings, but str objects in our code will be encoded to
bytes internally using the UTF-8 Unicode encoding by Python’s DBM implementation.
'''


"""
Still, we can always decode to Unicode str strings to display in a more friendly fashion
if desired, and DBM files have a keys iterator just like dictionaries. Moreover, assigning
and deleting keys updates the DBM file, and we should close after making changes (this
ensure that changes are flushed to disk):
    >>> for key in file: print(key.decode(), file[key].decode())
    ...
    Cat-woman Splat!
    Batman Pow!
    Joker Wham!

    >>> file['Batman'] = 'Ka-Boom!' # change Batman slot
    >>> del file['Robin'] # delete the Robin entry
    >>> file.close() # close it after changes
"""


'''
Apart from having to import the interface and open and close the DBM file, Python
programs don’t have to know anything about DBM itself.

DBM files look like normal Python dictionaries, stored on external files. Changes made to them
are retained indefinitely:
    C:\...\PP4E\Dbase> python
    >>> import dbm # open DBM file again
    >>> file = dbm.open('movie', 'c')
    >>> for key in file: print(key.decode(), file[key].decode())
    ...
    Cat-woman Splat!
    Batman Ka-Boom!
    Joker Wham!
'''
