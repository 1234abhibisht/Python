from tkinter import *
from PIL import Image, ImageTk
root = Tk()
img = Image.open("/home/abhishek-bisht/Downloads/telephone.png")
img = img.resize((300,300))
photo = ImageTk.PhotoImage(img)
bt = Button(root, image = photo)
bt.place(x = 600, y = 400)

# now this image will work as button

root.mainloop()

