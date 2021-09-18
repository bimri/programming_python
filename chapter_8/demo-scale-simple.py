"Scales and variables"

from tkinter import *
root = Tk()
scl  = Scale(root, from_=-100, to =100, tickinterval =25, resolution =10)
scl.pack(expand=YES, fill=Y)

def report():
    print(scl.get())

Button(root, text='State', command=report).pack(side=RIGHT)
root.mainloop()


"""
Its scale displays a
range from −100 to 100, uses the resolution option to adjust the current position up
or down by 10 on every move, and sets the tickinterval option to show values next to
the scale in increments of 50. When you press the State button in this script’s window,
it calls the scale’s get method to display the current setting, without variables or callbacks
of any kind.
"""
