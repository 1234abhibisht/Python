# As textbox widget does not support variable parameter, so we need to store data in a variable  directly

from tkinter import *
def test() :
    var = text_box.get("1.0","end")  # by this way we can store data of textbox in var variable
    lab.config(text = var)
root = Tk()
text_box = Text(root, font = ("Aerial", 40), height = 8)
text_box.place(x = 600, y = 400, height = 200, width = 500)

bt = Button(text = "Click", font = ("Aerial", 30, "bold"), bg = "blue", fg = "white", command = test)
bt.place(x = 600, y = 700)

lab = Label(text = "", font = ("Aerial", 30), bg = "green")
lab.place(x = 600, y = 750)
root.mainloop()
