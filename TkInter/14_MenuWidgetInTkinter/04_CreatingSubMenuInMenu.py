# Menubutton is different from Menu
# here we will make a complete menu

from tkinter import *
root = Tk()
file_menu = Menu(root)
f_menu = Menu(file_menu, tearoff = 0)  # creating a new variable
f_menu.add_command(label = "Open File")
f_menu.add_command(label = "Close File")
f_menu.add_separator()
# f_menu.add_command(label = "Save File"), we will make a sub menu inside this Save File
f_menu.add_command(label = "SaveAs File")

# creating sub menu
sub_menu = Menu(f_menu)
sub_menu.add_command(label = "Red")
sub_menu.add_command(label = "Yellow")
f_menu.add_cascade(label = "Save File", menu = sub_menu)

# changing menu of our main window
root.config(menu = file_menu)   
file_menu.add_cascade(label = "File", menu = f_menu)

root.mainloop()