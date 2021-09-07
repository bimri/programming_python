"Bidirectional IPC with anonymous pipes"
'''
Pipes normally let data flow in only one direction—one side is input, one is output.
What if you need your programs to talk back and forth, though? For example, one
program might send another a request for information and then wait for that information
to be sent back. A single pipe can’t generally handle such bidirectional conversations,
but two pipes can. One pipe can be used to pass requests to a program and
another can be used to ship replies back to the requestor.

by spawning command-line programs with streams attached by pipes, systems
can add new interfaces to legacy programs.
'''

"""
spawn a child process/program, connect my stdin/stdout to child process's
stdout/stdin--my reads and writes map to output and input streams of the
spawned program; much like tying together streams with subprocess module;
"""

import os, sys

def spawn(prog, *args):                             # pass progname, cmdline args
    stdinFd  = sys.stdin.fileno()                   # get descriptors for streams
    stdoutFd = sys.stdout.fileno()                  # normally stdin=0, stdout=1

    parentStdin, childStdout  = os.pipe()            # make two IPC pipe channels
    childStdin,  parentStdout = os.pipe()            # pipe returns (inputfd, outoutfd)
    pid = os.fork()                                  # make a copy of this process
    if pid:
        os.close(childStdout)                       # in parent process after fork:
        os.close(childStdin)                        # close child ends in parent
        os.dup2(parentStdin,  stdinFd)              # my sys.stdin copy   = pipe1[0]
        os.dup2(parentStdout, stdoutFd)             # my sys.stdout copy  = pipe2[1]
    else:
        os.close(parentStdin)                       # in child process after fork:
        os.close(parentStdout)                      # close parent ends in child
        os.dup2(childStdin,  stdinFd)               # my sys.stdin copy   = pipe2[0]
        os.dup2(childStdout, stdoutFd)              # my sys.stdout copy  = pipe1[1]
        args = (prog,) + args
        os.execvp(prog, args)                       # new program in this process
        assert False, 'execvp failed!'              # os.exec call never returns here
    
if __name__ == '__main__':
    mypid = os.getpid()
    spawn('python', 'pipes-testchild.py', 'spam')     # fork child program
    
    print('Hello 1 from parent', mypid)                 # to child's stdin
    sys.stdout.flush()                                 # subvert stdio buffering
    reply = input()                                    # from child's stdout
    sys.stderr.write('Parent got: "%s"\n' % reply)     # stderr not tied to pipe!
    
    print('Hello 2 from parent', mypid)
    sys.stdout.flush()
    reply = sys.stdin.readline()
    sys.stderr.write('Parent got: "%s"\n' % reply[:-1])


"""
The spawn function in this module does not work on standard Windows Python (remember
that fork isn’t yet available there today).

# Unix concepts
os.fork
    Copies the calling process as usual and returns the child’s process ID in the parent
    process only.
os.execvp
    Overlays a new program in the calling process; it’s just like the os.execlp used
    earlier but takes a tuple or list of command-line argument strings (collected with
    the *args form in the function header).
os.pipe
    Returns a tuple of file descriptors representing the input and output ends of a pipe,
    as in earlier examples.
os.close(fd)
    Closes the descriptor-based file fd.
os.dup2(fd1,fd2)
    Copies all system information associated with the file named by the file descriptor
    fd1 to the file named by fd2.

In terms of connecting standard streams, os.dup2 is the real nitty-gritty here. For example,
the call os.dup2(parentStdin,stdinFd) essentially assigns the parent process’s
stdin file to the input end of one of the two pipes created; all stdin reads will henceforth
come from the pipe.
"""
