"Output stream buffering: A first look"
'''
By default, standard output is fully buffered when connected to a pipe like this; it’s only
line-buffered when connected to a terminal:
>>> pipe = os.popen('python testexit_os.py')
>>> pipe.read() # streams not flushed on exit
''
>>> pipe = os.popen('python -u testexit_os.py') # force unbuffered streams
>>> pipe.read()
'Bye os world\n'

Confusingly, you can pass mode and buffering argument to specify line buffering in
both os.popen and subprocess.Popen, but this won’t help here—arguments passed to
these tools pertain to the calling process’s input end of the pipe, not to the spawned
program’s output stream:
>>> pipe = os.popen('python testexit_os.py', 'r', 1) # line buffered only
>>> pipe.read() # but my pipe, not program's!
''
>>> from subprocess import Popen, PIPE
>>> pipe = Popen('python testexit_os.py', bufsize=1, stdout=PIPE) # for my pipe
>>> pipe.stdout.read() # doesn't help
b''

Really, buffering mode arguments in these tools pertain to output the caller writes to
a command’s standard input stream, not to output read from that command.
'''
