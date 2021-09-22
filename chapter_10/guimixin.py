"Mixin Utility Classes"
'''
we can implement common methods in a class and inherit them everywhere
they are needed. Such classes are commonly called mixin classes because their
methods are “mixed in” with other classes. Mixins serve to package generally useful
tools as methods. The concept is almost like importing a module, but mixin classes can
access the subject instance, self, to utilize both per-instance state and inherited methods.
'''

"""
###############################################################################
a "mixin" class for other frames: common methods for canned dialogs,
spawning programs, simple text viewers, etc; this class must be mixed
with a Frame (or a subclass derived from Frame) for its quit method
###############################################################################
"""

from tkinter import * 
from tkinter.messagebox import * 
from tkinter.filedialog import * 
from chapter_9.scrolledtext import ScrolledText                    # or tkinter.scrolledtext
from chapter_5.launchmodes import PortableLauncher, System          # or use multiprocessing


class GuiMixin:
    def infobox(self, title, text, *args):                          # use standard dialogs
        return showinfo(title, text)                                # *args for backward comaptibility
    
    def errorbox(self, text):
        showerror('Error!', text)
    
    def question(self, title, text, *args):
        return askyesno(title, text)                                # return True or False
    
    def notdone(self):
        showerror('Not implemented', 'Optin not available')
    
    def quit(self):
        ans = self.question('Verify quit', 'Are you sure you want to quit?')
        if ans:
            Frame.quit(self)                                        # quit not recursive!
        
    def help(self):
        self.infobox('RTFM', 'See figure 1...')                     # override this better
    
    def selectOpenFile(self, file="", dir='.'):                     # use standard dialogs
        return askopenfilename(initialdir=dir, initialfile=file)
    
    def selectSaveFile(self, file="", dir="."):
        return asksaveasfilename(initialfile=file, initialdir=dir)
    
    def clone(self, args=()):               # optional constructor args
        new = Toplevel()                    # make new in-process version of me
        myclass = self.__class__            # instance's (lowest) class object
        myclass(new, *args)                 # attach/run instance to new window
    
    def spawn(self, pycmdline, wait=False):
        if not wait:                                            # start new process
            PortableLauncher(pycmdline, pycmdline)()            # run Python program
        else:
            System(pycmdline, pycmdline)()                      # wait for it to exit
        
    def browser(self, filename):                                
        new = Toplevel()                                        # make new window
        view = ScrolledText(new, file=filename)                 # Text with Scrollbar
        view.text.config(height=30, width=85)                   # config Text in Frame
        view.text.config(font=('courier', 10, 'normal'))        # use fixed-width font
        new.title('Text Viewer')                                # set window mgr attrs
        new.iconname('browser')                                 # file text added auto
    
    """
    def browser(self, filename): # if tkinter.scrolledtext
        new = Toplevel() # included for reference
        text = ScrolledText(new, height=30, width=85)
        text.config(font=('courier', 10, 'normal'))
        text.pack(expand=YES, fill=BOTH)
        new.title("Text Viewer")
        new.iconname("browser")
        text.insert('0.0', open(filename, 'r').read() )
    """


if __name__ == '__main__':

    class TestMixin(GuiMixin, Frame):           # standalone test
        def __init__(self, parent=None):
            Frame.__init__(self, parent)
            self.pack()
            Button(self, text='quit', command=self.quit).pack(fill=X)
            Button(self, text='help', command=self.help).pack(fill=X)
            Button(self, text='clone', command=self.clone).pack(fill=X)
            Button(self, text='spawn', command=self.other).pack(fill=X)
        def other(self):
            self.spawn('guimixin.py')           # spawn self as separate process
        
    
    TestMixin().mainloop()


'''
The GuiMixin class is meant to be a library of reusable tool methods and is essentially
useless by itself. In fact, it must generally be mixed with a Frame-based class to be used:
quit assumes it’s mixed with a Frame, and clone assumes it’s mixed with a widget class.
To satisfy such constraints, this module’s self-test code at the bottom combines Gui
Mixin with a Frame widget.
'''


"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Make sure your PYTHONPATH includes the Chapter_8&9 directory’s 
container for the cross-directory package
imports in this example and later examples which use it.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
