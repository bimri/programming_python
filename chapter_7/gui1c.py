# roots, sides, pack in place
from tkinter import *
root = Tk()
Label(root, text='Hello GUI, world!').pack(side=TOP)
root.mainloop()


'''
When widgets are packed, we can specify which side of their parent they should be
attached to—TOP, BOTTOM, LEFT, or RIGHT.

In general, larger tkinter
GUIs can be constructed as sets of rectangles, attached to the appropriate sides of other, 
enclosing rectangles.
'''