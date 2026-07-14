from tkinter import *
from PIL import Image, ImageTk
root = Tk()
img = Image.open("/home/abhishek-bisht/Downloads/telephone.png")
img = img.resize((300,300))  # resize image before loading to Label
photo = ImageTk.PhotoImage(img)
lab = Label(root, image = photo, text = "Phone", font = ("Aerial", 60, "bold"), compound = "left")

# compound = "top" -> brings text to bottom of image
# compound = "bottom" -> brings text to top of image
# compound = "left" -> brings text to right of image
# compound = "right" -> brings text to left of image

lab.place(x = 600, y = 400)
root.mainloop()