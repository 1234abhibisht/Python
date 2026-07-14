import tkinter as tk
root = tk.Tk()
root.geometry("500x500+600+200")
root.config(bg = "red")
lab = tk.Label(root, text="Hello", font=("Aerial Rounded MT Bold", 30,"bold"), bg = "red", cursor = "watch")
lab.pack(padx = 20, pady = 20)
root.mainloop() 

# some more cursors we can user
  # "plus" , "circle"
  # "none" -> for invisible cursor inside label
  # "hand1",  "hand2"  -> for hand cursors
  # "watch"  -> for loading cursor (linux)
  # "wait"  -> for loading cursor (windows)