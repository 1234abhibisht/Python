# we can do this by height parameter

from tkinter import *
root = Tk()
text_box = Text(root, font = ("Aerial", 40), height = 8)  # now this textbox will store only 8 lines of input
text_box.place(x = 600, y = 400, height = 200, width = 500)
root.mainloop()