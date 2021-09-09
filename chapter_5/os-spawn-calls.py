"Other Ways to Start Programs" 
'The os.spawn Calls'
'''
In recent versions of Python, the portable subprocess module has started to supersede
these calls. In fact, Python’s library manual includes a note stating that this module has
more powerful and equivalent tools and should be preferred to os.spawn calls. Moreover,
the newer multiprocessing module can achieve similarly portable results today
when combined with os.exec calls, as we saw earlier. Still, the os.spawn calls continue
to work as advertised and may appear in Python code you encounter.

C:\...\PP4E\System\Processes> python
>>> print(open('makewords.py').read())
print('spam')
print('eggs')
print('ham')

>>> import os
>>> os.system('python makewords.py')
spam
eggs
ham

>>> result = os.popen('python makewords.py').read()
>>> print(result)
spam
eggs
ham

The equivalent os.spawn calls achieve the same effect, with a slightly more complex call
signature that provides more control over the way the program is launched:
>>> os.spawnv(os.P_WAIT, r'C:\Python31\python', ('python', 'makewords.py'))
spam
eggs
ham
0
>>> os.spawnl(os.P_NOWAIT, r'C:\Python31\python', 'python', 'makewords.py')
1820
>>> spam
eggs
ham

The spawn calls are also much like forking programs in Unix. They don’t actually copy
the calling process (so shared descriptor operations won’t work), but they can be used
to start a program running completely independent of the calling program,
'''
