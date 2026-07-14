# 0 to 3.4 = Fail
# 3.5 to 5.0 = C+
# 5.1 to 6 = B
# 6.1 to 7 = B+
# 7.1 to 8 = A
# 8.1 to 9 = A+
# 9.1 to 10 = O

name = input("Enter your name : ")
rollNumber = int(input("Enter your roll number : "))
sem = int(input("Enter your semester : "))
pds = int(input("Enter PDS marks : "))
python = int(input("Enter python marks : "))
chemistry = int(input("Enter chemistry marks : "))
english = int(input("Enter english marks : "))
physics = int(input("Enter physics marks : "))

percentage = float((pds + python + chemistry + english + physics) / 500 * 100)
cgpa = float(percentage / 10)

grade = 0
if cgpa >= 0 and cgpa <= 3.4 :
    grade = "Fail"
elif cgpa >= 3.5 and cgpa <= 5.0 :
    grade = "C+"
elif cgpa >= 5.1 and cgpa <= 6 :
    grade = "B"
elif cgpa >= 6.1 and cgpa <= 7 :
    grade = "B+"
elif cgpa >= 7.1 and cgpa <= 8 :
    grade = "A"
elif cgpa >= 8.1 and cgpa <= 9 :
    grade = "A+"
elif cgpa >= 9.1 and cgpa <= 10 :
    grade = "O"

print("-----Gradesheet-----")
print("Name :",name)
print("Roll Number :",rollNumber)
print("Sem :",sem)
print("---Subject Marks---")
print("PDS :",pds)
print("Python :",python)
print("Chemistry :",chemistry)
print("English :",english)
print("Physics :",physics)
print("---------------------")
print("Percentage :",percentage)
print("CGPA :",cgpa)
print("Grade :",grade)