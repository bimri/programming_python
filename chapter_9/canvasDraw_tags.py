"Simple Animation Techniques"
"""
add tagged moves with time.sleep (not widget.after or threads);
time.sleep does not block the GUI event loop while pausing, but screen not redrawn
until callback returns or widget.update call; currently running onMove callback has
exclusive attention until it returns: others pause if press 'r' or 'o' during move;
"""

from tkinter import *
import canvasDraw, time


class CanvasEventsDemo(canvasDraw.CanvasEventsDemo):
    def __init__(self, parent=None):
        canvasDraw.CanvasEventsDemo.__init__(self, parent)
        self.canvas.create_text(100, 10, text='Press o and r to move shapes')
        self.canvas.master.bind('<KeyPress-o>', self.onMoveOvals)
        self.canvas.master.bind('<KeyPress-r>', self.onMoveRectangles)
        self.kinds = self.create_oval_tagged, self.create_rectangle_tagged

    def create_oval_tagged(self, x1, y1, x2, y2):
        objectId = self.canvas.create_oval(x1, y1, x2, y2)
        self.canvas.itemconfig(objectId, tag='ovals', fill='blue')
        return objectId

    def create_rectangle_tagged(self, x1, y1, x2, y2):
        objectId = self.canvas.create_rectangle(x1, y1, x2, y2)
        self.canvas.itemconfig(objectId, tag='rectangles', fill='red')
        return objectId
    
    def onMoveOvals(self, event):
        print('moving ovals')
        self.moveInSquares(tag='ovals')                             # move all tagged ovals
    
    def onMoveRectangles(self, event):
        print('moving rectangles')
        self.moveInSquares(tag='rectangles')
    def moveInSquares(self, tag):                                   # 5 reps of 4 times per sec
        for i in range(5):
            for (diffx, diffy) in [(+20, 0), (0, +20), (-20, 0), (0, -20)]:
                self.canvas.move(tag, diffx, diffy)
                self.canvas.update()                                # force screen redraw/update
                time.sleep(0.25)                                    # pause, but don't block GUI


if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()


'''
All three of the scripts in this section create a window of blue ovals and red rectangles
as you drag new shapes out with the left mouse button. The drag-out implementation
itself is inherited from the superclass. A right-mouse-button click still moves a single
shape immediately, and a double-left click still clears the canvas, too—other operations
inherited from the original superclass.
'''

"""
The main drawback of this first approach is that only one animation can be going at
once: if you press “r” or “o” while a move is in progress, the new request puts the prior
movement on hold until it finishes because each move callback handler assumes the
only thread of control while it runs.
"""
