import tkinter as tk
root = tk.Tk()
var = tk.StringVar(root, value = "Hello")
print(var.get())
tk.mainloop()