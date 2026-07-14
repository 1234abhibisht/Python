# sometimes after running program, initially the checkbutton is checked
# we can make it unchecked initially using deselect() function
# Note -> use deselect() function after placing the Checkbutton (means after, pack(), place(), grid())

from tkinter import *
def test() :
    lab.config(text = var.get()) 
root = Tk()
var = StringVar()
cb = Checkbutton(root, text = "button", font = ("Aerial", 40), onvalue = "Hi", offvalue = "Bye", variable = var)
cb.pack()
cb.deselect()   # deselected checkbox initially

lab = Label(text = "", font = ("Aerial", 30))
lab.pack()

bt = Button(text = "Checkbutton State", font = ("Aerial", 20, "bold"), fg = "red", bg = "yellow", command = test)
bt.pack()

root.mainloop()