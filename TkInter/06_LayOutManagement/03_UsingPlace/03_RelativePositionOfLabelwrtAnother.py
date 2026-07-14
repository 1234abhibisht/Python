import tkinter as tk
root = tk.Tk()
lab = tk.Label(root, text="Hello", font=("Time New Roman", 30, "bold"), bg="yellow")
lab.place(x = 600, y = 400)
lab1 = tk.Label(root, text="World", font=("Time New Roman", 30, "bold"), bg="yellow")
lab1.place(relx = 0.3, rely = 0.2)
tk.mainloop()