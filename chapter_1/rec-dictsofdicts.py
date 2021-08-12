"Dictionaries of dictionaries"
'''
we can use a dictionary
of dictionaries—the outer dictionary is the database, and the nested dictionaries are
the records within it. Rather than a simple list of records, a dictionary-based database
allows us to store and retrieve records by symbolic key:
'''
bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
print(bob) 

db = {}
db['bob'] = bob                                                 # reference in a dict of dicts
db['sue'] = sue

print(db['bob']['name'])                                        # fetch bob's name


db['sue']['pay'] = 50000                                        # change sue's pay
print(db['sue']['pay'])                                         # fetch sue's pay
print(); print(db)


import pprint
pprint.pprint(db)
print()

# keys result is a generator 
for key in db:
    print(key, '=>', db[key]['name'])

for key in db:
    print(key, '=>', db[key]['pay'])
print() 

# To visit all records, either index by key as you go:
for key in db:
    print(db[key]['name'].split()[-1])
    db[key]['pay'] *= 1.10
print() 

# or step through the dictionary’s values to access records directly:
for record in db.values(): print(record['pay'])

x = [db[key]['name'] for key in db]
print(x)

x = [rec['name'] for rec in db.values()]
print(x); print()

# to add a new record, simply assign it to a new key
db['tom'] = dict(name='Tom', age=50, job=None, pay=0)
print(db['tom'])
print(db['tom']['name'])
print(list(db.keys()))
print(len(db))
print([rec['age'] for rec in db.values()])
print([rec['name'] for rec in db.values() if rec['age'] >= 45])             # SQL-ish query
