"Socket Basics" 
'''
basic socket transfers are remarkably easy to code in Python.

To create a connection between machines,
Python programs import the socket module, create a socket object, and call the object’s
methods to establish connections and send and receive data.

Sockets are inherently bidirectional in nature, and socket object methods map directly
to socket calls in the C library.
'''

"""
Server side: open a TCP/IP socket on a port, listen for a message from
a client, and send an echo reply; this is a simple one-shot listen/reply
conversation per client, but it goes into an infinite loop to listen for
more clients as long as this server script runs; the client may run on
a remote machine, or on same computer if it uses 'localhost' for server
"""

from socket import *                # get socket constructor and constants
myHost = ''                         # '' = all available interfaces on host
myPort = 50007                      # list on a non-reserved port number

sockobj = socket(AF_INET, SOCK_STREAM)          # make a TCP socket object
sockobj.bind((myHost, myPort))                  # bind it to server port number
sockobj.listen(5)                               # list, allow 5 pending connects

while True:                                     # listen until process killed
    connection, address = sockobj.accept()      # wait for next client connect
    print('Server connected by', address)       # connection is a new socket
    while True:
        data = connection.recv(1024)            # read next line on client socket
        if not data: break                      # send a reply line to the client
        connection.send(b'Echo=>' + data)       # until eof when socket closed
    connection.close()


'''
we usually call programs like this that listen for incoming connections
servers because they provide a service that can be accessed at a given machine
and port on the Internet. Programs that connect to such a server to access its service
are generally called clients.
'''

'''
sockobj = socket(AF_INET, SOCK_STREAM)
    AF_INET means the IP address protocol, and 
    SOCK_STREAM means the TCP transfer protocol.

sockobj.bind((myHost, myPort))
    Associates the socket object with an address.
    IP addresses, we pass a server machine name
    and port number on that machine.

In server programs, the hostname is typically an empty string (“”), 
which means the machine that the script runs on and the port
is a number outside the range 0 to 1023.

Note that each unique socket dialog you support must have its own port number;
if you try to open a socket on a port already in use, Python will raise an exception.

sockobj.listen(5)
    Starts listening for incoming client connections 
    and allows for a backlog of up to five pending requests.

connection, address = sockobj.accept()
    Waits for the next client connection request to occur.
    when it does, the accept call returns a brand-new socket 
    object over which data can be transferred from and to
    the connected client.

    Connections are accepted on sockobj, but communication
    with a client happens on connection, the new socket. This call actually returns a
    two-item tuple—address is the connecting client’s Internet address.

    We can call accept more than one time, to service multiple client connections; that’s why each
    call returns a new, distinct socket for talking to a particular client.
'''


"""
Once we have a client connection, we fall into another loop to receive data from the
client in blocks of up to 1,024 bytes at a time, and echo each block back to the client:
    data = connection.recv(1024)
        Reads at most 1,024 more bytes of the next 
        message sent from a client. and returns it 
        to the script as a byte string.
    
    connection.send(b'Echo=>' + data)
        Sends the latest byte string data block 
        back to the client program. 
        The client program can then recv what 
        we send here.
    
    connection.close()
        Shuts down the connection with this 
        particular client.
"""
# sockets by themselves always deal in binary byte strings, not text.
