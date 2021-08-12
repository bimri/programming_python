"Nested structures"

bob2 = {'name': {'first': 'Bob', 'last': 'Smith'},
    'age': 42,
    'job': ['software', 'writing'],
    'pay': (40000, 50000)} 


print(bob2['name'])
print(bob2['name']['last'])
print(bob2['job'])
print(bob2['pay'])
print(bob2['pay'][1])
print()


for job in bob2['job']: print(job)                              # all of bob's jobs
for pay in bob2['pay']: print(pay)                              # all of bob's pay
print()

print(bob2['job'][-1])                                          # last job
print(bob2['pay'][-1])                                          # last pay
print()

bob2['job'].append('janitor')
print(bob2)
print()
