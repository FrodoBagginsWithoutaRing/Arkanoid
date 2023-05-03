import tkinter as tk
import random
#.move posun o dany vektor
win = tk.Tk()
w=600
h=500
canvas = tk.Canvas(win,width=w, height=h, bg= "white")
canvas.pack()
d=15
movement=[1*d,1*d]
o=canvas.create_oval(150,150,180,180,fill="green")
#vektor=(1,1)
def shake_that_as_4_ME_X():
    canvas.move(o,random.randint(-1,1),0)
def shake_that_as_4_ME_Y():
    canvas.move(o,0,random.randint(-1,1))
def posuvnik():
    global movement
    canvas.move(o,movement[0],movement[1])
    if canvas.coords(o)[0]<0:
        movement[0] *= (-1)
        shake_that_as_4_ME_Y()
    if canvas.coords(o)[1]<0:
        movement[1] *= (-1)
        shake_that_as_4_ME_X()
    if canvas.coords(o)[2]>w:
        movement[0] *= (-1)
        shake_that_as_4_ME_Y()
    if canvas.coords(o)[3]>h:
        movement[1] *=(-1)
        shake_that_as_4_ME_X()
    canvas.after(100,posuvnik)


posuvnik()
win.mainloop()


