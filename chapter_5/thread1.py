"The _thread Module"
'''
_thread module is a bit simpler than the more advanced threading
module.

This module
provides a portable interface to whatever threading system is available in your platform:
its interfaces work the same on Windows, Solaris, SGI, and any system with an installed
pthreads POSIX threads implementation (including Linux and others). Python scripts
that use the Python _thread module work on all of these platforms without changing
their source code.
'''

"Basic usage"
"spawn threads until you type 'q'"

import _thread

def child(tid):
    print('Hello from thread', tid)


def parent():
    i = 0
    while True:
        i += 1
        _thread.start_new_thread(child, (i,))
        if input() == 'q': break
    

parent()


'''
This call takes a function (or other callable) object and an arguments tuple and
starts a new thread to execute a call to the passed function with the passed arguments.
It’s almost like Python’s function(*args) call syntax, and similarly accepts an optional
keyword arguments dictionary, too, but in this case the function call begins running in
parallel with the rest of the program.
'''


"Other ways to code threads with _thread"
import _thread                                          # all 3 print 4294967296

def action(i):                                          # function run in threads
    print(i ** 32)


class Power:
    def __init__(self, i):
        self.i = i
    def action(self):                                   # bound method run in threads
        print(self.i ** 32)
    

_thread.start_new_thread(action, (2,))                  # simple function

_thread.start_new_thread((lambda: action(2)), ())       # lambda function to defer

obj = Power(2)
_thread.start_new_thread(obj.action, ())                # bound method object
 

"""
bound methods are especially useful
in this role—because they remember both the method function and instance object,
they also give access to state information and class methods for use within and during
the thread.

More fundamentally, because threads all run in the same process, bound methods run
by threads reference the original in-process instance object, not a copy of it. Hence, any
changes to its state made in a thread will be visible to all threads automatically.
"""
