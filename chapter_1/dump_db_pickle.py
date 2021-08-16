'''
shows how to access the pickled database after it has been created; we simply open the file
and pass its content back to pickle to remake the object from its serialized string.
'''

import pickle
dbfile = open('people-pickle', 'rb')                                    # use binary mode files in 3.X!
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])

