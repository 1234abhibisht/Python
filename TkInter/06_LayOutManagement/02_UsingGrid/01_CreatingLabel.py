import tkinter as tk
root = tk.Tk()
lab = tk.Label(root, text="Hello", font=("Time New Roman", 30, "bold"), bg="yellow")
lab.grid(row = 0, column = 0)
root.mainloop()

# how grid works

# by default widget will be placed in row = 0, column = 0, but if row = 0 and column = 0 doesn't have anything
# means that cell of grid is empty and we directy try to add widget in any other cell
# like, if we try to add in row = 0 column = 1, it will still be added to row = 0 column = 0, means it will overlap to it 

# similarly if row = 1 column = 0 is empty,
# and we try to add in row = 2 column = 0, it will still be placed in row = 1 column = 0

# so in this situation we use padding