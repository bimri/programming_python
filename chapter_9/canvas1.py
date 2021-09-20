"Canvas"
'''
When it comes to graphics, the tkinter Canvas widget is the most free-form device in
the library. It’s a place to draw shapes, move objects dynamically, and place other kinds
of widgets. The canvas is based on a structured graphic object model: everything drawn
on a canvas can be processed as an object. You can get down to the pixel-by-pixel level
in a canvas, but you can also deal in terms of larger objects such as shapes, photos, and
embedded widgets. The net result makes the canvas powerful enough to support
everything from simple paint programs to full-scale visualization and animation.
'''

"demo all basic canvas interfaces"

from tkinter import * 

canvas = Canvas(width=525, height=300, bg='white')          # 0,0 is top left corner
canvas.pack(expand=YES, fill=BOTH)                          # increases down, right

canvas.create_line(100, 100, 200, 200)                      # fromX, fromY, toX, toY
canvas.create_line(100, 200, 200, 300)                      # draw shapes
for i in range(1, 20, 2):
    canvas.create_line(0, i, 50, i)

canvas.create_oval(10, 10, 200, 200, width=2, fill='blue')
canvas.create_arc(200, 200, 300, 100)
canvas.create_rectangle(200, 200, 300, 300, width=5, fill='red')
canvas.create_line(0, 300, 150, 150, width=10, fill='green')

photo=PhotoImage(file=r'C:\Users\avatar\Pictures\gifs\1d021770674669.5bf64572446e1.gif')
canvas.create_image(325, 25, image=photo, anchor=NW)        # embed a photo

widget = Label(canvas, text='Spam', fg='white', bg='black')
widget.pack()
canvas.create_window(100, 100, window=widget)               # embed a widget
canvas.create_text(100, 280, text='Ham')                    # draw some text
mainloop()
