# in tkinter only png, gif images support by default
# to load jpg images use PIL library

from tkinter import *
root = Tk()
photo = PhotoImage(file = "/home/abhishek-bisht/Downloads/telephone.png")
lab = Label(root, image = photo, bg = "red")
lab.place(x = 600, y = 200)
root.mainloop()