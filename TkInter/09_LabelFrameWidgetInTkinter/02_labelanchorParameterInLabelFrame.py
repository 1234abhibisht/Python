# labelanchor is used to set position of the name of label in label frame
# by default the position of label name is at north-west, we can set it to North, South, West, East, etc

from tkinter import *
root = Tk()
label_frame = LabelFrame(root, text = "Hello", font = ("Aerial", 30), labelanchor = N)

# -> N = North
# -> S = South
# -> W = West
# -> E = East
# -> NE = NorthEast
# -> NW = NorthWest
# -> SW = SouthWest
# -> EW = EastWest

label_frame.place(x = 600, y = 400, height = 300, width = 500)
root.mainloop()