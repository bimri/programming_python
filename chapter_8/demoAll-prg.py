"Running Programs"

"""
4 demo classes run as independent program processes: command lines;
if one window is quit now, the others will live on; there is no simple way to
run all report calls here (though sockets and pipes could be used for IPC), and
some launch schemes may drop child program stdout and disconnect parent/child;
"""

from tkinter import *
from ..launchmodes import PortableLauncher
demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']

for demo in demoModules: # see Parallel System Tools
    PortableLauncher(demo, demo + '.py')() # start as top-level programs

root = Tk()
root.title('Processes')
Label(root, text='Multiple program demo: command lines', bg='white').pack()
root.mainloop()


"""
Make sure the PP4E directory’s container is on your module search path (e.g.,
PYTHONPATH) to run this; it imports an example module from a different directory.
"""
