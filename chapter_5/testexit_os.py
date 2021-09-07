def outahere():
    import os
    print('Bye os world')
    os._exit(99)
    print('Never reached')


if __name__ == '__main__':
    outahere()


'''
Unlike sys.exit, os._exit is immune to both try/except and try/finally interception:
C:\...\PP4E\System\Exits> python testexit_os.py
Bye os world
C:\...\PP4E\System\Exits> python

>>> from testexit_os import outahere
>>> try:
...     outahere()
... except:
...     print('Ignored')
...
Bye os world # exits interactive process
C:\...\PP4E\System\Exits> python

>>> from testexit_os import outahere
>>> try:
...     outahere()
... finally:
...     print('Cleanup')
...
Bye os world # ditto
'''
