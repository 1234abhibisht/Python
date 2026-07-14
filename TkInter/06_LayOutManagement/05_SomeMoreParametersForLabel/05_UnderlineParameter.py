# used to underline the whole text or a letter of text in label
# it works by index number

# textvariable is used to take input in label in runtime or from the user

import tkinter as tk
root = tk.Tk()
lab = tk.Label(root, text = "Hello", font = ("Aerial Rounded MT Bold", 30, "bold"), bg = "red", underline = 2)
# now the character in second index of text string will be underlined

lab.place(x = 600, y = 400)
root.mainloop()