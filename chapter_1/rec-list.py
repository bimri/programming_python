"The Task"
'''
Imagine, if you will, that you need to keep track of information about people for some
reason. Maybe you want to store an address book on your computer, or perhaps you
need to keep track of employees in a small business. For whatever reason, you want to
write a program that keeps track of details about these people. In other words, you
want to keep records in a database—to permanently store lists of people’s attributes
on your computer.

Naturally, there are off-the-shelf programs for managing databases like these. By writing
a program for this task yourself, however, you’ll have complete control over its
operation. You can add code for special cases and behaviors that precoded software
may not have anticipated. You won’t have to install and learn to use yet another database
product. And you won’t be at the mercy of a software vendor to fix bugs or add
new features. You decide to write a Python program to manage your people.
'''

"""
Step 1: Representing Records
If we’re going to store records in a database, the first step is probably deciding what
those records will look like. Built-in object types such as lists and dictionaries are
often sufficient, especially if we don’t initially care about processing the data we store.
""" 

'Using Lists'
bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']

print(bob[0], sue[2])                                   # fetch name, pay
print(bob[0].split()[-1])                               # fetch last name
print(sue[2] * 0.5)                                     # fetch half pay
print(sue)
print()


'A database list'
people = [bob, sue]                                     # create a database
for person in people:                                   # loop over database
    print(person)                                       # print each record

print(people[1][0])

for person in people:
    print(person[0].split()[-1])                        # print last names
    person[2] *= 1.10                                   # give 10% raise

for person in people:
    print(person[2])                                    # print new pay


pays = [person[2] for person in people]                 # make a list of pay
print(pays)

pays = map((lambda x: x[2]), people)                    # make a list of pay
print(list(pays))

print(sum(person[2] for person in people))              # compute pay sum

people.append(['Tom', 50, 0, None])                     # add a record
print(len(people))

print(people[-1][0])
print()


'Field labels'
NAME, AGE, PAY = range(3)                               # assign field labels
bob = ['Bob Smith', 42, 30000, 'software']              # create a record
print(bob[PAY], bob[NAME])                              # field by number
print(PAY, bob[PAY])                                    # field by name


bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]

for person in people:
    print(person[0][1], person[2][1])                   # name, pay

[person[0][1] for person in people]                     # collect names

for person in people:
    print(person[0][1].split()[-1])                     # get last names
    person[2][1] *= 1.10                                # give a 10% raise

for person in people: print(person[2])


# the loop uses tuple assignment here to unpack the name/value pairs
for person in people:
    for (name, value) in person:
        if name == 'name': print(value)                 # find a specific field 

# fetcher function
def field(record, label):
    for (fname, fvalue) in record:
        if fname == label:                              # find a field by name
            return fvalue

print(field(bob, 'name'))        
print(field(sue, 'pay'))

for rec in people:
    print(field(rec, 'age'))                            # find a field by name
