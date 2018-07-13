from Tkinter import *
from PIL import Image, ImageDraw

canvas_width = 300
canvas_height = 300

def clear():
    w.delete("all")
    global img
    img = Image.new('RGB', (canvas_width,canvas_height), 'white')
    global draw
    draw = ImageDraw.Draw(img)

def save():
    filename="utils/temp.jpg"
    img.save(filename)
    master.destroy()

def paint(event):
   x1, y1 = event.x, event.y
   x2, y2 = ( event.x + 20), ( event.y + 20 )
   w.create_oval( x1, y1, x2, y2, fill = "#000000", width=5 )
   draw.ellipse([x1,y1,x2,y2], fill='black')

def get_image():
    global master
    master = Tk()
    master.title( "Handwritten Digit Recognizer" )
    global w
    w = Canvas(master, width=canvas_width, height=canvas_height, bg='white')
    w.pack(expand = YES, fill = BOTH)
    w.bind( "<B1-Motion>", paint )

    global img
    img = Image.new('RGB', (canvas_width,canvas_height), 'white')
    global draw
    draw = ImageDraw.Draw(img)

    message = Label( master, text = "Press and Drag the mouse to draw" )
    message.pack( side = BOTTOM )

    button = Button(master, text='Predict', command=save, anchor = SW)
    button.pack()

    clr = Button(master, text='Clear', command=clear, anchor = NW)
    clr.pack()

    mainloop()
    img.close()

    img = Image.open('utils/temp.jpg')
    img = img.resize((28,28))
    img.save('utils/temp.jpg')
    img.close()
