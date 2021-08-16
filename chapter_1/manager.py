"Step 3: Stepping Up to OOP"
'Using Classes'
'Adding Inheritance'
'''
One last enhancement to our records before they become permanent: because they are
implemented as classes now, they naturally support customization through the inheritance
search mechanism in Python.
'''
from person import Person


class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        self.pay *= (1.0 + percent + bonus)



if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)



""" 
    >>> from person import Person
    >>> from manager import Manager
    
    >>> bob = Person(name='Bob Smith', age=42, pay=10000)
    >>> sue = Person(name='Sue Jones', age=45, pay=20000)
    >>> tom = Manager(name='Tom Doe', age=55, pay=30000)
    >>> db = [bob, sue, tom]

    >>> for obj in db:
            obj.giveRaise(.10) # default or custom
    
    >>> for obj in db:
            print(obj.lastName(), '=>', obj.pay)
""" 
