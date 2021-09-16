"Standardizing Behavior and Appearance"
'Common behavior'

from gui5 import HelloButton
from tkinter import Tk, Button


class MyButton(HelloButton):                        # subclass HelloButton
    def callback(self):                                 # redefine callback
        print('Ignoring press!.....')
    

if __name__ == '__main__':
    MyButton(None, text='Hello subclass world').mainloop()


'''
Tk becomes truly object oriented in Python, just because Python is object oriented—we
can specialize widget classes using normal class-based and object-oriented techniques.
'''


"Common appearance"
'''
a similar customized button class could provide a standard look-and-feel
different from tkinter’s defaults for every instance created from it, and approach the
notions of “styles” or “themes” in some GUI toolkits:
'''
class ThemedButton(Button):                             # config my style too
    def __init__(self, parent=None, **configs):         # used for each instance
        Button.__init__(self, parent, **configs)
        self.pack()
        self.config(fg='red', bg='black', font=('courier', 12, 'normal'))
        self.config(text='Spam')


B1 = ThemedButton(text='one', command=onSpam)           # normal button widget objects
B2 = ThemedButton(text='two')                           # but same appearance by inheritance
B2.pack(expand=YES, fill=BOTH)
