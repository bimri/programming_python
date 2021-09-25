# GUI server side: read and display non-GUI script's output

import sys, os
from socket import *                                        # including socket.error
from tkinter import Tk
from chapter_5.launchmodes import PortableLauncher
from chapter_10.guiStreams import GuiOutput

myport = 50008
sockobj = socket(AF_INET, SOCK_STREAM)                      # GUI is server, script is client
sockobj.bind(('', myport))                                  # config server before client
sockobj.listen(5)

print('starting')
PortableLauncher('nongui', 'socket-nongui.py -gui')()       # spawn non-GUI script
print('accepting')
conn, addr = sockobj.accept()                               # wait for client to connect
conn.setblocking(False)                                     # use nonblocking socket (False=0)
print('accepted')


def checkdata():
    try:
        message = conn.recv(1024)                   # don't block for input
        #output.write(message + '\n')               # could do sys.stdout=output too
        print(message, file=output)                 # if ready, show text in GUI window
    except error:                                   # raises socket.error if not ready
        print('no data')                            # print to sys.stdout
    root.after(1000, checkdata)                     # check once per second


root = Tk()
output = GuiOutput(root)                            # socket text is displayed on this
checkdata()
root.mainloop()
# conn.close()
# sockobj.close()
# sys.exit(0)


'''
• This example should probably be augmented to detect and handle an end-of-file
signal from the spawned program, and then terminate its timer loop.

• The non-GUI script could also start the GUI instead, but in the socket world, the
server’s end (the GUI) must be configured to accept connections before the client
(the non-GUI) can connect. One way or another, the GUI has to start before the
non-GUI connects to it or the non-GUI script will be denied a connection and
will fail.

• Because of the buffered text nature of the socket.makefile objects used for streams
here, the client program is required to flush its printed output with
sys.stdout.flush to send data to the GUI—without this call, the GUI receives and
displays nothing.
'''
