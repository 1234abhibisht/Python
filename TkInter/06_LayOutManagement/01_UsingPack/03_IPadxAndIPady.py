import tkinter as tk
root = tk.Tk()
lab = tk.Label(root, text="Hello", font=("Time New Roman", 30, "italic"), bg="yellow")
lab.pack(padx=30, pady=20)
lab.pack(ipadx=40,ipady=20)

# ipadx adds extra pixels to left and right within the widget itself
# similarly ipady adds extra pixels to up and down both

root.mainloop()