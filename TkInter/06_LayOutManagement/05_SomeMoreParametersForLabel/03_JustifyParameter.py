import tkinter as tk
root = tk.Tk()
root.geometry("500x500+600+200")
root.config(bg = "red")
lab = tk.Label(root, text="Welcome \n to \n Dubai", font=("Aerial Rounded MT Bold", 30,"bold"), bg = "red", justify = "left")
lab.pack(padx = 20, pady = 20)
root.mainloop() 