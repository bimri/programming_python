'''
We still have a dictionary of dictionaries here, but the top-level dictionary is really a
shelve mapped onto a file. Much happens when you access a shelve’s keys—it uses
pickle internally to serialize and deserialize objects stored, and it interfaces with a
keyed-access filesystem. From your perspective, though, it’s just a persistent dictionary.
'''

from initdata import tom
import shelve


db = shelve.open('people-shelve')
sue = db['sue']                                         # fetch sue
sue['pay'] *= 1.50
db['sue'] = sue                                         # update sue
db['tom'] = tom                                         # add a new record
db.close()


'''
Notice how this code fetches sue by key, updates in memory, and then reassigns to the
key to update the shelve; this is a requirement of shelves by default, but not always of
more advanced shelve-like systems such as ZODB
'''


""" 
shelve.open also has a newer writeback keyword argument, which, if passed
True, causes all records loaded from the shelve to be cached in memory, and automatically
written back to the shelve when it is closed; this avoids manual write backs on
changes, but can consume memory and make closing slow.
""" 


'''
Also note how shelve files are explicitly closed. Although we don’t need to pass mode
flags to shelve.open (by default it creates the shelve if needed, and opens it for reads
and writes otherwise), some underlying keyed-access filesystems may require a close
call in order to flush output buffers after changes.
'''
