"Other ways to be modal"

from tkinter import *

def dialog():
    win = Toplevel()                                            # make a new window
    Label(win, text='Hard drive reformatted!').pack()           # add a few widgets
    Button(win, text='OK', command=win.quit).pack()             # set quit callback
    win.protocol('WM_DELETE_WINDOW', win.quit)                  # quit on wm close too!

    win.focus_set()             # take over input focus,
    win.grab_set()              # disavle other windows while I'm open
    win.mainloop()              # and start a nested event loop to wait
    win.destroy()
    print('dialog exit')


root = Tk()
Button(root, text='popup', command=dialog).pack()
root.mainloop()


'''
If you go this route, be sure to call quit rather than destroy in dialog callback handlers
(destroy doesn’t terminate the mainloop level), and be sure to use protocol to make the
window border close button call quit too (or else it won’t end the recursive mainloop
level call and may generate odd error messages when your program finally exits). Because
of this extra complexity, you’re probably better off using wait_window or
wait_variable, not recursive mainloop calls.
'''
