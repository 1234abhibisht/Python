# when a varible is declred inside constructor function, it is instance variable

# unlike class variable where data of a variable was shared to all objects, here data of each instance
# variable for each object is initialized
# means for different objects, we can initialize different data for variables in class

class Student :
    def __init__(self, name_input, rollNo_input) :
        self.name = name_input   
        self.roll = rollNo_input
    # here name_input, rollNo_input are instance variable
    
s1 = Student("abc", 1)  # s1 object will pass to self inside constructor automatically
print(s1.name)
print(s1.roll)

s2 = Student("def", 2)
print(s2.name)
print(s2.roll)
