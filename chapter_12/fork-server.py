"Forking Servers"
# forks a new process to handle each new client connection
'''
Because the handleClient function runs
in a new process, the dispatcher function can immediately resume its main loop in
order to detect and service a new incoming request.
'''

"""
Server side: open a socket on a port, listen for a message from a client,
and send an echo reply; forks a process to handle each client connection;
child processes share parent's socket descriptors; fork is less portable
than threads--not yet on Windows, unless Cygwin or similar installed;
"""

import os, time, sys
from socket import *                        # get socket constructor and constants
myHost = ''                                 # server machine, '' means local host
myPort = 50007                              # listen on a non-reserved port number

sockobj = socket(AF_INET, SOCK_STREAM)      # make a TCP socket object
sockobj.bind((myHost, myPort))              # bind it to server port number
sockobj.listen(5)                           # allow 5 pending connects

def now():                                  # current time on server
    return time.ctime(time.time())

activeChildren = []
def reapChildren():                                 # reap any dead child processes
    while activeChildren:                           # else may fill up system table
        pid, stat = os.waitpid(0, os.WNOHANG)       # don't hang if no child exited
        if not pid: break
        activeChildren.remove(pid)

def handleClient(connection):               # child process: reply, exit
    time.sleep(5)                           # simulate a blocking activity
    while True:                             # read, write a client socket
        data = connection.recv(1024)        # till eof when socket closed
        if not data: break 
        reply = 'Echo=>%s at %s' % (data, now())
        connection.send(reply.encode())
    connection.close()
    os._exit(0)

def dispatcher():                           # listen until process killed
    while True:                             # wait for next connection,
        connection, address = sockobj.accept()              # pass to process for service
        print('Server connected by', address, end=' ')
        print('at', now())
        reapChildren()                      # clean up exited children now
        childPid = os.fork()                # copy this process
        if childPid == 0:                   # if in child process: handle
            handleClient(connection)
        else:                               # else: go accept next connect
            activeChildren.append(childPid) # add to active child pid list

dispatcher()


'''
`Running the forking server`
most of its library calls work only on Unix-like
platforms. Crucially, it runs on Cygwin Python on Windows, but not standard Windows
Python.
'''

"""
clients are serviced at the same time by forked processes, while the main
parent process continues listening for new client requests. If clients were not handled
in parallel like this, no client could connect until the currently connected client’s fivesecond
delay expired.

With process forks per request, clients can be serviced in parallel.

clients simply send and receive data to a machine and
port and don’t care how their requests are handled on the server.
"""

'''
`Forked processes and sockets`
~ Forked processes are essentially a copy of
the process that forks them, and so they inherit file and socket descriptors from their
parent process.

As a result, the new child process that runs the handleClient function
has access to the connection socket created in the parent process. Really, this is why
the child process works at all—when conversing on the connected socket, it’s using
the same socket that parent’s accept call returns. Programs know they are in a forked
child process if the fork call returns 0; otherwise, the original parent process gets back
the new child’s ID.
'''

