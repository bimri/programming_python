"The fork/exec Combination"
'''
child processes simply ran a function within the Python program
and then exited. On Unix-like platforms, forks are often the basis of starting
independently running programs that are completely different from the program that
performed the fork call.
'''

"starts programs until you type 'q'"

import os 

parm = 0
while True:
    parm += 1
    pid = os.fork()
    if pid == 0:                                                        # copy process
        os.execlp('python3', 'python3', 'child.py', str(parm))          # run new program in child
        assert False, 'error starting program'                          # should not return
    else:
        print('Child is', pid)
        if input() == 'q': break


'''
The main thing to notice is the os.execlp call in this code. In a nutshell, this
call replaces (overlays) the program running in the current process with a brand new
program. Because of that, the combination of os.fork and os.execlp means start a new
process and run a new program in that process—in other words, launch a new program
in parallel with the original program.
'''
