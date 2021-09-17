"Dialogs" 
'''
Dialogs are windows popped up by a script to provide or request additional information.
They come in two flavors, modal and nonmodal:
    Modal
        These dialogs block the rest of the interface until the dialog window is dismissed;
        users must reply to the dialog before the program continues.
    
    Nonmodal
        These dialogs can remain on-screen indefinitely without interfering with other
        windows in the interface; they can usually accept inputs at any time.

Regardless of their modality, dialogs are generally implemented with the Toplevel window
object.        

There are essentially three ways to present pop-up dialogs to users with tkinter—by using
common dialog calls, by using the now-dated Dialog object, and by creating custom
dialog windows with Toplevels and other kinds of widgets.
'''


'Standard (Common) Dialogs'
'''
Because standard dialog calls are simpler, let’s start here first. tkinter comes with a
collection of precoded dialog windows that implement many of the most common pop
ups programs generate—file selection dialogs, error and warning pop ups, and question
and answer prompts. They are called standard dialogs (and sometimes common dialogs)
because they are part of the tkinter library, and they use platform-specific library
calls to look like they should on each platform.

All standard dialog calls are modal (they don’t return until the dialog box is dismissed
by the user), and they block the program’s main window while they are displayed.
Scripts can customize these dialogs’ windows by passing message text, titles, and the
like.
'''

from tkinter import *
from tkinter.messagebox import * 


def callback():
    if askyesno('Verify', 'Do you really want to quit?'):
        showwarning('Yes', 'Quit not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')
    

errmsg = 'Sorry, no Spam allowed!'
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('Spam', errmsg))).pack(fill=X)
mainloop()


'''
A lambda anonymous function is used here to wrap the call to showerror so that it is
passed two hardcoded arguments (remember, button-press callbacks get no arguments
from tkinter itself).
'''