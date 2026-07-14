import tkinter as tk
root = tk.Tk()
var = tk.StringVar(root)
var.set("Hello")
print(var.get())
tk.mainloop()