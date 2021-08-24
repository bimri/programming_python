import os
print('setenv...', end=' ')
print(os.environ['USER'])                           # show current shell variable value

os.environ['USER'] = 'Brian'                        # runs os.putenv behind the scenes
os.system('python echoenv.py')

os.environ['USER'] = 'Arthur'                       # changes passed to spawned programs
os.system('python echoenv.py')                      # and linked-in C library modules

os.environ['USER'] = input('?')
print(os.popen('python echoenv.py').read())


'''
In general terms, a spawned program always
inherits environment settings from its parents. Spawned programs are programs started
with Python tools such as os.spawnv, the os.fork/exec combination on Unix-like platforms,
and os.popen, os.system, and the subprocess module on a variety of platforms.
All programs thus launched get the environment variable settings that exist in the parent
at launch time.

From a larger perspective, setting shell variables like this before starting a new program
is one way to pass information into the new program. For instance, a Python configuration
script might tailor the PYTHONPATH variable to include custom directories just
before launching another Python script; the launched script will have the custom search
path in its sys.path because shell variables are passed down to children
'''
