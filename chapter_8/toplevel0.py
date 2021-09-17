"Top-Level Windows"
'''
tkinter GUIs always have an application root window, whether you get it by default or
create it explicitly by calling the Tk object constructor. This main root window is the
one that opens when your program runs, and it is where you generally pack your most
important and long-lived widgets. In addition, tkinter scripts can create any number
of independent windows, generated and popped up on demand, by creating Toplevel
widget objects.

Each Toplevel object created produces a new window on the display and automatically
adds it to the program’s GUI event-loop processing stream
'''

import sys 
from tkinter import Toplevel, Button, Label 

win1 = Toplevel()                               # two independent windows
win2 = Toplevel()                               # but part of same process

Button(win1, text='bimri', command=sys.exit).pack()
Button(win2, text='BIMRI', command=sys.exit).pack()

Label(text='Popups').pack()                     # on default Tk() root window
win1.mainloop()


'''
The toplevel0 script gets a root window by default (that’s what the Label is attached to,
since it doesn’t specify a real parent), but it also creates two standalone Toplevel windows
that appear and function independently of the root window.
'''


"""
The two Toplevel windows on the right are full-fledged windows; they can be independently
iconified, maximized, and so on. Toplevels are typically used to implement
multiple-window displays and pop-up modal and nonmodal dialogs.
"""


'''
It’s important to know that although Toplevels are independently active windows, they
are not separate processes; if your program exits, all of its windows are erased, including
all Toplevel windows it may have created.
'''