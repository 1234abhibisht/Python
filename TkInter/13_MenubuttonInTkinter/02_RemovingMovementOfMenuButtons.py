# to remove movement of menu buttons we will use tearoff parameter

from tkinter import *
root = Tk()
root.geometry("600x300")
mb = Menubutton(root, text = "file")
mb.menu = Menu(mb, tearoff = 0)
mb["menu"] = mb.menu
mb.menu.add_checkbutton(label = "New File")
mb.menu.add_checkbutton(label = "Open File")
mb.grid()
root.mainloop()