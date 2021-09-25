"Passing bound method callbacks on queues"
# tests thread callback queue, but uses class bound methods for action and callbacks

import time
from tkinter import EXCEPTION
from threadtools import threadChecker, startThread
from tkinter.scrolledtext import ScrolledText


class MyGui:
    def __init__(self, reps=3):
        self.reps = reps                    # number of times to run the loop; uses default Tk root
        self.text = ScrolledText()          # save widget as state
        self.text.pack()
        threadChecker(self.text)            # start thread to check for errors
        self.text.bind('<Button-1>',        # bind to widget to check for errors
                    lambda event: list(map(self.onEvent, range(6))))
                
    def onEvent(self, i):                   # code that spawns thread
        myname = 'thread=%s' % i 
        startThread(
            action     = self.threadAction,
            args       = (i,),
            context    = self.threadexit,
            onExit     = self.threadfail,
            onProgress = self.threadprogress)
        
    # thread's main action
    def threadAction(self, id, progress):   # what the thread does
        for i in range(self.reps):          # access to object state here
            time.sleep(1)
            if progress: progress(i)        # progress callback: queued
        if id % 2 == 1: raise Exception     # odd numbered: fail
    
    # thread callbacks: dipatch off queue in main thread
    def threadexit(self, myname):
        self.text.insert('end', '%s\texit\n' % myname)
        self.text.see('end')
    
    def threadfail(self, exc_info, myname): # have access to self state
        self.text.insert('end', '%s\tfail\t%s\n' % (myname, exc_info[0]))
        self.text.see('end')
    
    def threadprogress(self, count, myname):
        self.text.insert('end', '%s\tprog\t%s\n' % (myname, count))
        self.text.see('end')
        self.text.update()                  # works here: run in main thread
    

if __name__ == '__main__': MyGui().text.mainloop()


'''
threads all run in the same process and memory space, bound methods reference the
original in-process instance object, not a copy of it. This allows them to update the GUI
and other implementation state directly. Furthermore, because bound methods are
normal objects which pass for callables interchangeably with simple functions, using
them both on queues and in threads this way just works.
'''
