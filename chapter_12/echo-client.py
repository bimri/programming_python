"""
Client side: use sockets to send data to the server, and print server's
reply to each message line; 'localhost' means that the server is running
on the same machine as the client, which lets us test client and server
on one machine; to test over the Internet, run a server on a remote
machine, and set serverHost or argv[1] to machine's domain name or IP addr;
Python sockets are a portable BSD socket interface, with object methods
for the standard socket calls available in the system's C library;
"""

import sys 
from socket import *                # portable socket interface plus constants
serverHost = 'localhost'            # server name, or: 'starship.python.net'
serverPort = 50007                  # non-reserved port used by the server

message = [b'Hello network world']          # default text to send to server
                                            # requires bytes: b'' or str, encode()

if len(sys.argv) > 1:
    serverHost = sys.argv[1]                # server from cmd line arg 1
    if len(sys.argv) > 2:                   # text from cmd line args 2..n
        message = (x.encode() for x in sys.argv[2:])
    
sockobj = socket(AF_INET, SOCK_STREAM)      # make a TCP/IP socket object
sockobj.connect((serverHost, serverPort))   # connect to server machine + port

for line in message:
    sockobj.send(line)                      # send line to server over socket
    data = sockobj.recv(1024)               # receive line from server: up to 1k
    print('Client received:', data)         # bytes are quoted, was `x`, repr(x)

sockobj.close()                             # close socket to send eof to server


"""
sockobj = socket(AF_INET, SOCK_STREAM)
    Creates a Python socket object in the client program

sockobj.connect((serverHost, serverPort))
    Opens a connection to the machine and port on which the server program is listening
    for client connections.
"""

'''
Once the client establishes a connection to the server, it falls into a loop, sending a
message one line at a time and printing whatever the server sends back after each line
is sent:

    sockobj.send(line)
        Transfers the next byte-string message line to the server over the socket.

    data = sockobj.recv(1024)
        Reads the next reply line sent by the server program
    
    sockobj.close()
        Closes the connection with the server, sending it the end-of-file signal.
'''

