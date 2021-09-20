"""
FAILS-- can't grid and pack in same parent container (here, root window)
"""

from tkinter import *
from grid2 import gridbox, packbox

# root = Tk()
# gridbox(root)
# packbox(root)
# Button(root, text='Quit', command=root.quit).pack()
# mainloop()


'''
This script passes the same parent (the top-level window) to each function in an effort
to make both forms appear in one window. It also utterly hangs the Python process on
my machine, without ever showing any windows at all (on some versions of Windows,
I’ve had to resort to Ctrl-Alt-Delete to kill it; on others, the Command Prompt shell
window must sometimes be restarted altogether).
'''


"""
Geometry manager combinations can be subtle until you get the hang of this. To make
this example work, for instance, we simply need to isolate the grid box in a parent
container all its own to keep it away from the packing going on in the root window—
as in the following bold alternative code:
    root = Tk()
    frm = Frame(root)
    frm.pack() # this works
    gridbox(frm) # gridbox must have its own parent in which to grid
    packbox(root)
    Button(root, text='Quit', command=root.quit).pack()
    mainloop()
"""
