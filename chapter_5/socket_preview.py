"""
sockets for cross-task communication: start threads to communicate over sockets;
independent programs can too, because sockets are system-wide, much like fifos;
see the GUI and Internet parts of the book for more realistic socket use cases;
some socket servers may also need to talk to clients in threads or processes;
sockets pass byte strings, but can be pickled objects or encoded Unicode text;
caveat: prints in threads may need to be synchronized if their output overlaps;
"""

from socket import socket, AF_INET, SOCK_STREAM                     # portable socket api

port = 50008                                                        # poer number identifies socket on machine
host = 'localhost'                                                  # machine name or IP address;  bind to port on this machine


def server():
    sock = socket(AF_INET, SOCK_STREAM)                              # create a socket; ip addresses tcp connection
    sock.bind((host, port))                                          # bind socket to port on this machine
    sock.listen(5)                                                   # listen for incoming connections
    while True:
        conn, addr = sock.accept()                                   # accept connection from client
        data = conn.recv(1024)                                       # receive bytes data from this client
        reply = 'server got: [%s]' % data                            # reply to client; conn is a new connected socket
        conn.send(reply.encode())                                    # send bytes reply to client
    

def client(name):
    sock = socket(AF_INET, SOCK_STREAM)                              # create a socket
    sock.connect((host, port))                                       # connect to server
    sock.send(('Hello, %s' % name).encode())                         # send bytes data to server
    reply = sock.recv(1024)                                          # receive bytes data from server    
    sock.close()                                                     # close socket
    print('client got: [%s]' % reply.decode())                       # print decoded bytes data from server



if __name__ == '__main__':
    from threading import Thread
    sthread = Thread(target=server)                                  
    sthread.daemon = True                                            # don't wait for server thread
    sthread.start()                                                  # do wait for children to exit
    for i in range(5):
        Thread(target=client, args=('client%s' % i,)).start()


"""
Once connected, the client and server transfer byte strings by
using send and receive calls instead of writes and reads.
"""
