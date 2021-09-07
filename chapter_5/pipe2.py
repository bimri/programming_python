"Wrapping pipe descriptors in file objects"
# same as pipe1.py, but wrap pipe input in stdio file object
# to read by line, and close unused pipe fds in both processes

import os, time

def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)                                 # make parent wait
        msg = ('Spam %03d\n' % zzz).encode()            # pipes are binary
        os.write(pipeout, msg)                          # send to parent
        zzz = (zzz+1) % 5                               # goto 0 after 4               
    
def parent():
    pipein, pipeout = os.pipe()                         # make two pipes
    if os.fork() == 0:                                  # in child, write to pipe
        os.close(pipein)                                # close input side here
        child(pipeout)                                  # in child, echo output
    
    else:                                               # in parent, listen to pipe
        os.close(pipeout)                               # close output side here
        pipein = os.fdopen(pipein)                      # make text mode input file object
        while True:
            line = pipein.readline()                     # blocks until data sent
            print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))
    
parent()


"""
This version has also been augmented to close the unused end of the pipe in each process
(e.g., after the fork, the parent process closes its copy of the output side of the pipe
written by the child); programs should close unused pipe ends in general.
"""

'''
Notice that this version’s reads also return a text data str object now, per the default
r text mode for os.fdopen. As mentioned, pipes normally deal in binary byte strings
when their descriptors are used directly with os file tools, but wrapping in text-mode
files allows us to use str strings to represent text data instead of bytes. In this example,
bytes are decoded to str when read by the parent; using os.fdopen and text mode in
the child would allow us to avoid its manual encoding call, but the file object would
encode the str data anyhow (though the encoding is trivial for ASCII bytes like those
used here). As for simple files, the best mode for processing pipe data in is determined
by its nature.
'''
