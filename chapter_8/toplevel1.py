"Toplevel and Tk Widgets"
'''
A Toplevel is roughly like a Frame that is split off into its own window and has additional
methods that allow you to deal with top-level window properties. The Tk widget is
roughly like a Toplevel, but it is used to represent the application root window.
Toplevel windows have parents, but Tk windows do not—they are the true roots of the
widget hierarchies we build when making tkinter GUIs.

Technically, you can suppress the default root creation logic and make multiple root
windows with the Tk widget
'''

import tkinter
from tkinter import Tk, Button
tkinter.NoDefaultRoot()

win1 = Tk()                         # two independent root windows
win2 = Tk()

Button(win1, text='bimri', command=win1.destroy).pack()
Button(win2, text='BIMRI', command=win1.destroy).pack()
win1.mainloop()


'''
Notice how this GUI’s windows use a window’s destroy method to close just one
window, instead of sys.exit to shut down the entire program;
'''
