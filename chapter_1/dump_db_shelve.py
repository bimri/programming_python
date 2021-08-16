# reopens the shelve and indexes it by key to fetch its stored records

import shelve
db = shelve.open('people-shelve')


for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
db.close()
