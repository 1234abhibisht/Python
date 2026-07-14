from tkinter import *
def change_var(variable) :
    variable = var.get()
    lab.config(text = variable)
    
root = Tk()
data = ("Java", "Python", "C++")
var = StringVar()
var.set("Choice")  # to set name for out optionmenu
op = OptionMenu(root, var, *data, command = change_var)
op.pack()

lab = Label(text = "", font = ("Aerial", 30), bg = "yellow")
lab.pack()
root.mainloop()