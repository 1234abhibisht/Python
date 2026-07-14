from tkinter import *
root = Tk()
root.geometry("600x300")
mb = Menubutton(root, text = "file")
mb.menu = Menu(mb)
mb["menu"] = mb.menu
mb.menu.add_checkbutton(label = "New File")   # add_checkbutton will add checkbuttons inside menu options
mb.menu.add_checkbutton(label = "Open File")
mb.grid()

# creating another menu button
mb2 = Menubutton(root, text = "view")
mb2.menu = Menu(mb2)
mb2["menu"] = mb2.menu
mb2.menu.add_checkbutton(label = "Front view")
mb2.menu.add_checkbutton(label = "Back view")
mb2.grid(row = 0, column = 1)

root.mainloop()