"""
###########################################################################################
Same as fork-server.py, but use multiprocessing instead of os.fork;
this works on Cygwin, and probably works on other Unix-likes, because 
multiprocessing forks and descriptors are inherited, but it fails on 
Windows (sockets do not pickle correctly as arguments to the Process target), 
and would be very slow in any event (starting a new Python interpreter versus
starting an in-process thread);  I get this in 3.1 on Windows 7:
###########################################################################################
"""

import os, time, sys
from multiprocessing import Process
from socket import *                      # get socket constructor and constants
myHost = ''                               # server machine, '' means local host
myPort = 50007                            # listen on a non-reserved port number

def now():                                       # current time on server
    return time.ctime(time.time())

def handleClient(connection):
    print('Child:', os.getpid())                 # child process: reply, exit
    time.sleep(5)                                # simulate a blocking activity
    while True:                                  # read, write a client socket
        data = connection.recv(1024)             # till eof when socket closed
        if not data: break
        reply = 'Echo=>%s at %s' % (data, now())
        connection.send(reply.encode())
    connection.close()

def dispatcher():                                # listen until process killed
    while True:                                  # wait for next connection,
        connection, address = sockobj.accept()   # pass to process for service
        print('Server connected by', address, end=' ')
        print('at', now())
        Process(target=handleClient, args=(connection,)).start()

if __name__ == '__main__':
    print('Parent:', os.getpid())
    sockobj = socket(AF_INET, SOCK_STREAM)           # make a TCP socket object
    sockobj.bind((myHost, myPort))                   # bind it to server port number
    sockobj.listen(5)                                # allow 5 pending connects
    dispatcher()


'''
multiprocessing has other IPC tools such as its own pipes and
queues that might be used instead of sockets to work around this issue, but clients
would then have to use them, too—the resulting server would not be as broadly accessible
as one based upon general Internet sockets.

Even if multiprocessing did work on Windows, though, its need to start a new Python
interpreter would likely make it much slower than the more traditional technique of
spawning threads to talk to clients.
'''
