"Playing the Monty Python theme song"

#!/usr/local/bin/python
"""
Usage: sousa.py.  Fetch and play the Monty Python theme song.
This will not work on your system as is: it requires a machine with Internet access
and an FTP server account you can access, and uses audio filters on Unix and your 
.au player on Windows.  Configure this and playfile.py as needed for your platform.
"""

from getpass import getpass
import getfile
from chapter_6.playfile import playfile

file = 'sousa.au'                      # default file coordinates
site = 'ftp.rmi.net'                   # Monty Python theme song
dir  = '.'
user = ('lutz', getpass('Pswd?'))

getfile(file, site, dir, user)         # fetch audio file by FTP
playfile(file)                         # send it to audio player

# import os
# os.system('getone.py sousa.au')      # equivalent command line


'''
We’re reusing Example 13-4’s getfile to download, and Chapter 6’s play
file module (Example 6-23) to play the audio sample after it is downloaded (turn back
to that example for more details on the player part of the task).

Also notice the last two
lines in this file—we can achieve the same effect by passing in the audio filename as a
command-line argument to our original script, but it’s less direct.
'''
