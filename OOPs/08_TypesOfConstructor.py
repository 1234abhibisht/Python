# There are two types of constructors 
# -> default constructor
# -> parametrized constructor

# default constructor
class Student :
    def __init__(self) :
        self.name = "Rohan"
        self.sap = 123
s1 = Student()
# in default constructor we have not passed any argument in constructor


# parametrized constructor
class Student :
    def __init__(self, name_input, sap_input) :
        self.name = name_input
        self.sap = sap_input
s1 = Student("Rohan", 123)
# in parametrized constructor, we have passed arguments to the constructor


# we can use both type of constructors at same time
class Student :
    def __init__(self,  sap_input) :
        self.name = "Rohan"
        self.sap = sap_input
s1 = Student(123)