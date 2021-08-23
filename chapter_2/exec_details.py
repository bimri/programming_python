"Exception Details"
'''
Other attributes in the sys module allow us to fetch all the information related to the
most recently raised Python exception. This is handy if we want to process exceptions
in a more generic fashion.

For instance, the sys.exc_info function returns a tuple with
the latest exception’s type, value, and traceback object.
'''
import sys 

try:
    raise IndexError
except:
    print(sys.exc_info())


"""
We might use such information to format our own error message to display in a GUI
pop-up window or HTML web page (recall that by default, uncaught exceptions terminate
programs with a Python error display).
""" 
import traceback, sys 

def grail(x):
    raise TypeError('already got one')

try:
    grail('arthur')
except:
    exc_info = sys.exc_info()
    print(exc_info[0])
    print(exc_info[1])
    traceback.print_tb(exc_info[2])


'''
The traceback module can also format messages as strings and route them to specific
file objects
'''


"Other sys Module Exports"
'''
sys module exports additional commonly-used tools.For instance:
    • Command-line arguments show up as a list of strings called sys.argv.
    • Standard streams are available as sys.stdin, sys.stdout, and sys.stderr.
    • Program exit can be forced with sys.exit calls.
'''
