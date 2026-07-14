from tkinter import *
root = Tk()
def new_window() :
    window = Toplevel(root)
    window.title("New Window")
bt = Button(text = "New Window", font = ("Aerial", 30), bg = "red", fg = "white", cursor = "hand2", command = new_window)
bt.pack()
root.mainloop()