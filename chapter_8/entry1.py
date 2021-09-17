"Entry"
'''
The Entry widget is a simple, single-line text input field. It is typically used for input
fields in form-like dialogs and anywhere else you need the user to type a value into a
field of a larger display. Entry also supports advanced concepts such as scrolling, key
bindings for editing, and text selections.
'''

from tkinter import *
from quitter import Quitter

def fetch():
    print('Input => "%s' % ent.get())           # get text


root = Tk()
ent = Entry(root)
ent.insert(0, 'Type words here')                # set text
ent.pack(side=TOP, fill=X)                      # grow horizontally

ent.focus()                                     # save a click
ent.bind('<Return>', lambda event: fetch())     # on enter key
btn = Button(root, text='Fetch', command=fetch) # and on button
btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()
