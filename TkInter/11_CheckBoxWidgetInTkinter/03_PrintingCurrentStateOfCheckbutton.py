from tkinter import *
def test() :
    print(var.get()) 
root = Tk()
var = BooleanVar()
cb = Checkbutton(root, text = "button", font = ("Aerial", 40), variable = var)
cb.pack()

bt = Button(text = "Checkbutton State", font = ("Aerial", 20, "bold"), fg = "red", bg = "yellow", command = test)
bt.pack()

# this will print the current state of Checkbutton after pressing Button
# -> If Checkbutton in uncheked, then after pressing button it will print False
# -> If Checkbutton in cheked, then after pressing button it will print True
root.mainloop()