# Command parameter calls the function, for the working of our button

# Ex -> if we have a label named hello, and we want to make it change to python after clicking button

from tkinter import *
def python() :
    lb.config(text = "Python")
root = Tk()
lb = Label(text = "Hello", font = ("Aerial", 30), bg = "green")
lb.place(x = 600, y = 300)

bt = Button(text = "ON", font = ("Aerial", 30), fg = "red", bg = "yellow", command = python)
# we are calling the function in command parameter, but don't use () for calling

bt.place(x = 600, y = 400)
root.mainloop()