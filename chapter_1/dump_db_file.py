"Utility scripts"
# reloads the database from a file each time it is run

from make_db_file import loadDbase
db = loadDbase()
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])


'''
The main point to notice
is that the data stays around after each script exits—our objects have become persistent
simply because they are mapped to and from text files:
'''
