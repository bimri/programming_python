"Entry"
'Laying Out Input Forms'
# Entry widgets are often used to get 
# field values in form-like displays.
# combines labels, entries, and frames to 
# achieve the multiple-input display

"""
use Entry widgets directly
lay out by rows with fixed-width labels: this and grid are best for forms
"""

from tkinter import *
from quitter import Quitter
fields = 'Name', 'Job', 'Pay'


def fetch(entries):
    for entry in entries:
        print('Input => "%s"' % entry.get())            # get text

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)                               # make a new row
        lab = Label(row, width=5, text=field)           # add label, entry
        ent = Entry(row)
        row.pack(side=TOP, fill=X)                      # pack row on top
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)        # grow horizontal
        entries.append(ent)
    return entries


if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event: fetch(ents)))
    Button(root, text='Fetch',
           command= (lambda: fetch(ents))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.mainloop()


'''
Most of the art in form layout has to do with arranging widgets in a hierarchy. This
script builds each label/entry row as a new Frame attached to the window’s current
TOP; fixed-width labels are attached to the LEFT of their row, and entries to the RIGHT.
Because each row is a distinct Frame, its contents are insulated from other packing going
on in this window. The script also arranges for just the entry fields to grow vertically
on a resize.
'''
 