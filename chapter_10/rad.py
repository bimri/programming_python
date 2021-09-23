"Reloading Callback Handlers Dynamically"
# reload callback handlers dynamically

from tkinter import *
import radactions                                           # get initial callback handlers
from importlib import reload


class Hello(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.make_widgets()
    
    def make_widgets(self):
        Button(self, text='message1', command=self.message1).pack(side=LEFT)
        Button(self, text='message2', command=self.message2).pack(side=RIGHT)
    
    def message1(self):
        reload(radactions)                                  # need to reload actions module before calling
        radactions.message1()                               # now new version triggered by pressing button
    
    def message2(self):
        reload(radactions)                                  # changes to radactions.py picked up by reload
        radactions.message2(self)                           # call the most recent version; pass self
    
    def method1(self):
        print('exposed method...')                          # called from radactions function

Hello().mainloop()


'''
You can change this file any number of times while the rad
script’s GUI is active; each time you do so, you’ll change the behavior of the GUI when
a button press occurs.
'''

"""
There are other ways to change a GUI while it’s running.
hat appearances can be altered at any time by calling the widget config method,
and widgets can be added and deleted from a display dynamically with methods
such as pack_forget and pack (and their grid manager relatives).
"""

'''
Furthermore, passing a new command=action option setting to a widget’s config method might reset
a callback handler to a new action object on the fly; with enough support code, this
may be a viable alternative to the indirection scheme used earlier to make reloads more
effective in GUIs.
'''
