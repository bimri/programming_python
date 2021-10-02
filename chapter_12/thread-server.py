"""
Server side: open a socket on a port, listen for a message from a client,
and send an echo reply; echoes lines until eof when client closes socket;
spawns a thread to handle each client connection; threads share global
memory space with main thread; this is more portable than fork: threads
work on standard Windows systems, but process forks do not;
"""

import time, _thread as thread                      # or use threading.Thread().start()
from socket import *                                # get socket constructor and constants
myHost = ''                                         # server machine, '' means local host
myPort = 50007                                      # listen on a non-reserved port number

sockobj = socket(AF_INET, SOCK_STREAM)              # make a TCP socket object
sockobj.bind((myHost, myPort))                      # bind it to server port number
sockobj.listen(5)                                   # allow up to 5 pending connects

def now():
    return time.ctime(time.time())               # current time on the server

def handleClient(connection):                    # in spawned thread: reply
    time.sleep(5)                                # simulate a blocking activity
    while True:                                  # read, write a client socket
        data = connection.recv(1024)
        if not data: break
        reply = 'Echo=>%s at %s' % (data, now())
        connection.send(reply.encode())
    connection.close()

def dispatcher():                                # listen until process killed
    while True:                                  # wait for next connection,
        connection, address = sockobj.accept()   # pass to thread for service
        print('Server connected by', address, end=' ')
        print('at', now())
        thread.start_new_thread(handleClient, (connection,))

dispatcher()


'''
This dispatcher delegates each incoming client connection request to a newly spawned
thread running the handleClient function. As a result, this server can process multiple
clients at once, and the main dispatcher loop can get quickly back to the top to check
for newly arrived requests. The net effect is that new clients won’t be denied service
due to a busy server.
'''

"""
`
Functionally, this version is similar to the fork solution (clients are handled in parallel),
but it will work on any machine that supports threads, including Windows and Linux.
`
"""


'''
Remember that a thread silently exits when the function it is running returns; unlike
the process fork version, we don’t call anything like os._exit in the client handler function
(and we shouldn’t—it may kill all threads in the process, including the main loop
watching for new connections!). Because of this, the thread version is not only more
portable, but also simpler.
'''
