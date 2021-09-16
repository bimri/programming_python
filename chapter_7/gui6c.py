from tkinter import *                           # get Tk widget classes
from gui6 import Hello                          # import the subframe class


class HelloContainer(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.make_widgets()
    
    def make_widgets(self):
        Hello(self).pack(side=RIGHT)           # attach a Hello to me
        Button(self, text='Attach', command=self.quit).pack(side=LEFT)
    


if __name__ == '__main__': HelloContainer().mainloop()


'''
This looks and works exactly like gui6b but registers the added button’s callback handler
as self.quit, which is just the standard quit widget method this class inherits from
Frame.
'''
