"Extending Class Components"

from tkinter import *
from gui6 import Hello 

class HelloExtender(Hello):
    def make_widgets(self):                         # extend method here
        Hello.make_widgets(self)                    # invoke superclass method
        Button(self, text='Extend', command=self.quit).pack(side=RIGHT)
    
    def message(self):
        print('hello', self.data)                   # redifine method here
    

if __name__ == '__main__': HelloExtender().mainloop()



"""
Although this example is simple, it demonstrates a technique that can be powerful in
practice: to change a GUI’s behavior, we can write a new class that customizes its parts
rather than changing the existing GUI code in place. The main code need be debugged
only once and can be customized with subclasses as unique needs arise.

The moral of this story is that tkinter GUIs can be coded without ever writing a single
new class, but using classes to structure your GUI code makes it much more reusable
in the long run. If done well, you can both attach already debugged components to new
interfaces and specialize their behavior in new external subclasses as needed for custom
requirements. Either way, the initial upfront investment to use classes is bound to save
coding time in the end.
"""
