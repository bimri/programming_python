"Talking to Reserved Ports"
'''
the following client-side code connects
to programs listening on the standard email, FTP, and HTTP web server ports
on three different server machines:
'''

from socket import * 
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('pop.secureserver.net', 100))         # talk to POP email server
print(sock.recv(70))                                # b'+OK <14654.1272040794@p3pop01-09.prod.phx3.gdg>\r\n'
sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('learning-python.com', 21))           # talk to FTP server
print(sock.recv(70))                                # b'220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------\r\n220-You'                                                    
sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('www.python.net', 80))                # talk to Python's HTTP server

sock.send(b'GET /\r\n')                             # fetch root page reply
sock.recv(70)                                       # b'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\r\n "http://'
sock.recv(70)


'''
If we know how to interpret the output returned by these ports’ servers, we could use
raw sockets like this to fetch email, transfer files, and grab web pages and invoke serverside
scripts.
'''


"Binding reserved port servers"
'''
Speaking of reserved ports, it’s all right to open client-side connections on reserved
ports as in the prior section, but you can’t install your own server-side scripts for these
ports unless you have special permission.

[...]$ python
>>> from socket import *
>>> sock = socket(AF_INET, SOCK_STREAM)                 # try to bind web port on general server
>>> sock.bind(('', 80))                                 # learning-python.com is a shared machine
Traceback (most recent call last):
File "<stdin>", line 1, in
File "<string>", line 1, in bind
socket.error: (13, 'Permission denied')

Even if run by a user with the required permission, you’ll get the different exception
we saw earlier if the port is already being used by a real web server. On computers being
used as general servers, these ports really are reserved.

C:\...\PP4E\Internet\Sockets> python
>>> from socket import *
>>> sock = socket(AF_INET, SOCK_STREAM) # can bind port 80 on Windows
>>> sock.bind(('', 80)) # allows running server on localhost
>>>
'''
