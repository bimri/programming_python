"Thread Exits and Shared State"
'threads run in parallel within the same process and share global memory'

"""
spawn threads to watch shared global memory change; threads normally exit
when the function they run returns, but _thread.exit() can be called to
exit calling thread; _thread.exit is the same as sys.exit and raising
SystemExit; threads communicate with possibly locked global vars; caveat:
may need to make print/input calls atomic on some platforms--shared stdout;
"""

import _thread as thread
exitstat = 0

def child():
    global exitstat                                 # process global names
    exitstat += 1                                   # shared by all threads
    threadid = thread.get_ident()
    print('Hello from child', threadid, exitstat)
    thread.exit()
    print('Never reached')

def parent():
    while True:
        thread.start_new_thread(child, ())
        if input() == 'q': break
    

if __name__ == '__main__': parent()


'''
On a related note, keep in mind that threads and processes have default lifespan models,
which we explored earlier. By way of review, when child threads are still running, the
two thread modules’ behavior differs—programs on most platforms exit when the parent
thread does under _thread, but not normally under threading unless children are
made daemons. When using processes, children normally outlive their parent. This
different process behavior makes sense if you remember that threads are in-process
function calls, but processes are more independent and autonomous.

When used well, exit status can be used to implement error detection and simple communication
protocols in systems composed of command-line scripts. But having said
that, I should underscore that most scripts do simply fall off the end of the source to
exit, and most thread functions simply return; explicit exit calls are generally employed
for exceptional conditions and in limited contexts only.
'''