"Storing Class Instances in Shelves"
'''
a person object: fields + behavior
change: the tax method is now a computed attribute
'''

class Person:
    def __init__(self, name, job, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay                  # real instance data

    def __getattr__(self, attr):         # on person.attr
        if attr == 'tax':
            return self.pay * 0.30       # computed on access
        else:
            raise AttributeError()       # other unknown names

    def info(self):
        return self.name, self.job, self.pay, self.tax


'''
Notice that calling Bob’s tax method works even though we didn’t import the Person
class in this last session. Python is smart enough to link this object back to its original
class when unpickled, such that all the original methods are available through fetched
objects.
'''
