# WAP using OOP concepts to define a Student class with attributes name, SAP ID, and marks in Physics,
# Chimistry, and Mathematics. Include a constructor to initialize the data, a method to calculate percentage,
# and a method to display the result as Pass or Fail based on whether the student scores at least 
# 40 marks in each subject. Create two objects of the class and display their details. 
# Also write a seperate function to calculate the average percentage of all students.

class Student :
    def __init__(self, name_input, SAP_input, marks_input) :
        self.name = name_input
        self.SAP = SAP_input
        self.marks = marks_input
    def percentage(self) :
        total_marks = 0
        for i in self.marks:
            total_marks = total_marks + i
        marks_percentage = (total_marks / 300) * 100
        print(f"percentage : {marks_percentage}%")
        return marks_percentage
    def result(self) :
        marks_percentage = self.percentage()
        if int(marks_percentage) > 40 :
            print("pass")
        else :
            print("fail")

nameS1 = input("Enter name of student 1 : ")
sapS1 = input("Enter SAP of student 1 : ")
print("Enter Physics, Maths, Chemistry marks of student 1 : ")
marksS1 = []
for i in range(3) :
    marks_input = int(input("Enter marks : "))
    marksS1.append(marks_input)
s1 = Student(nameS1, sapS1, marksS1)
s1.percentage()
s1.result()

nameS2 = input("Enter name of student 2 : ")
sapS2 = input("Enter SAP of student 2 : ")
print("Enter Physics, Maths, Chemistry marks of student 2 : ")
marksS2 = []
for i in range(3) :
    marks_input = int(input("Enter marks : "))
    marksS2.append(marks_input)
s2 = Student(nameS2, sapS2, marksS2)
s2.percentage()
s2.result()

