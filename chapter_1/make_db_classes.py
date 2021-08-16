"Step 3: Stepping Up to OOP"
'Adding Persistence'


import shelve
from person import Person
from manager import Manager


bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)


db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()


'''
This file creates three class instances (two from the original class and one from its
customization) and assigns them to keys in a newly created shelve file to store them
permanently.
'''
