# for this we will use fg parameter
from tkinter import *
root = Tk()
bt = Button(root, text = "ON", font = ("Aerial", 40, "bold"), relief = "raised", fg = "red", bg = "black")
bt.place(x = 600, y = 400)
root.mainloop()

# we can use all parameters used in label in this Button widget