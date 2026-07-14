# onvalue parameter is used to get a value when checkbutton is checked
# offvalue parameter is used to get a value when checkbutton is unchecked

from tkinter import *
def test() :
    lab.config(text = var.get()) 
root = Tk()
var = StringVar()
cb = Checkbutton(root, text = "button", font = ("Aerial", 40), onvalue = "Hi", offvalue = "Bye", variable = var)
cb.pack()

lab = Label(text = "", font = ("Aerial", 30))
lab.pack()

bt = Button(text = "Checkbutton State", font = ("Aerial", 20, "bold"), fg = "red", bg = "yellow", command = test)
bt.pack()

root.mainloop()