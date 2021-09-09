"Sockets and independent programs"
'''
Although sockets work for threads, the shared memory model of threads often allows
them to employ simpler communication devices such as shared names and objects and
queues. Sockets tend to shine brighter when used for IPC by separate processes and
independently launched programs.
'''

"""
same socket, but talk between independent programs too, not just threads;
server here runs in a process and serves both process and thread clients;
sockets are machine-global, much like fifos: don't require shared memory
"""

from socket_preview import server, client                   # both use same port number

import sys, os
from threading import Thread

mode = int(sys.argv[1])                                     # run server in this process
if mode == 1:
    server()
elif mode == 2:                                             # run client in this process
    client('client:process=%s' % os.getpid())
elif mode == 3:
    for i in range(5):                                      # run 5 client threads in process
        Thread(target=client, args=('client:thread=%s' % i,)).start()



"""
First, start the server in a process as an independently launched program in
its own window; this process runs perpetually waiting for clients to request connections.
    C:\...\PP4E\System\Processes> socket-preview-progs.py 1

Now, in another window, run a few clients in both processes and thread, by launching
them as independent programs—using 2 as the command-line argument runs a single
client process, but 3 spawns five threads to converse with the server on parallel:

    C:\...\PP4E\System\Processes> socket-preview-progs.py 2

    C:\...\PP4E\System\Processes> socket-preview-progs.py 3
"""
