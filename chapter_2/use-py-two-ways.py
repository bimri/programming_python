"Using Programs in Two Ways"
'''
the last few lines in the more.py file in Example 2-1 introduce
one of the first big concepts in shell tool programming. They instrument the file to be
used in either of two ways—as a script or as a library.

Recall that every Python module has a built-in __name__ variable that Python sets to the
__main__ string only when the file is run as a program, not when it’s imported as a
library.

Because of that, the more function in this file is executed automatically by the
last line in the file when this script is run as a top-level program, but not when it is
imported elsewhere. This simple trick turns out to be one key to writing reusable script
code: by coding program logic as functions rather than as top-level code, you can also
import and reuse it in other scripts.
'''
# words typed in the command that is used to start a program show up 
# in the built-in sys.argv list in Python.


"""
When the more.py file is imported, we pass an explicit string to its more function, and
this is exactly the sort of utility we need for documentation text. Running this utility
on the sys module’s documentation string gives us a bit more information in humanreadable
form about what’s available to scripts:
    C:\...\PP4E\System> python
    >>> from more import more
    >>> import sys
    >>> more(sys.__doc__)
"""

'''
Pressing “y” or “Y” here makes the function display the next few lines of documentation,
and then prompt again, unless you’ve run past the end of the lines list.
'''
