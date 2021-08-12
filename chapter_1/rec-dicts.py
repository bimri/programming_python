"Using Dictionaries"
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}

print(bob['name'], sue['pay'])
print(bob['name'].split()[-1])

sue['pay'] *= 1.10
print(sue['pay'])
print()


'Other ways to make dictionaries'
# with keyword arguments and the type constructor
bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
print(bob)
print(sue)
print()

# dictionary keys are pseudorandomly ordered
sue = {} 
sue = {}
sue['name'] = 'Sue Jones'
sue['age'] = 45
sue['pay'] = 40000
print(sue)
print()

# zipping together name/value lists
names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 45, 40000, 'hdw']
print(list(zip(names, values)))

sue = dict(zip(names, values))
print(sue)
print()

'''
We can even make dictionaries from a sequence of key values and an optional starting
value for all the keys (handy to initialize an empty dictionary):
'''
fields = ('name', 'age', 'job', 'pay')
record = dict.fromkeys(fields, '?')
print(record)
print()


'Lists of Dictionaries'
# We can also create a list of dictionaries
print(bob)
print(sue)
print()

people = [bob, sue]                                                 # reference in a list
for person in people:
    print(person['name'], person['pay'], sep=', ')                  # all name, pay

for person in people:
    if person['name'] == 'Sue Jones':                               # fetch sue's pay
        print(person['pay'])
print()

names = [person['name'] for person in people]                       # collect names
print(names)
print()

print(list(map((lambda x: x['name']), people)))                     # ditto, generate
print(list(map((lambda x: x['pay']), people)))                      # sum all pay 
print()

# list comprehensions and on-demand generator expressions on SQL queries
print([rec['name'] for rec in people if rec['age'] >= 45])          # SQL -ish query
print(list(filter((lambda rec: rec['age'] >= 45), people)))         # filter() -ish query
print([(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people])
print()

# generator
G = (rec['name'] for rec in people if rec['age'] >= 45)
print(G)
print(next(G))

G = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
print(G.__next__())

# dictionaries are normal Python objects
for person in people:
    print(person['name'].split()[-1])                       # last name
    person['pay'] *= 1.10                                   # give each person a raise   
print()

for person in people: print(person['pay'])
