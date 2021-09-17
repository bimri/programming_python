"Custom Dialogs"
'''
Custom dialogs support arbitrary interfaces, but they are also the most complicated to
program. Even so, there’s not much to it—simply create a pop-up window as a
Toplevel with attached widgets, and arrange a callback handler to fetch user inputs
entered in the dialog (if any) and to destroy the window.
'''

import sys
from tkinter import *
makemodal = (len(sys.argv) > 1)

def dialog():
    win = Toplevel()                                        # make a new window
    Label(win, text='Hard drive reformatted!').pack()       # add a few widgets
    Button(win, text='OK', command=win.destroy).pack()      # set destroy callback
    if makemodal:
        win.focus_set()         # take over input focus,
        win.grab_set()          # disable other windows while I'm open,
        win.wait_window         # and wait here until win destroyed
    print('dialog exit')        # else returns right away


root = Tk()
Button(root, text='popup', command=dialog).pack()
root.mainloop()


'''
Because dialogs are nonmodal in this mode, the
root window remains active after a dialog is popped up. In fact, nonmodal dialogs never
block other windows, so you can keep pressing the root’s button to generate as many
copies of the pop-up window as will fit on your screen.
'''
