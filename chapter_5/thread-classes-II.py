"Other ways to code threads with threading"
'''
The Thread class can also be used to start a simple function, or any other type of callable
object, without coding subclasses at all—if not redefined, the Thread class’s default
run method simply calls whatever you pass to its constructor’s target argument, with
any provided arguments passed to args (which defaults to () for none). This allows us
to use Thread to run simple functions, too, though this call form is not noticeably simpler
than the basic _thread module.
'''
import _thread, threading
def action(i):
    print(i ** 32)


# subclass with state
class MyThread(threading.Thread):
    def __init__(self, i):
        super().__init__()
        self.i = i

    def run(self):                                                  # redefine run()
        print(self.i ** 32)
MyThread(2).start()    


# pass action in
thread = threading.Thread(target=(lambda: action(2)).start())       # callable plus its args

# basic thread module
_thread.start_new_thread(action, (2,))                              # all-function interface


""""
As a rule of thumb, class-based threads may be better if your threads require per-thread
state, or can leverage any of OOP’s many benefits in general. Your thread classes don’t
necessarily have to subclass Thread, though. In fact, just as in the _thread module, the
thread’s target in threading may be any type of callable object. When combined with
techniques such as bound methods and nested scope references, the choice between
coding techniques becomes even less clear-cut:
"""
# a non-thread class with state, OOP
class Power:
    def __init__(self, i):
        self.i = i
    def action(self):
        print(self.i ** 32)
    

obj = Power(2)
threading.Thread(target=obj.action).start()                     # thread runs bound method


# nested scope to retain state
def action(i):
    def power():
        return i ** 32
    return power


threading.Thread(target=action(2)).start()                      # thread runs function returned by action

# both with basic thread module
_thread.start_new_thread(action(2), ())                         # thread runs a callable object
_thread.start_new_thread(action(2), ())
