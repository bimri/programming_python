"GuiMixin: Common Tool Mixin Classes"
'''
GUI programming often becomes an exercise in
typing, or at least in cut-and-paste text editor operations.
'''
'Widget Builder Functions'
"""
a better idea is to wrap or automate as much
of the GUI construction process as possible.
One approach is to code functions that
provide typical widget configurations, 
and automate the construction process for cases
to which they apply.

For instance, we could define a button function to handle configuration
and packing details and support most of the buttons we draw.
"""


"""
###############################################################################
wrap up widget construction in functions for easier use, based upon some
assumptions (e.g., expansion); use **extras fkw args for width, font/color,
etc., and repack result manually later to override defaults if needed;
###############################################################################
"""

from tkinter import * 

def frame(root, side=TOP, **extras):
    widget = Frame(root)
    widget.pack(side=side, expand=YES, fill=BOTH)
    if extras: widget.config(**extras)
    return widget

def label(root, side, text, **extras):
    widget = Label(root, text=text, relief=RIDGE)               # default config
    widget.pack(side=side, expand=YES, fill=BOTH)               # pack automatically
    if extras: widget.config(**extras)                          # apply any extras
    return widget

def button(root, side, text, command, **extras):
    widget = Button(root, text=text, command=command)
    widget.pack(side=side, expand=YES, fill=BOTH)
    if extras: widget.config(**extras)
    return widget

def entry(root, side, linkvar, **extras):
    widget = Entry(root, relief=SUNKEN, textvariable=linkvar)
    widget.pack(side=side, expand=YES, fill=BOTH)
    if extras: widget.config(**extras)


if __name__ == '__main__':
    app = Tk()
    frm = frame(app, TOP)               # much less code requires here!
    label(frm, LEFT, 'SPAM')
    button(frm, BOTTOM, 'Press', lambda: print('Pushed'))
    mainloop()


'''
This module makes some assumptions about its clients’ use cases, which allows it to
automate typical construction chores such as packing. The net effect is to reduce the
amount of code required of its importers.
'''


"""
This function-based approach can cut down on the amount of code required. As functions,
though, its tools don’t lend themselves to customization in the broader OOP
sense. Moreover, because they are not methods, they do not have access to the state of
an object representing the GUI.
"""
