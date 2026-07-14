# if we want to call a function after checking the Checkbox, we can use command parameter in Checkbox

# using command Button was calling the function after clicking that button

from tkinter import *
def test() :
    lb.config(text = var.get())
root = Tk()
var = StringVar()
cb = Checkbutton(root, text = "CheckIt", font = (40,), onvalue = "Hi", offvalue = "Bye", command = test, variable = var)
cb.pack()
cb.deselect()

lb = Label(text = "Bye", font = ("Aerial", 30))
lb.pack()

# now in label, Bye will be converted to Hi after checking Checkbutton
root.mainloop()