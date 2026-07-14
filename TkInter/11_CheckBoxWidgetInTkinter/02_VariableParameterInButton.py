# variable connects Checkbutton in tkinter with a variable such as StringVar, IntVar etc,
# it store state of checkbox  
#   -> checked = True or 1
#   -> unchecked = False or 0

from tkinter import *
root = Tk()
var = BooleanVar()
cb = Checkbutton(root, text = "button", font = ("Aerial", 40), variable = var)
cb.pack()
print(var.get())  # This will print current state of Checkbutton i.e False
root.mainloop()