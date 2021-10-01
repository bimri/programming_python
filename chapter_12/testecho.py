"Spawning Clients in Parallel"
'''
Realistic servers are generally intended to handle many clients, of
course, and possibly at the same time.
''' 

import sys
from launchmodes import QuietPortableLauncher

numclients = 8
def start(cmdline):
    QuietPortableLauncher(cmdline, cmdline)()

# start('echo-server.py')                         # spawn server locally if not yet started

args = ' '.join(sys.argv[1:])                   # pass server name if running remotely
for i in range(numclients):
    start('echo-client.py %s' % args)           # spawn 8? clients to test the server


'''
To see the
clients’ messages on Windows, you can change testecho to use the StartArgs launcher
with a /B switch at the front of the command line to route messages to the persistent
console window (see file testecho-messages.py in the examples package):
'''
