# we can give value to radio button, so that after selecting it, we can get some output

from tkinter import *
root = Tk()
var = StringVar()
rb = Radiobutton(root, text = "Python", font = (40,), value = "Python is selected", variable = var)
rb.pack()
rb.deselect()  # to deselect Radiobutton initially
print(var.get())
root.mainloop()