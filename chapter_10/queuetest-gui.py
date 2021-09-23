"Placing Data on Queues"
'''
Whether your GUIs interface with satellites, websites, or something else, this threadbased
model turns out to be fairly simple in terms of code.

In the context of a GUI, the consumer thread becomes the
GUI itself, and producer threads add data to be displayed to the shared queue as it is
produced. The main GUI thread uses the tkinter after method to check the queue for
results instead of an explicit loop.
'''

# GUI that displays data produced and queued by worker threads

import _thread, queue, time
dataQueue = queue.Queue()                                   # infinite size

def producer(id):
    for i in range(5):
        time.sleep(0.1)
        print('put')
        dataQueue.put('[producer id=%d, count=%d]' % (id, i))
    
def consumer(root):
    try:
        print('get')
        data = dataQueue.get(block=False)
    except queue.Empty:
        pass
    else:
        root.insert('end', 'consumer got => %s\n' % str(data))
        root.see('end')
    root.after(250, lambda: consumer(root))                 # 4 times per sec

def makethreads():
    for i in range(4):
        _thread.start_new_thread(producer, (i,))
    

if __name__ == '__main__':
    # main GUI thread: spawn batch of worker threads on each mouse click
    from tkinter.scrolledtext import ScrolledText
    root = ScrolledText()
    root.pack()
    root.bind('<Button-1>', lambda event: makethreads())
    consumer(root)                                          # start queue check loop in main thread
    root.mainloop()                                         # pop-up window, enter tk event loop


'''
Observe how we fetch one queued data item per timer event here. This is on purpose;
although we could loop through all the data items queued on each timer event, this
might block the GUI indefinitely in pathological cases where many items are queued
quickly (imagine a fast telemetry interface suddenly queueing hundreds or thousands
of results all at once). Processing one item at a time ensures that the GUI will return to
its event loop to update the display and process new user inputs without becoming
blocked. The downside of this approach is that it may take awhile to work through
very many items placed on the queue. Hybrid schemes, such as dispatching at most N
queued items per timer event callback, might be useful in some such scenarios;
'''
