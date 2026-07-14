from tkinter import *
root = Tk()
label1 = Label(text = "Email", font = ("Aerial", 30, "bold"))
label1.place(x = 600, y = 300)

entry1 = Entry(root, font = (40,), cursor = "plus", bd = 8)
entry1.place(x = 600, y = 350, height = 40, width = 200)
root.mainloop()