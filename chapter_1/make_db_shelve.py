"Storing Records Persistently"
'Using Shelves'
""" 
pickling one record per file also obviates the need to load and store the entire database for each
update. If we really want keyed access to records, though, the Python standard library
offers an even higher-level tool: shelves.
""" 

'''
Shelves automatically pickle objects to and from a keyed-access filesystem. They behave
much like dictionaries that must be opened, and they persist after each program exits.
Because they give us key-based access to stored records, there is no need to manually
manage one flat file per record—the shelve system automatically splits up stored records
and fetches and updates only those records that are accessed and changed. In
this way, shelves provide utility similar to per-record pickle files, but they are usually
easier to code.
'''
from initdata import bob, sue 
import shelve


db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()


'''
This script creates one or more files in the current directory with the name peopleshelve
as a prefix (in Python 3.1 on Windows, people-shelve.bak, people-shelve.dat, and
people-shelve.dir). You shouldn’t delete these files (they are your database!), and you
should be sure to use the same base name in other scripts that access the shelve.
'''
