"Step 5: Adding a GUI"
'Using OOP for GUIs'
'''
In larger programs, it is often more useful to code a GUI as a subclass
of the tkinter Frame widget—a container for other widgets.
'''

from tkinter import *
from tkinter.messagebox import showinfo


class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.reply)
        button.pack()
    def reply(self):
        showinfo(title='popup', message='Button pressed!')
    


if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()


'''
The button’s event handler is a bound method—self.reply, an object that remembers
both self and reply when later called.

but because it is now a subclass of
Frame, it automatically becomes an attachable component—i.e., we can add all of the
widgets this class creates, as a package, to any other GUI, just by attaching this Frame
to the GUI.
'''
