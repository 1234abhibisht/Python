import tkinter as tk                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
# Function to update expression
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear screen
def clear():
    entry.delete(0, tk.END)

# Function to calculate result
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry box
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]

for (text,row,col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=6, height=2, command=equal)
    elif text == "C":
        btn = tk.Button(root, text=text, width=28, height=2, command=clear)
        btn.grid(row=row, column=col, columnspan=4)
        continue
    else:
        btn = tk.Button(root, text=text, width=6, height=2,
                        command=lambda t=text: click(t))
    
    btn.grid(row=row, column=col)

root.mainloop()