from Tkinter import *
from PIL import Image, ImageDraw

class canvasUI(object):
    def __init__(self):
        self.master = Tk()
        self.canvas_width = 300
        self.canvas_height = 300
        self.win = None
        self.img = None
        self.draw = None
        self.initCanvas()
    def initCanvas(self):
        self.master.title( "Handwritten Digit Recognizer" )
        self.win = Canvas(self.master, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.win.pack(expand = YES, fill = BOTH)
        self.win.bind( "<B1-Motion>", self.paint )

        self.img = Image.new('RGB', (self.canvas_width, self.canvas_height), 'white')
        self.draw = ImageDraw.Draw(self.img)

        message = Label( self.master, text = "Press and Drag the mouse to draw" )
        message.pack( side = BOTTOM )

        button = Button(self.master, text='Predict', command=self.save, anchor = SW)
        button.pack()

        clr = Button(self.master, text='Clear', command=self.clear, anchor = NW)
        clr.pack()

        mainloop()
        self.img.close()

        img = Image.open('utils/temp.jpg')
        img = img.resize((28,28))
        img.save('utils/temp.jpg')
        img.close()

    def clear(self):
        self.win.delete("all")
        self.img = Image.new('RGB', (self.canvas_width, self.canvas_height), 'white')
        self.draw = ImageDraw.Draw(img)

    def save(self):
        filename="utils/temp.jpg"
        self.img.save(filename)
        self.master.destroy()

    def paint(self, event):
        x1, y1 = event.x, event.y
        x2, y2 = ( event.x + 20), ( event.y + 20 )
        self.win.create_oval( x1, y1, x2, y2, fill = "#000000", width=5 )
        self.draw.ellipse([x1,y1,x2,y2], fill='black')
