from tkinter import *
f = open("filename.txt","w")
def Write() :
    f.write("Hello")
def Read() :
    data = f.read()
    print(data)
root = Tk()
file_menu = Menu(root)
f_menu = Menu(file_menu)
f_menu.add_command(label = "Write File", command = Write)
f_menu.add_command(label = "Read File", command = Read)

root.config(menu = file_menu)
file_menu.add_cascade(label = "file", menu = f_menu)
root.mainloop()