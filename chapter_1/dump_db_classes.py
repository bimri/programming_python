"Step 3: Stepping Up to OOP"
'Adding Persistence'
# reads the shelve and prints fields of its records


import shelve
db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n ', db[key].name, db[key].pay)


bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())


'''
Note that we don’t need to reimport the Person class here in order to fetch its instances
from the shelve or run their methods. When instances are shelved or pickled, the underlying
pickling system records both instance attributes and enough information to
locate their classes automatically when they are later fetched (the class’s module simply
has to be on the module search path when an instance is loaded).
'''

""" 
This is on purpose;
because the class and its instances in the shelve are stored separately, you can change
the class to modify the way stored instances are interpreted when loaded
""" 
