"Step 3: Stepping Up to OOP"
'Using Classes'


class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    print(bob.name, sue.pay)

    print(bob.name.split()[-1])
    sue.pay *= 1.10
    print(sue.pay)



'''
This isn’t a database yet, but we could stuff these objects into a list or dictionary as
before in order to collect them as a unit:
    >>> from person_start import Person
    >>> bob = Person('Bob Smith', 42)
    >>> sue = Person('Sue Jones', 45, 40000)
    
    >>> people = [bob, sue] # a "database" list
    >>> for person in people:
    print(person.name, person.pay)

    >>> x = [(person.name, person.pay) for person in people]
    >>> x
    [('Bob Smith', 0), ('Sue Jones', 40000)]

    >>> [rec.name for rec in people if rec.age >= 45] # SQL-ish query
    ['Sue Jones']
    >>> [(rec.age ** 2 if rec.age >= 45 else rec.age) for rec in people]
    [42, 2025]
'''
