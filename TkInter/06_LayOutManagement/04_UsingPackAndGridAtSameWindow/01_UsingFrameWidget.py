# we can't use pack and grid management together in same window
# but we can do this by using Frame widget
# This will create a seperate environment in same window, where we can now use grid

# always use frames to divide layout window, istead of using grid in one window, it will mess up
# we can also use labelframe to do this thing

from tkinter import *
root = Tk()
root.geometry("400x400")
lab1 = Label(root, text = "hello", font = ("Aerial", 30))
lab1.pack(pady = (30,0))

frame1 = Frame(root)
frame1.pack(pady = (40,0))

lab2 = Label(frame1, text = "hi", font = ("Aerial", 30))  # now this label will go instide frame1 Frame
lab2.grid(row = 0, column = 0)

button1 = Button(frame1, text = "Button", font = ("Aerial", 30))
button1.grid(row = 0, column = 1, padx = (20,0))
root.mainloop()