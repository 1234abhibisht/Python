from tkinter import *
root = Tk()
label_frame = LabelFrame(root, text = "Hello", font = ("Aerial", 30), labelanchor = N)
label_frame.place(x = 600, y = 400, height = 300, width = 500)

# Label
lab = Label(root, text = "Python", font = ("Aerial", 30, "bold"), bg = "red")
lab.place(x = 650, y = 500)
root.mainloop()