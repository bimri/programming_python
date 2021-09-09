"multiprocessing pipes"
"""
Use multiprocess anonymous pipes to communicate. Returns 2 connection
object representing ends of the pipe: objects are sent on one end and
received on the other, though pipes are bidirectional by default
"""

import os
from multiprocessing import Process, Pipe

def sender(pipe):
    """
    Send a sequence of strings to the pipe
    """
    pipe.send(['spam'] + [42, 'eggs'])
    pipe.close()

def talker(pipe):
    """
    Receive and print a sequence of objects sent by sender()
    """
    pipe.send(dict(name='Bob', spam=42))
    reply = pipe.recv()
    print('talker got:', reply)



if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    Process(target=sender, args=(child_conn,)).start()      # start sender
    print('parent got:', parent_conn.recv())                # receive from sender
    parent_conn.close()

    parent_conn, child_conn = Pipe()
    child = Process(target=talker, args=(child_conn,))
    child.start()
    print('parent got:', parent_conn.recv())                # receive from child
    parent_conn.send({x * 2 for x in 'spam'})               # send to child
    child.join()                                            # wait for child to finish
    print('parent exit')
