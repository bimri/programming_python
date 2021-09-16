"Customizing Widgets with Classes"

from tkinter import *


class HelloButton(Button):
    def __init__(self, parent=None, **config):              # add callback method
        Button.__init__(self, parent, **config)             # and pack myself
        self.pack()                                         # could config style too
        self.config(command=self.callback)

    def callback(self):                                     # default press action
        print('Goodbye world...')                           # replace in subclass
        self.quit()


if __name__ == '__main__':
    HelloButton(text='Hello subclass world').mainloop()     # make me load


'''
it is a button widget we created on
our own. The HelloButton class inherits everything from the tkinter Button class, but
adds a callback method and constructor logic to set the command option to
self.callback, a bound method of the instance.

The **config argument here is assigned unmatched keyword arguments in a dictionary,
so they can be passed along to the Button constructor. The **config in the Button
constructor call unpacks the dictionary back into keyword arguments
'''
