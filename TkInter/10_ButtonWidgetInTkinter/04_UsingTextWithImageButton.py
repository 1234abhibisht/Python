from tkinter import *
from PIL import Image, ImageTk
root = Tk()
img = Image.open("/home/abhishek-bisht/Downloads/telephone.png")
img = img.resize((300,300))
photo = ImageTk.PhotoImage(img)
bt = Button(root, text = "ImageButton", font = ("Aerial", 40, "bold"), image = photo, compound = "bottom")
bt.place(x = 600, y = 400)
root.mainloop()

