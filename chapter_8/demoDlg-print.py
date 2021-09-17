"Printing dialog results and passing callback data with lambdas"
"""
similar, but show return values of dialog calls; the lambda saves data from
the local scope to be passed to the handler (button press handlers normally
get no arguments, and enclosing scope references don't work for loop variables)
and works just like a nested def statement: def func(key=key): self.printit(key)
"""

from tkinter import *                   # get base widget set
from dialogTable import demos           # button callback handlers
from quitter import Quitter             # attach a quit object to me


class Demo(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text='Basics demos').pack()
        for key in demos:
            func = (lambda key=key: self.printit(key))
            Button(self, text=key, command=func).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)
    
    def printit(self, name):
        print(name, 'returns =>', demos[name]())            # fetch, call, print

if __name__ == '__main__': Demo().mainloop()


'''
Because button-press callbacks
are run with no arguments, if we need to pass extra data to the handler, it must
be wrapped in an object that remembers that extra data and passes it along, by deferring
the call to the actual handler. Here, a button press runs the function generated by the
lambda, an indirect call layer that retains information from the enclosing scope.

The net effect is that the real handler, printit, receives an extra required name argument
giving the demo associated with the button pressed, even though this argument wasn’t
passed back from tkinter itself. In effect, the lambda remembers and passes on state
information.
'''