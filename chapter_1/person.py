"Step 3: Stepping Up to OOP"
'Using Classes'
'Adding Behavior'
'''
By wrapping up bits of behavior in class method functions,
we can insulate clients from changes. And by packaging methods in classes along with
data, we provide a natural place for readers to look for code. In a sense, classes combine
records and the programs that process those records; methods provide logic that interprets
and updates the data (we say they are object-oriented, because they always
process an object’s data).
'''


class Person:
    def __init__(self, name, age, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        self.age = age
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 'software', 30000)
    sue = Person('Sue Jones', 45, 'hardware', 40000)
    print(bob.name, sue.pay)

    print(bob.lastName())
    sue.giveRaise(.10)
    print(sue.pay)
