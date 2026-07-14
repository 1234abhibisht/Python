# Label function do not have control over image size
# so first we need to set size of image, then load in label

from tkinter import *
from PIL import Image, ImageTk
root = Tk()
img = Image.open("/home/abhishek-bisht/Downloads/telephone.png")
img = img.resize((300,300))  # resize image before loading to Label
photo = ImageTk.PhotoImage(img)
lab = Label(root, image = photo)
lab.place(x = 600, y = 400)
root.mainloop()