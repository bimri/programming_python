"Climbing the GUI Learning Curve"
'“Hello World” in Four Lines (or Less)'

from tkinter import Label, Widget                               # get a widget object
widget = Label(None, text='Hello GUI world!')                   # make one
widget.pack( )                                         # arrange it
widget.mainloop()                                               # start event loop


'tkinter Coding Basics'
"""
This Python code does the following:
1. Loads a widget class from the tkinter module
2. Makes an instance of the imported Label class
3. Packs (arranges) the new Label in its parent widget
4. Calls mainloop to bring up the window and start the tkinter event loop
"""


'Avoiding DOS consoles on Windows'
'''
if a program’s name ends in a .pyw extension rather
than a .py extension, the Windows Python port does not pop up a DOS console box
to serve as its standard streams when the file is launched by clicking its filename icon.

If you just want to see the windows that your script makes no matter how it is launched,
be sure to name your GUI scripts with a .pyw if they might be run on Windows.

You can also avoid the DOS pop up on Windows by running the program with the
pythonw.exe executable, not python.exe (in fact, .pyw files are simply registered to be
opened by pythonw)
'''
 