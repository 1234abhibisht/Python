class Student :
    def __init__(self, name, marks) :
        self.name = name   # instance variables
        self.marks = marks

    def hello(self) :   
        print("Hello")
    
    def printDetails(self) :
        print(f"Name : {self.name}")
        print(f"Marks : {self.marks}")
        
s1 = Student("Abhishek", 98) 
s1.hello()
print(s1.name)

s2 = Student("Abhinav", 96)
s2.printDetails()
