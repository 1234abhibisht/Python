from tkinter import *
from tkinter import ttk
root = Tk()
lab1 = Label(text = "python", font = ("Aerial", 30))
lab1.pack()

sep = ttk.Separator(root, orient = "horizontal")
sep.pack(fill = X)

lab2 = Label(text = "c++", font = ("Aerial", 30))
lab2.pack()

# we can also set seperator vertically, and also set its side
root.mainloop()