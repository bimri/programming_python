"The io.StringIO and io.BytesIO Utility Classes"
'''
The standard library tool provides an object that maps 
a file object interface to and from in-memory strings.
'''
from io import StringIO

buff = StringIO()                                       # save written text to a string
buff.write('spam\n')
buff.write('eggs\n')
buff.getvalue()                                         # get the text written so far


buff = StringIO('ham\nspam\n')                          # provide input from a string
buff.readline()
buff.readline()
buff.readline()


'python, the object interface, not the concrete datatype, is the name of the game'
from io import StringIO
import sys
buff = StringIO()

temp = sys.stdout
sys.stdout = buff
print(42, 'spam', 3.141592)                             # or print(..., file=buff)
sys.stdout = temp                                       # restore the default
buff.getvalue()                                         # or buff.getvalue()


'''
Note that there is also an io.BytesIO class with similar behavior, but which maps file
operations to an in-memory bytes buffer, instead of a str string:
'''
from io import BytesIO
stream = BytesIO()
stream.write(b'binary data')
stream.getvalue()

stream = BytesIO(b'binary data')
stream.read()
