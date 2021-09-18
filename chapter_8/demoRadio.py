"Radio Buttons"
'''
Radio buttons are toggles too, but they are generally used in groups:
only one can be selected at one time. In tkinter, associating all radio buttons
in a group with unique values and the same variable guarantees that, at most, only one
can ever be selected at a given time.

In addition, radio buttons have a value attribute that lets you tell tkinter what value
the button’s associated variable should have when the button is selected. Because more
than one radio button is associated with the same variable, you need to be explicit about
each button’s value (it’s not just a 1 or 0 toggle scenario).
'''

"create a group of radio buttons that launch dialog demos"

from tkinter import *
from typing import Pattern                  # get base widget set
from dialogTable import demos               # button callback handlers
from quitter import Quitter                 # attach a quit object to "me"


class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="Radio demos").pack(side=TOP)
        self.var = StringVar()
        for key in demos:
            Radiobutton(self, text=key, command=self.onPress, variable=self.var, value=key).pack(anchor=NW)
        self.var.set(key)                   # select last to start
        Button(self, text='State', command=self.report).pack(fill=X)
        Quitter(self).pack(fill=X)

    def onPress(self):
        pick = self.var.get()
        print('you pressed', pick)
        print('result:', demos[pick]())
    
    def report(self):
        print(self.var.get())
    

if __name__ == '__main__':
    Demo().mainloop()
