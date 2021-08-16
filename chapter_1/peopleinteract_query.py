"Step 4: Adding Console Interaction"
'A Console Shelve Interface'
# allow users to type keys and values in a console window in order to process the database


# interactive queries
import shelve
fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)
db = shelve.open('class-shelve')


while True:
    key = input('\nKey? => ')                                       # key or empty line, exc at eof
    if not key: break
    try:
        record = db[key]                                            # fetch by key, show in console
    except:
        print('No such key "%s"!' % key)
    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record, field))
db.close()

'''
This script uses the getattr built-in function to fetch an object’s attribute when given
its name string, and the ljust left-justify method of strings to align outputs (max
field, derived from a generator expression, is the length of the longest field name).
'''
