from collections import namedtuple
b1 = namedtuple("point", ['x', 'y', 'z'])  # defining a namedtuple b1 with name "point" and element names 'x', 'y', 'z'
b1.x = 2
b1.y = 3
print(b1.x)
