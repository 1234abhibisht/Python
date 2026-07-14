from tkinter import *
root = Tk()
var = "Hello"
text_box = Text(root, font = ("Aerial", 40))
text_box.place(x = 600, y = 400, height = 200, width = 500)

# now we want to display hello in textbox widget
text_box.insert(END, var)
# here we use END to insert new text after end of last text
# if text box is empty, it will automatically insert new text in beginning position


# we can also set manual positions in place of END
# "1.0" -> menas 1st line 0th character -> means new text will be inserting from beginning
# "1.5" -> 1st line 5th character -> means new text will be inserting from 5th character of first line
# "2.0" _> 2nd line 0th character
root.mainloop()