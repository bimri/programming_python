import gui7 
from tkinter import *

class HelloPackage(gui7.HelloPackage):
    def __getattr__(self, name):
        return getattr(self.top, name)                      # pass off to a read widget
    

if __name__ == '__main__':                                  # invokes __getattr__!
    HelloPackage().mainloop()
