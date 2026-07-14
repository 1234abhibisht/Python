from tkinter import *
from tkinter import ttk
root = Tk()
text_box = Text(root, font = ("Aerial", 25))
text_box.place(x = 10, y = 10, height = 300, width = 400)
scroll = Scrollbar(root, orient = "vertical", command = text_box.yview)
scroll.place(x = 430, y = 10, height = 300, width = 20)
# use command = text_box.yview for y axis scrolling
# use command = text_box.xview for x axis scrolling
root.mainloop()