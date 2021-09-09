"Sockets: A First Look"
'''
Sockets, implemented by the Python socket module, are a more general IPC device
than the pipes we’ve seen so far. Sockets let us transfer data between programs running
on the same computer, as well as programs located on remote networked machines.
When used as an IPC mechanism on the same machine, programs connect to sockets
by a machine-global port number and transfer data. When used as a networking connection,
programs provide both a machine name and port number to transfer data to
a remotely-running program.
'''


'Socket basics'
'''
Although sockets are one of the most commonly used IPC tools, it’s impossible to fully
grasp their API without also seeing its role in networking.

    • Like fifos, sockets are global across a machine; they do not require shared memory
    among threads or processes, and are thus applicable to independent programs.
    
     • Unlike fifos, sockets are identified by port number, not filesystem path name; they
    employ a very different nonfile API, though they can be wrapped in a file-like object;
    and they are more portable: they work on nearly every Python platform, including
    standard Windows Python.
'''