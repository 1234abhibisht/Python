class Students :
    def __init__(self, name_input, sapid_input, li_marks) :
        self.name = name_input
        self.sap = sapid_input
        dict[self.name] = {}
        dict[self.name]["sap"] = self.sap
        dict[self.name]["marks"] = li_marks
dict = {}
n = int(input("Enter number of students : "))

for i in range(n) :
    li_marks = []
    name_input = input(f"Enter name of {i + 1} student : ")
    sapid_input = input(f"Enter SAP Id of {i + 1} student : ")
    maths = int(input(f"Enter maths marks for {i + 1} student : "))
    physics = int(input(f"Enter physics marks for {i + 1} student : "))
    chemistry = int(input(f"Enter chemistry marks for {i + 1} student : "))
    li_marks.extend([maths, physics, chemistry])
    obj = Students(name_input, sapid_input, li_marks)
    
# a)
print(dict)