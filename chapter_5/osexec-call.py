"os.exec call formats"
'''
The arguments to os.execlp specify the program to be run by giving command-line
arguments used to start the program (i.e., what Python scripts know as sys.argv). If
successful, the new program begins running and the call to os.execlp itself never returns
(since the original program has been replaced, there’s really nothing to return to). If
the call does return, an error has occurred, so we code an assert after it that will always
raise an exception if reached.
'''

"""
There are a handful of os.exec variants in the Python standard library; some allow us
to configure environment variables for the new program, pass command-line arguments
in different forms, and so on. All are available on both Unix and Windows, and
they replace the calling program (i.e., the Python interpreter). exec comes in eight flavors,
which can be a bit confusing unless you generalize:
    os.execv(program, commandlinesequence)
        The basic “v” exec form is passed an executable program’s name, along with a list
        or tuple of command-line argument strings used to run the executable (that is, the
        words you would normally type in a shell to start a program).
    
    os.execl(program, cmdarg1, cmdarg2,... cmdargN)
        The basic “l” exec form is passed an executable’s name, followed by one or more
        command-line arguments passed as individual function arguments. This is the
        same as os.execv(program, (cmdarg1, cmdarg2,...)).
        os.execlp
    
    os.execvp
        Adding the letter p to the execv and execl names means that Python will locate the
        executable’s directory using your system search-path setting (i.e., PATH).
    
    os.execle        
    os.execve
        Adding a letter e to the execv and execl names means an extra, last argument is a
        dictionary containing shell environment variables to send to the program.
        
    os.execvpe
    os.execlpe
        Adding the letters p and e to the basic exec names means to use the search path
        and to accept a shell environment settings dictionary.
"""