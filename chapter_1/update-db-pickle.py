'''
Updating with a pickle file is similar to a manually formatted file, except that Python
is doing all of the formatting work for us.
'''

import pickle
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()


db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'


dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()

'''
Notice how the entire database is written back to the file after the records are changed
in memory, just as for the manually formatted approach; this might become slow for
very large databases.
'''
