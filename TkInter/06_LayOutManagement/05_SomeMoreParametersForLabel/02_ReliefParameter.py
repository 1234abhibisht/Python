
import tkinter as tk
root = tk.Tk()
root.geometry("500x500+600+200")
root.config(bg = "red")
lab = tk.Label(root, text="Hello", font=("Aerial Rounded MT Bold", 30,"bold"), bg = "red", cursor = "plus", relief = "raised")
lab.pack(padx = 20, pady = 20)
root.mainloop() 

# some more relief parameters
    # "raised" -> for raised label
    # "sunken" -> pressed label
    # "groove"
    # "ridge" -> raised border with edges
    # "solid" -> simple solid border 