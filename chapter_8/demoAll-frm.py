"Running GUI Code Three Ways"
'''
Because the demos were coded as both reusable
classes and scripts, they can be deployed as attached frame components, run in their
own top-level windows, and launched as standalone programs.
'''

"""
4 demo class components (subframes) on one window;
there are 5 Quitter buttons on this one window too, and each kills entire gui;
GUIs can be reused as frames in container, independent windows, or processes;
"""

from tkinter import *
from quitter import Quitter
demoModules = ['demoDlg', 'demoCheck', 'demoRadio', 'demoScale']
parts = []


def addComponents(root):
    for demo in demoModules:
        module = __import__(demo)                           # import by name string
        part = module.Demo(root)                            # attach an instance
        part.config(bd=2, relief=GROOVE)                    # or pass config to Demo()
        part.pack(side=LEFT, expand=YES, fill=BOTH)         # grow, stretch with window
        parts.append(part)                                  # change list in-place
    

def dumpState():
    for part in parts:                                      # run demo report if any
        print(part.__module__ + ':', end=' ')
        if hasattr(part, 'report'):
            part.report()
        else:
            print('none')


root = Tk()                                                 # make explicit root first
root.title('Frame')
Label(root, text='Multiple Frame demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()
