"Adding Multiple Widgets"

from tkinter import *

def greeting():
    print('Hello stdout world!...')


win = Frame()
win.pack()
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Hello', command=greeting).pack(side=LEFT)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT)

win.mainloop()


'''
This example makes a Frame widget (another tkinter class) and attaches three other
widget objects to it, a Label and two Buttons, by passing the Frame as their first argument.

In tkinter terms, we say that the Frame becomes a parent to the other three
widgets. Both buttons on this display trigger callbacks:
    • Pressing the Hello button triggers the greeting function defined within this file,
    which prints to stdout again.
    • Pressing the Quit button calls the standard tkinter quit method, inherited by win
    from the Frame class (Frame.quit has the same effect as the Tk.quit we used earlier).
'''


'Widget Resizing Revisited: Clipping'
# Button(win, text='Hello', command=greeting).pack(side=LEFT)
# Button(win, text='Quit', command=win.quit).pack(side=RIGHT)
# Label(win, text='Hello container world').pack(side=TOP) 


"Attaching Widgets to Frames"
'''
Frame widgets
are just containers for other widgets, and so give rise to the notion of GUIs as widget
hierarchies, or trees. Here, win serves as an enclosing window for the other three
widgets. In general, though, by attaching widgets to frames, and frames to other frames,
we can build up arbitrary GUI layouts. Simply divide the user interface into a set of
increasingly smaller rectangles, implement each as a tkinter Frame, and attach basic
widgets to the frame in the desired screen position.
'''


"Layout: Packing Order and Side Attachments"
'''
When a widget tree is displayed, child widgets appear inside their parents and are
arranged according to their order of packing and their packing options. Because of this,
the order in which widgets are packed not only gives their clipping order, but also
determines how their side settings play out in the generated display.
Here’s how the packer’s layout system works:

    1. The packer starts out with an available space cavity that includes the entire parent
    container (e.g., the whole Frame or top-level window).
    2. As each widget is packed on a side, that widget is given the entire requested side
    in the remaining space cavity, and the space cavity is shrunk.
    3. Later pack requests are given an entire side of what is left, after earlier pack requests
    have shrunk the cavity.
    4. After widgets are given cavity space, expand divides any space left, and fill and
    anchor stretch and position widgets within their assigned space.
'''
# Button(win, text='Hello', command=greeting).pack(side=LEFT)
# Label(win, text='Hello container world').pack(side=TOP)
# Button(win, text='Quit', command=win.quit).pack(side=RIGHT)


"The Packer’s Expand and Fill Revisited"
'''
Beyond the effects of packing order, the fill option we met earlier can be used to stretch
the widget to occupy all the space in the cavity side it has been given, and any cavity
space left after all packing is evenly allocated among widgets with the expand=YES
'''
# Button(win, text='Hello', command=greeting).pack(side=LEFT,fill=Y)
# Label(win, text='Hello container world').pack(side=TOP)
# Button(win, text='Quit', command=win.quit).pack(side=RIGHT, expand=YES, fill=X)

# win = Frame()
# win.pack(side=TOP, expand=YES, fill=BOTH)
# Button(win, text='Hello', command=greeting).pack(side=LEFT, fill=Y)
# Label(win, text='Hello container world').pack(side=TOP)
# Button(win, text='Quit', command=win.quit).pack(side=RIGHT, expand=YES,fill=X)


"Using Anchor to Position Instead of Stretch"
'''
the packer also allows widgets to be positioned
within their allocated space with an anchor option, instead of filling that space with a
fill. The anchor option accepts tkinter constants identifying all eight points of the
compass (N, NE, NW, S, etc.) and CENTER as its value (e.g., anchor=NW).
'''
# Button(win, text='Hello', command=greeting).pack(side=LEFT, anchor=N)
# Label(win, text='Hello container world').pack(side=TOP)
# Button(win, text='Quit', command=win.quit).pack(side=RIGHT)

"""
Keep in mind that fill and anchor are applied after a widget has been allocated cavity
side space by its side, packing order, and expand extra space request. By playing with
packing orders, sides, fills, and anchors, you can generate lots of layout and clipping
effects

frames can be nested in other frames, too, in order to make more
complex layouts. In fact, because each parent container is a distinct space cavity, this
provides a sort of escape mechanism for the packer cavity algorithm: to better control
where a set of widgets show up, simply pack them within a nested subframe and attach
the frame as a package to a larger container. A row of push buttons, for example, might
be easier laid out in a frame of its own than if mixed with other widgets in the display
directly.

tkinter internally records the relationships implied by passed parent
widget arguments. In OOP terms, this is a composition relationship—the Frame contains
a Label and Buttons.
"""
