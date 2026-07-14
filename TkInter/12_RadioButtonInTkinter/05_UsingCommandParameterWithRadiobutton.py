# we can directly give output to label to show after checking a radio button, instead pressing a button

from tkinter import *
def test() :
    lab.config(text = var.get())
root = Tk()
var = StringVar()
languages = ("Python", "Java", "C++", "C")

# Radiobutton
for i in languages :
    rb = Radiobutton(root, text = i, font = ("Aerial", 40), value = i, variable = var, command = test)
    rb.pack()
    rb.deselect()
    print(var.get())
    
# label, where value will get
lab = Label(text = "", font = ("Aerial", 40))
lab.place(x = 400, y = 400)
    
root.mainloop()