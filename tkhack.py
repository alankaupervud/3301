import os
import  tkinter
from tkinter import *

def openfile(event):
    os.startfile(r"site.png")

root = Tk()

button = Button(root)
button['text'] = 'PUSH IT'
button.place(x = 70, y = 70)

button.bind("<Button-3>", openfile)

root.mainloop()