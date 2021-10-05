"FTP get and put Utilities"

#!/usr/local/bin/python
"""
A Python script to download and play a media file by FTP.
Uses getfile.py, a utility module which encapsulates FTP step.
"""

import getfile
from getpass import getpass
filename = 'monkeys.jpg'

# fetch with utility
getfile.getfile(file=filename, site='ftp.rmi.net', 
                dir='.', user=('lutz', getpass('Pswd')), 
                refetch=True)

# rest is the same
if input('Open file?') in ['Y', 'y']:
    from chapter_6.playfile import playfile
    playfile(filename)


'''
Besides having a much smaller line count, the meat of this script has been split off into
a file for reuse elsewhere. If you ever need to download a file again, simply import an
existing function instead of copying code with cut-and-paste editing. Changes in download
operations would need to be made in only one file, not everywhere we’ve copied
boilerplate code; getfile.getfile could even be changed to use urllib rather than
ftplib without affecting any of its clients. It’s good engineering.
'''
