"""
spawn FTP get and put GUIs no matter what directory I'm run from; os.getcwd is not 
necessarily the place this script lives;  could also hardcode path from $PP4EHOME,
or guessLocation;  could also do:  [from PP4E.launchmodes import PortableLauncher, 
PortableLauncher('getfilegui', '%s/getfilegui.py' % mydir)()], but need the DOS
console pop up on Windows to view status messages which describe transfers made;
"""

import os, sys
print('Running in: ', os.getcwd())

# PP3E
# from PP4E.Launcher import findFirst
# mydir = os.path.split(findFirst(os.curdir, 'PyFtpGui.pyw'))[0]

# PP4E
from chapter_6.find import findlist
mydir = os.path.dirname(findlist('PyFtpGui.pyw', startdir=os.curdir)[0])

if sys.platform[:3] == 'win':
    os.system('start %s\getfilegui.py' % mydir)
    os.system('start %s\putfilegui.py' % mydir)
else:
    os.system('python %s/getfilegui.py &' % mydir)
    os.system('python %s/putfilegui.py &' % mydir)


'''
find utility
    to locate the home directory of the script in order to build command lines.

When run by launchers in the examples root directory or command lines elsewhere in
general, the current working directory may not always be this script’s container.
'''