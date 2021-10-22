"Pickle to/from flat file utilities"
import pickle

def saveDbase(filename, object):
    "save object to file"
    file = open(filename, 'wb')
    pickle.dump(object, file)               # pickle to binary file
    file.close()                            # any file-like object will do

def loadDbase(filename):
    "load object from file"
    file = open(filename, 'rb')
    object = pickle.load(file)              # unpickle from binary file
    file.close()                            # re-creates object in memory
    return object


'''
To store and fetch now, simply call these module functions; here they are in action
managing a fairly complex structure with multiple references to the same nested
object—the nested list called L at first is stored only once in the file:

C:\...\PP4E\Dbase> python
>>> from filepickle import *
>>> L = [0]
>>> D = {'x':0, 'y':L}
>>> table = {'A':L, 'B':D} # L appears twice
>>> saveDbase('myfile', table) # serialize to file

C:\...\PP4E\Dbase>python
>>> from filepickle import *
>>> table = loadDbase('myfile') # reload/unpickle
>>> table
{'A': [0], 'B': {'y': [0], 'x': 0}}
>>> table['A'][0] = 1 # change shared object
>>> saveDbase('myfile', table) # rewrite to the file

C:\...\PP4E\Dbase>python
>>> from filepickle import *
>>> print(loadDbase('myfile')) # both L's updated as expected
{'A': [1], 'B': {'y': [1], 'x': 0}}
'''


"""
Besides built-in types like the lists, tuples, and dictionaries of the examples so far, class
instances may also be pickled to file-like objects. This provides a natural way to associate
behavior with stored data (class methods process instance attributes) and provides a
simple migration path

>>> class Rec:
def __init__(self, hours):
self.hours = hours
def pay(self, rate=50):
return self.hours * rate
>>> bob = Rec(40)
>>> import pickle
>>> pickle.dump(bob, open('bobrec', 'wb'))
>>>
>>> rec = pickle.load(open('bobrec', 'rb'))
>>> rec.hours
40
>>> rec.pay()
2000
"""


'''
In general, Python can pickle just about anything, except for:
    • Compiled code objects: functions and classes record just their names and those of
    their modules in pickles, to allow for later reimport and automatic acquisition of
    changes made in module files.

    • Instances of classes that do not follow class importability rules: in short, the class
    must be importable on object loads (more on this at the end of the section “Shelve
    Files” on page 1315).
    
    • Instances of some built-in and user-defined types that are coded in C or depend
    upon transient operating system states (e.g., open file objects cannot be pickled).

A PicklingError is raised if an object cannot be pickled.
'''
