# some operators behaves differently for different situations


class Coordinates :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        
    def __add__(self, other) :
        return Coordinates(self.x + other.x, self.y + other.y)   # we have return a new object
    
    def __sub__(self, other) :
        return Coordinates(self.x - other.x, self.y - other.y)
    
    # similarly we can do multiply and divide
    
c1 = Coordinates(10, 20)
c2 = Coordinates(12, 15)
c3 = c1 + c2
c4 = c1 - c2

print(c1.x, c1.y)
print(c2.x, c2.y)
print(c3.x, c3.y)
print(c4.x, c4.y)

# now we want to add x coordinate of c1, c2 and y coordinate of c1, c2
# means we want ans -> 22, 35

# now, we can't directly add two objects
# like -> c1 + c2

# so for this we will use overloading