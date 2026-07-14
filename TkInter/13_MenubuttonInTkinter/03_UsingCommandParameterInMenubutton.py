from tkinter import *
def test() :
    lab.config(text = "File Opened")
root = Tk()
root.geometry("600x300")
mb = Menubutton(root, text = "file")
mb.menu = Menu(mb)
mb["menu"] = mb.menu
mb.menu.add_checkbutton(label = "Open File", command = test)
mb.grid()

lab = Label(root, text = "", font = ("Aerial", 30), bg = "yellow")
lab.grid()
root.mainloop()