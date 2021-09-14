"Widget Resizing Basics"
# expansion

from tkinter import *
Label(text='Hello GUI world!').pack(expand=YES, fill=BOTH)
mainloop()


'''
Technically, the packer geometry manager assigns a size to each widget in a display
based on what it contains. By default, a widget can occupy
only its allocated space and is no bigger than its assigned size. The expand and fill
options let us be more specific about such things:
    expand=YES option
        Asks the packer to expand the allocated space for the widget in general into any
        unclaimed space in the widget’s parent.
    fill option
        Can be used to stretch the widget to occupy all of its allocated space.

Combinations of these two options produce different layout and resizing effects, some
of which become meaningful only when there are multiple widgets in a window. For
example, using expand without fill centers the widget in the expanded space, and the
fill option can specify vertical stretching only (fill=Y), horizontal stretching only
(fill=X), or both (fill=BOTH). By providing these constraints and attachment sides for
all widgets in a GUI, along with packing order, we can control the layout in fairly precise
terms. In later chapters, we’ll find that the grid geometry manager uses a different
resizing protocol entirely, but it provides similar control when needed.        
'''
