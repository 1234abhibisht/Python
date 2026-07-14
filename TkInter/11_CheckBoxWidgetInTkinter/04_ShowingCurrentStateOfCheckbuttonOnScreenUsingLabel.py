# Doing same thing in program 03, but showing the state in window, using label

from tkinter import *
def test() :
    lab.config(text = var.get()) 
root = Tk()
var = BooleanVar()
cb = Checkbutton(root, text = "button", font = ("Aerial", 40), variable = var)
cb.pack()

lab = Label(text = "", font = ("Aerial", 30))
lab.pack()

bt = Button(text = "Checkbutton State", font = ("Aerial", 20, "bold"), fg = "red", bg = "yellow", command = test)
bt.pack()

root.mainloop()