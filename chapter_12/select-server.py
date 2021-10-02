"Multiplexing Servers with select"
'''
Technically, though, threads and processes don’t really run in parallel, unless you’re
lucky enough to have a machine with many CPUs. Instead, your operating system
performs a juggling act—it divides the computer’s processing power among all active
tasks. It runs part of one, then part of another, and so on. All the tasks appear to run
in parallel, but only because the operating system switches focus between tasks so fast
that you don’t usually notice. This process of switching between tasks is sometimes
called time-slicing when done by an operating system; it is more generally known as
multiplexing.
'''

'A select-based echo server'
'''
implements another echo server, one that can handle multiple 
clients without ever starting new processes or threads.
'''


"""
Server: handle multiple clients in parallel with select. use the select
module to manually multiplex among a set of sockets: main sockets which
accept new client connections, and input sockets connected to accepted
clients; select can take an optional 4th arg--0 to poll, n.m to wait n.m
seconds, or omitted to wait till any socket is ready for processing.
"""

import sys, time
from select import select
from socket import socket, AF_INET, SOCK_STREAM
def now(): return time.ctime(time.time())

myHost = ''                                     # server machine, '' means local host
myPort = 50007                                  # listen on a non-reserved port number
if len(sys.argv) == 3:                          # allow host/port as cmdline args too
    myHost, myPort = sys.argv[1:]
numPortSocks = 2                                # number of ports for client connects

# make main sockets for accepting new client requests
mainsocks, readsocks, writesocks = [], [], []
for i in range(numPortSocks):
    portsock = socket(AF_INET, SOCK_STREAM)     # make a TCP/IP socket object
    portsock.bind((myHost, myPort))             # bind it to server port number
    portsock.listen(5)                          # listen, allow 5 pending connects
    mainsocks.append(portsock)                  # add to main list to identify
    readsocks.append(portsock)                  # add to select inputs list
    myPort += 1                                 # bind on consecutive ports

# event loop: listen and multiplex until server process killed
print('select-server loop starting')
while True:
    #print(readsocks)
    readables, writeables, exceptions = select(readsocks, writesocks, [])
    for sockobj in readables:
        if sockobj in mainsocks:                            # for ready input sockets
            # port socket: accept new client
            newsock, address = sockobj.accept()             # accept should not block
            print('Connect:', address, id(newsock))         # newsock is a new socket
            readsocks.append(newsock)                       # add to select list, wait
        else:
            # client socket: read next line
            data = sockobj.recv(1024)                       # recv should not block
            print('\tgot', data, 'on', id(sockobj))
            if not data:                                    # if closed by the clients
                sockobj.close()                             # close here and remv from
                readsocks.remove(sockobj)                   # del list else reselected
            else:
                # this may block: should really select for writes too
                reply = 'Echo=>%s at %s' % (data, now())
                sockobj.send(reply.encode())


'''
Both the accept and recv calls in this code are guaranteed
to not block the server process after select returns; as a result, this server can quickly
get back to the top of the loop to process newly arrived client requests and already
connected clients’ inputs. The net effect is that all new requests and clients are serviced
in pseudoparallel fashion.

To make this process work, the server appends the connected socket for each client to
the readables list passed to select, and simply waits for the socket to show up in the
selected inputs list.
'''
