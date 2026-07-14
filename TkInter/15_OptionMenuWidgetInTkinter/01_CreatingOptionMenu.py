from tkinter import *
root = Tk()
data = ("Java", "Python", "C++")
var = StringVar()
var.set("Choice")  # to set name for out optionmenu
op = OptionMenu(root, var, *data)
op.pack()
root.mainloop()