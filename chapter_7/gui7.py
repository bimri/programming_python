"Standalone Container Classes"

from tkinter import *


class HelloPackage:                             # not a widget subbclass
    def __init__(self, parent=None):
        self.top = Frame(parent)                # embed a Frame
        self.top.pack()
        self.data = 0
        self.make_widgets()                     # attach widgets to self.top                
    
    def make_widgets(self):
        Button(self.top, text='Bye', command=self.top.quit).pack(side=LEFT)
        Button(self.top, text='Hello', command=self.message).pack(side=RIGHT)
    
    def message(self):
        self.data += 1
        print('Hello number', self.data)
    


if __name__ == '__main__':
    HelloPackage().top.mainloop()


'''
Also as before, self.data retains state between events, and callbacks are routed to the
self.message method within this class. Unlike before, the HelloPackage class is not itself
a kind of Frame widget. In fact, it’s not a kind of anything—it serves only as a generator
of namespaces for storing away real widget objects and state.
'''
