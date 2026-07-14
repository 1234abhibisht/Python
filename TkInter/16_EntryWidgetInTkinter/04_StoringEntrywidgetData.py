from tkinter import *
def test() :
    lab.config(text = var.get())
root = Tk()
label1 = Label(text = "Email", font = ("Aerial", 30, "bold"))
label1.place(x = 600, y = 300)

var = StringVar()
entry1 = Entry(root, font = (40,), cursor = "plus", bd = 8, textvariable = var)
entry1.place(x = 600, y = 350, height = 40, width = 200)

bt = Button(text = "Click",font = ("Aerial", 30, "bold"), fg = "red", bg = "yellow", command = test)
bt.place(x = 600, y = 400)

lab = Label(text = "", font = ("Aerial", 30, "bold"))
lab.place(x = 600, y = 500)
root.mainloop()