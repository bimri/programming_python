'''
More commonly, widget options can be set after construction by calling the widget
config method.
'''

# config and titles
from tkinter import *

root = Tk()
widget = Label(root)
widget.config(text='Hello config world')
widget.pack(side=TOP, expand=YES, fill=BOTH)
root.title('Configure world')
root.mainloop()


"""
Notice that this version also calls a root.title method; this call sets the label that
appears at the top of the window.

In general terms, top-level
windows like the Tk root here export window-manager interfaces—i.e., things that
have to do with the border around the window, not its contents.
"""
