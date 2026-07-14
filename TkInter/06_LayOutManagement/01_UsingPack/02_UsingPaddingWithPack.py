from tkinter import *
root = Tk()
lab = Label(root, text="Hello", font=("Time New Roman", 30, "italic"), bg="yellow")
lab.pack(padx=30, pady=20)

# padding adds extra pixels to both up and down if we do padx
# and add extra pixels to left and right both if we do pady
# these extra pixels are added within the cell and outside the widget

root.mainloop()