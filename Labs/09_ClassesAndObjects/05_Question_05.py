# Create a class for operator overloading which adds two Point Objects where Point has x & y values
# e.g. if
# P1(x=10,y=20)
# P2(x=12,y=15)
# P3=P1+P2 => P3(x=22,y=35)

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