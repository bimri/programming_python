"Step 3: Stepping Up to OOP"
'Using Classes'
'Refactoring Code'
# Augmenting methods


from person import Person


class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        """
        call back the superclass’s version of the method directly
        passing in the self argument explicitly.
        """
        Person.giveRaise(self, percent + bonus)


'''
We still redefine the method, but we simply run the general
version after adding 10 percent (by default) to the passed-in percentage. This coding
pattern can help reduce code redundancy (the original raise method’s logic appears in
only one place and so is easier to change) and is especially handy for kicking off superclass
constructor methods in practice.
'''


# Display format
class Person:
    def __str__(self):
        return '<%s => %s>' % (self.__class__.__name__, self.name)
    

'''
Here __class__ gives the lowest class from which self was made, even though
__str__ may be inherited. The net effect is that __str__ allows us to print instances
directly instead of having to print specific attributes. We could extend this __str__ to
loop through the instance’s __dict__ attribute dictionary to display all attributes generically;
'''


# Constructor customization
tom = Manager(name='Tom Doe', age=50, pay=50000, job='manager')

""" 
The reason we didn’t include a job in the example is that it’s redundant with the class
of the object: if someone is a manager, their class should imply their job title. Instead
of leaving this field blank, though, it may make more sense to provide an explicit constructor
for managers, which fills in this field automatically:
"""
class Manager(Person):
    def __init__(self, name, age, pay):
        """ 
        Now when a manager is created, its job is filled in automatically. The trick here is to
        call to the superclass’s version of the method explicitly,
        """
        Person.__init__(self, name, age, pay, 'manager')
    

