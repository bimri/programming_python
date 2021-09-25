'''
This script disables the DOS pop up when clicked or run via a
desktop shortcut on Windows, but also takes care to configure the module search path
on machines where I haven’t used Control Panel to do so, and allows for other launching
scenarios where the current working directory may not be the same as the script’s
directory.
'''

#!/usr/bin/python
"""
convenience script to launch pyedit from arbitrary places with the import path set
as required; sys.path for imports and open() must be relative to the known top-level
script's dir, not cwd -- cwd is script's dir if run by shortcut or icon click, but may
be anything if run from command-line typed into a shell console window: use argv path;
this is a .pyw to suppress console pop-up on Windows; add this script's dir to your
system PATH to run from command-lines; works on Unix too: / and \ handled portably;
"""

import sys, os
mydir = os.path.dirname(sys.argv[0])                                        # use my dir for open, path
sys.path.insert(1, os.sep.join([mydir] + ['..']*3))                         # imports: PP4E root, 3 up
exec(open(os.path.join(mydir, 'textEditor.py')).read())


'''
To run this from a command line in a console window, it simply has to be on your
system path—the action taken by the first line in the following could be performed just
once in Control Panel on Windows:
    C:\...\PP4E\Internet\Web> set PATH=%PATH%;C:\...\PP4E\Gui\TextEditor
    C:\...\PP4E\Internet\Web> pyedit.pyw test-cookies.py

'''