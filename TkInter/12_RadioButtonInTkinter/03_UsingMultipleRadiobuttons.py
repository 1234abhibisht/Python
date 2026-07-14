from tkinter import *
root = Tk()
var = StringVar()
rb1 = Radiobutton(root, text = "Python", font = (40,), value = "Python is selected", variable = var)
rb1.pack()
rb1.deselect() 

rb2 = Radiobutton(root, text = "Tkinter", font = (40,), value = "Tkinter is selected", variable = var)
rb2.pack()
rb2.deselect() 

# the var contains the data inside value parameter

print(var.get())
root.mainloop()