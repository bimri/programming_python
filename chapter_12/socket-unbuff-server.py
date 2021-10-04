"Line Buffering"
'''
Text-mode socket wrappers also accept a buffering-mode argument of 1 to specify linebuffering
instead of the default full buffering:
>>> from socket import *
>>> s = socket()
>>> f = s.makefile('w', 1) # same as buffering=1, but acts as fully buffered!

This appears to be no different than full buffering, and still requires the resulting file
to be flushed manually to transfer lines as they are produced.
'''

from socket import *           # read three messages over a raw socket
sock = socket()
sock.bind(('', 60000))
sock.listen(5)
print('accepting...')
conn, id = sock.accept()       # blocks till client connect

for i in range(3):
    print('receiving...')
    msg = conn.recv(1024)      # blocks till data received
    print(msg)                 # gets all print lines at once unless flushed
