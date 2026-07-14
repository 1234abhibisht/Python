class Area :
    def __init__(self, length_input, breadth_input) :
        self.length = length_input
        self.breadth = breadth_input
    def calculate(self) :
        return self.length * self.breadth
    
r1 = Area(10, 5)
print(r1.calculate())