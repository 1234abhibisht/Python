# textvariable is used to take input in label in runtime or from the user

user_input = input("Enter text for label : ")
from tkinter import *
root = Tk()
var = StringVar()
lab = Label(root, font = ("Aerial", 30, "bold"), bg = "red", textvariable = var)
var.set(user_input)
lab.pack()
root.mainloop()

# we can also use texvariable to give dynamic names for Button, Checkbutton, LabelFrame widgets