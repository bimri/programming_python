"Using Pickle Files"
'''
The pickle module also knows how to reconstruct
the original object in memory, given the serialized byte stream: we get back
the exact same object. In a sense, the pickle module replaces proprietary data formats
—its serialized format is general and efficient enough for any program. With pickle,
there is no need to manually translate objects to data when storing them persistently,
and no need to manually parse a complex format to get them back. Pickling is similar
in spirit to XML representations, but it’s both more Python-specific, and much simpler
to code.
'''

from initdata import db
import pickle
dbfile = open('people-pickle', 'wb')                                        # use binary mode files in 3.X!
pickle.dump(db, dbfile)                                                     # data is bytes, not str
dbfile.close()


'''
When run, this script stores the entire database (the dictionary of dictionaries defined
in initdata.py) in a pickle file. 
To a flat file named people-pickle in the current working directory. The
pickle module handles the work of converting the object to a string.
'''
