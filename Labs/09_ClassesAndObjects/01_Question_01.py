# Create a class of student (name, sap id, marks[phy,chem,maths] ). Create 3 objects by taking inputs 
# from the user and display details of all students.

class Student :
    name = ""
    sapId = -1
    marks = []
    
    def printDetails(self) :
        print(f"Name : {self.name}")
        print(f"sapid : {self.sapId}")
        print(f"marks : {self.marks}")

# object 1      
s1 = Student()
s1_name_input = input("Enter name of first student : ")
s1.name = s1_name_input
s1_sap_input = int(input("Enter sap id of first student : "))
s1.sapId = s1_sap_input
s1_marks_physics_input = int(input("Enter physics marks : "))
s1.marks.append(s1_marks_physics_input)
s1_marks_chemistry_input = int(input("Enter physics marks : "))
s1.marks.append(s1_marks_chemistry_input)
s1_marks_maths_input = int(input("Enter physics marks : "))
s1.marks.append(s1_marks_maths_input)
# details
print("---Student 1---")
s1.printDetails()

# object 2
s2 = Student()
s2_name_input = input("Enter name of second student : ")
s2.name = s2_name_input
s2_sap_input = int(input("Enter sap id of second student : "))
s2.sapId = s2_sap_input
s2_marks_physics_input = int(input("Enter physics marks : "))
s2.marks.append(s2_marks_physics_input)
s2_marks_chemistry_input = int(input("Enter physics marks : "))
s2.marks.append(s2_marks_chemistry_input)
s2_marks_maths_input = int(input("Enter physics marks : "))
s2.marks.append(s2_marks_maths_input)
# details
print("---Student 2---")
s1.printDetails()




