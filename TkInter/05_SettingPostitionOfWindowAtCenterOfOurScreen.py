import tkinter as tk
root = tk.Tk()
root.title("Window At Centre")

# first find original pixels of your screen
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

# set height and width for window
height = 400
width = 400

centre_x = ((screen_width / 2) - (width / 2))
centre_y = ((screen_height / 2) - (height/ 2))

root.geometry(f"{width}x{height}+{centre_x}+{centre_y}")
root.mainloop()