# instead of using different Radiobuttons using different variable, we will use a loop

from tkinter import *
def test() :
    lab.config(text = var.get())
root = Tk()
var = StringVar()
languages = ("Python", "Java", "C++", "C")

# Radiobutton
for i in languages :
    rb = Radiobutton(root, text = i, font = ("Aerial", 40), value = i, variable = var)
    rb.pack()
    rb.deselect()
    print(var.get())
    
# label, where value will get
lab = Label(text = "", font = ("Aerial", 40))
lab.place(x = 400, y = 400)

# Button, after pressing Label will get value of Radiobutton
bt = Button(text = "Radiobutton Value", font = ("Aerial", 30), fg = "red", command = test)
bt.pack()
    
root.mainloop()