"One More for Old Times’ Sake"

from tkinter import *
Label(None, {'text': 'Hello GUI world!', Pack: {'side': 'top'}}).mainloop()


'''
This makes the window in just two lines, albeit arguably gruesome ones! This scheme
relies on an old coding style that was widely used until Python 1.3, which passed
configuration options in a dictionary instead of keyword arguments.# In this scheme,
packer options can be sent as values of the key Pack (a class in the tkinter module).

This makes the window in just two lines, albeit arguably gruesome ones! This scheme
relies on an old coding style that was widely used until Python 1.3, which passed
configuration options in a dictionary instead of keyword arguments.# In this scheme,
packer options can be sent as values of the key Pack (a class in the tkinter module).

On the other hand, the func(*pargs, **kargs) syntax now also allows you to pass an
explicit dictionary of keyword arguments in its third argument slot:
    options = {'text': 'Hello GUI world!'}
    layout = {'side': 'top'}
    Label(None, **options).pack(**layout) # keyword must be strings

 Even in dynamic scenarios where widget options are determined at run time, there’s
no compelling reason to ever use the pre-1.3 tkinter dictionary call form.
'''
