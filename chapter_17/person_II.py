"Changing Classes of Objects Stored in Shelves"

"""
a person object: fields + behavior
change: the tax method is now a computed attribute
"""

class Person:
    def __init__(self, name, job, pay=0):
        self.name = name
        self.job  = job 
        self.pay  = pay                     # real instance data
    
    def __getattr__(self, attr):            # on person.attr
        if attr == 'tax':
            return self.pay * 0.30          # computed on access
        else:
            raise AttributeError()          # other unknown names
    
    def info(self):
        return self.name, self.job, self.pay, self.tax


'''
This revision has a new tax rate (30 percent), introduces a __getattr__ qualification
overload method, and deletes the original tax method. Because this new version of the
class is re-imported when its existing instances are loaded from the shelve file, they
acquire the new behavior automatically—their tax attribute references are now intercepted
and computed when accessed:
    
    C:\...\PP4E\Dbase> python
    >>> import shelve
    >>> dbase = shelve.open('cast') # reopen shelve
    >>>
    >>> print(list(dbase.keys())) # both objects are here
    ['bob', 'emily']
    >>> print(dbase['emily'])
    <person.Person object at 0x019AEE90>
    >>>
    >>> print(dbase['bob'].tax) # no need to call tax()
    21000.0

Because the class has changed, tax is now simply qualified, not called. In addition,
because the tax rate was changed in the class, Bob pays more this time around. Of
course, this example is artificial, but when used well, this separation of classes and
persistent instances can eliminate many traditional database update programs. In most
cases, you can simply change the class, not each stored instance, for new behavior.
'''
