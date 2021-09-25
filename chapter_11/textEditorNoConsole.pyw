"Windows (and other) launch files" 
'''
gives the .pyw launching file used to suppress a DOS pop up on
Windows when run in some modes (for instance, when double-clicked), but still allow
for a console when the .py file is run directly.

Clicking this directly is similar to the behavior when PyEdit
is run from the PyDemos or PyGadgets demo launcher bars.
'''

"""
run without a DOS pop up on Windows; could use just a .pyw for both
imports and launch, but .py file retained for seeing any printed text
"""

exec(open('textEditor.py').read())                          # as if pasted here (or textEditor.main())
