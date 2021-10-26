"Templating with Replacements and Formats"
'''
the string replace method is often adequate by 
itself as a string templating tool

>>> val1 = 'Spam'
>>> val2 = 'shrubbery'
>>> template = template.replace('$target1', val1)
>>> template = template.replace('$target2', val2)
>>> template
'---Spam---shrubbery---'
'''


"""
string % formatting operator is also a powerful templating tool, especially
when combined with dictionaries—simply fill out a dictionary with values and apply
multiple substitutions to the HTML string all at once:
>>> template = '''
... ---
... ---%(key1)s---
... ---%(key2)s---
... '''
>>>
>>> vals = {}
>>> vals['key1'] = 'Spam'
>>> vals['key2'] = 'shrubbery'
>>> print(template % vals)
---
---Spam---
---shrubbery---
"""


'''
the string module’s Template feature is essentially a simplified
and limited variation of the dictionary-based format scheme

>>> vals
{'key2': 'shrubbery', 'key1': 'Spam'}
>>> import string
>>> template = string.Template('---$key1---$key2---')
>>> template.substitute(vals)
'---Spam---shrubbery---'
>>> template.substitute(key1='Brian', key2='Loretta')
'---Brian---Loretta---'
'''