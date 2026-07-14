import tkinter as tk
root = tk.Tk()
lab1 = tk.Label(root, text="Hello", font=("Time New Roman", 30, "bold"), bg="yellow")
lab1.grid(row = 0, column = 0)
lab2 = tk.Label(root, text="Hello", font=("Time New Roman", 30, "bold"), bg="yellow")
lab2.grid(row = 1, column = 0)
root.mainloop()