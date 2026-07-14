from tkinter import *
root = Tk()

li = ["1\n","2\n","3","4","5"]

text_box = Text(root, font = ("Aerial", 40))
text_box.place(x = 600, y = 400, height = 200, width = 500)

for i in li :
    text_box.insert(END, i)
    
root.mainloop()