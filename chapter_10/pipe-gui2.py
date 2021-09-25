# GUI reader side: like pipes-gui1, but make root window and mainloop explicit
from tkinter import *
from chapter_10.guiStreams import redirectedGuiShellCmd

def launch():
    redirectedGuiShellCmd('python -u pipe-nongui.py')


window = Tk()
Button(window, text='GO!', command=launch).pack()
window.mainloop()

'''
The -u unbuffered flag is crucial here again—without it, you won’t see the text output
window. The GUI will be blocked in the initial pipe input call indefinitely because the
spawned program’s standard output will be queued up in an in-memory buffer.
'''
