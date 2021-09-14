"Adding Buttons and Callbacks"

import sys 
from tkinter import *
widget = Button(None, text='Hello GUI world!', command=sys.exit)
widget.pack()
widget.mainloop()


'''
Here, instead of making a label, we create an instance of the tkinter Button class.

For buttons, the command option is the place where we specify a callback handler function
to be run when the button is later pressed. In effect, we use command to register an
action for tkinter to call when a widget’s event occurs.
'''
