"Step 2: Storing Records Persistently"
'Using Formatted Files'
'''
One way to keep our data around between program runs is to write all the data out to
a simple text file, in a formatted way. Provided the saving and loading tools agree on
the format selected, we’re free to use any custom scheme we like.
'''
# initialize data to be stored in files, pickles, shelves

# records
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}


# database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom


if __name__ == '__main__':                                              # when run as a script
    for key in db:
        print(key, '=>\n ', db[key])
