# To load jpg images in label, we need to use PIL(pillow) library
# And not only jpy, we can also add png and gif using PIL library

# so better to you PIL library to import and load images

from tkinter import *
from PIL import Image, ImageTk
root = Tk()
img = Image.open("/home/abhishek-bisht/Downloads/telephone.png")
photo = ImageTk.PhotoImage(img)
lab = Label(root, image = photo)
lab.place(x = 300, y = 200)
root.mainloop()