"Program Exits"
'sys Module Exits'

import sys
# sys.exit(N)                                     # exit with status N, else exits on end of script
# print('This line will not be printed')


"""
Interestingly, this call really just raises the built-in SystemExit exception. Because of
this, we can catch it as usual to intercept early exits and perform cleanup activities; if
uncaught, the interpreter exits as usual.
"""

try: 
    sys.exit()                                  # see also: os._exit, Tk().quit()
except SystemExit:
    print('ignoring exit')
print('This line will be printed')


'''
Programming tools such as debuggers can make use of this hook to avoid shutting
down. In fact, explicitly raising the built-in SystemExit exception with a Python raise
statement is equivalent to calling sys.exit. More realistically, a try block would catch
the exit exception raised elsewhere in a program
'''
