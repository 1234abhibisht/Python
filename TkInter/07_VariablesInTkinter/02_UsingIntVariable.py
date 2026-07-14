import tkinter as tk
root = tk.Tk()
var = tk.IntVar(root, value = 123)
print(var.get())
tk.mainloop()