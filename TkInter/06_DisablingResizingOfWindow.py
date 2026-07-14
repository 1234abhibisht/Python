# as we can resize window with our cursor, we can disable it

from tkinter import *
root = Tk()
root.geometry("500x500+600+300")
root.resizable(False, False)   # disabling resizing for x and y axis
root.mainloop()