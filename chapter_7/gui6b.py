"Attaching Class Components"
'''
Perhaps more importantly, subclasses of Frame are true widgets: they can be further
extended and customized by subclassing and can be attached to enclosing widgets. For
instance, to attach the entire package of widgets that a class builds to something else,
simply create an instance of the class with a real parent widget passed in.
'''

from sys import exit
from tkinter import *                           # get Tk widget classes
from gui6 import Hello                          # get the subframe class

parent = Frame(None)                            # make a Frame, no parent: container widget
parent.pack()                                   # size it to fit its widgets
Hello(parent).pack(side=RIGHT)                  # attach Hello, the subframe, to the right

Button(parent, text='Attach', command=exit).pack(side=LEFT)
parent.mainloop()
