from tkinter import *
from tkinter import ttk
root = Tk()
root.title("To Do Tracker")
root.geometry("600x600+600+200")
root.resizable(False, False)

def open_add_task_window() :
    add_task_window = Toplevel(root)
    add_task_window.geometry("1000x500")
    add_task_window.title("Add Tasks")
    
    labelFrame_add_task_input = LabelFrame(add_task_window, text = "Input: ", font = ("Aerial", 25, "bold"), labelanchor = NW)
    labelFrame_add_task_input.place(x = 20, y = 20, height = 350, width = 700)
    
    # label inside label frame input
    label_add_task_date = Label(labelFrame_add_task_input, text = "Date: ", font = ("Aerial", 25))  # now this label will go inside label frame as a seperate environment that layout window
    label_add_task_date.grid(row = 0, column = 0, padx = (50, 0), pady = (40,0))
    
    label_add_task_task = Label(labelFrame_add_task_input, text = "Task: ", font = ("Aerial", 25))
    label_add_task_task.grid(row = 1, column = 0, padx = (50, 0), pady = (70, 0))
    
    # entry inside label frame 
    entry_add_task_date = Entry(labelFrame_add_task_input, bd = 8)
    entry_add_task_date.grid(row = 0, column = 1, padx = (100, 0), pady = (40, 0), ipadx = 60, ipady = 5)
    format_label = Label(labelFrame_add_task_input, text = "DD-MM-YYYY", font = ("Aerial", 20), bg = "grey")
    format_label.grid(row = 1, column = 0, padx = (100, 0))

main_label = Label(root, text = "To Do Menu", font = ("Aerial", 27, "bold"), bg = "blue", fg = "white")
main_label.pack(pady = (30, 0), ipadx = 70)

# sep1 = ttk.Separator(root, orient = "horizontal")
# sep1.pack(fill = Y)

main_button_add = Button(root, text = "Add Task", font = ("Aerial", 27), relief = "raised", cursor = "hand2", command = open_add_task_window)
main_button_add.pack(pady = (50, 0), ipadx = 50)

main_button_add = Button(root, text = "Delete Task", font = ("Aerial", 27), relief = "raised", cursor = "hand2")
main_button_add.pack(pady = (50, 0), ipadx = 30)

main_button_add = Button(root, text = "Mark Task", font = ("Aerial", 27), relief = "raised", cursor = "hand2")
main_button_add.pack(pady = (50, 0), ipadx = 40)

main_button_add = Button(root, text = "Display Tasks", font = ("Aerial", 27), relief = "raised", cursor = "hand2")
main_button_add.pack(pady = (50, 0), ipadx = 30)



root.mainloop()