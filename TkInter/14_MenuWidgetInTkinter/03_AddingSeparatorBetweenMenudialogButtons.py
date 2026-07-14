# Menubutton is different from Menu
# here we will make a complete menu

from tkinter import *
root = Tk()
file_menu = Menu(root)
f_menu = Menu(file_menu, tearoff = 0)  # creating a new variable
f_menu.add_command(label = "Open File")
f_menu.add_command(label = "Close File")
f_menu.add_separator()
f_menu.add_command(label = "Save File")
f_menu.add_command(label = "SaveAs File")

# changing menu of our main window
root.config(menu = file_menu)   # we have to change config only one time, to add more options we will just do add_cascade
file_menu.add_cascade(label = "File", menu = f_menu)

# here we don't need to place the menu, as it automatically placed at top left corner


# creating another menu option
f_menu2 = Menu(file_menu, tearoff = 0)
f_menu2.add_command(label = "Copy")
f_menu2.add_command(label = "Cut")
f_menu2.add_separator()
f_menu2.add_command(label = "Paste")
file_menu.add_cascade(label = "Edit", menu = f_menu2)
root.mainloop()