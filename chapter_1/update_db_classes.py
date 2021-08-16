"Step 3: Stepping Up to OOP"
'Adding Persistence'
# Notice how we still fetch, update, and 
# reassign to keys to update the shelve.

import shelve 
db = shelve.open('class-shelve') 


sue = db['sue']
sue.giveRaise(.25)
db['sue'] = sue


tom = db['tom']
tom.giveRaise(.20)
db['tom'] = tom
db.close()


'''
class instances allow us to combine both data and behavior for our
stored items. In a sense, instance attributes and class methods take the place of records
and processing programs in more traditional schemes.
'''
