from tkinter import *
root = Tk()
def test(var_new_window) :
    print(var_new_window)
    
def new_window() :
    window = Toplevel(root)
    window.title("New Window")
    
    lab = Label(window, text = "new label", font = ("Aerial", 30))
    lab.place(x = 50, y = 90)
    
    # now we want to create a entry box in a new window and reflect it's data in lab Label
    # for this first we need to first create a variable that contains input data of entry variable
    # then we need to pass that variable in a new function to reflect our work
    
    # as our new window is created through a function, and we are using command= parameter to call another function
    # we need to pass that variable as argument manually, using lambda function
    
    # because, now our variable is not a global variable, it is defined in a function of new window, so to 
    # access it in another function, we need to pass it as argument
    
    # but, why we are using lambda function istead of directly passing it as a argument
    # because in command= parameter function is called, to make that button perform a task, without any argument
    # so to make command= parameter call function with argument, it is necessary to use lambda function
    
    
    var_new_window = StringVar()
    
    entry_new_window = Entry(window, font = ("Aerial", 30), bd = 8, textvariable = var_new_window)
    entry_new_window.place(x = 70, y = 20, height = 40, width = 90)
    
    bt_new_window = Button(window, text = "Update", font = ("Aerial", 30), bg = "red", fg = "white", cursor = "hand2", command = lambda: test(var_new_window.get()))
    bt_new_window.place(x = 70, y = 40)
    
bt = Button(root, text = "New Window", font = ("Aerial", 30), bg = "red", fg = "white", cursor = "hand2", command = new_window) 
bt.pack()
root.mainloop()