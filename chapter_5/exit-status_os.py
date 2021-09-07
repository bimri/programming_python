"Exit status with os.system and os.popen"
'''
[mark@linux]$ python
>>> import os
>>> pipe = os.popen('python testexit_sys.py')

>>> pipe.read()
'Bye sys world\012'
>>> stat = pipe.close() # returns exit code
>>> stat
10752
>>> hex(stat)
'0x2a00'
>>> stat >> 8 # extract status from bitmask on Unix-likes
42

>>> pipe = os.popen('python testexit_os.py')
>>> stat = pipe.close()
>>> stat, stat >> 8
(25344, 99)
'''