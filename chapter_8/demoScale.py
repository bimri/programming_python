"create two linked scales used to launch dialog demos"

from tkinter import *                                   # get base widget set
from dialogTable import demos                           # button callback handlers
from quitter import Quitter                             # attach a quit frame to me

class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="Scale demos").pack()
        self.var = IntVar()
        Scale(self, label='Pick demo number',
            command=self.onMove,                        # catch moves
            variable=self.var,                          # reflects position
            from_=0, to=len(demos)-1).pack()
        Scale(self, label='Pick demo number',
            command=self.onMove,                        # catch moves
            variable=self.var,                          # reflects position
            from_=0, to=len(demos)-1,
            length=200, tickinterval=1,
            showvalue=YES, orient='horizontal').pack()
        Quitter(self).pack(side=RIGHT)
        Button(self, text="Run demo", command=self.onRun).pack(side=LEFT)
        Button(self, text="State", command=self.report).pack(side=RIGHT)
    
    def onMove(self, value):
        print('in onMove', value)
    
    def onRun(self):
        pos = self.var.get()
        print('You picked', pos)
        demo = list(demos.values())[pos]                # map from 1..n to values
        print(demo())                                   # run it
    
    def report(self):
        print(self.var.get())
    

if __name__ == '__main__':
    print(list(demos.keys()))
    Demo().mainloop()


"""
    • The label option provides text that appears along with the scale, length specifies
    an initial size in pixels, and orient specifies an axis.
    • The from_ and to options set the scale range’s minimum and maximum values (note
    that from is a Python reserved word, but from_ is not).
    • The tickinterval option sets the number of units between marks drawn at regular
    intervals next to the scale (the default means no marks are drawn).
    • The resolution option provides the number of units that the scale’s value jumps
    on each drag or left mouse click event (defaults to 1).
    • The showvalue option can be used to show or hide the scale’s current value next to
    its slider bar (the default showvalue=YES means it is drawn).
"""
