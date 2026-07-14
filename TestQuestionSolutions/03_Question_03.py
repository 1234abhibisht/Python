# WAP that accepts the names of three students and store data in a nested dictionary.
# Names of students must be keys and roll number, age, marks must be values for outer 
# dictionary and keys for nested dictionary. Store their roll number, age and marks of three subjects
# as values inside nested dictionary. Their marks must be stored in a list.
# Display name of student that has obtained highest average and display the names of students
# whose average marks are above 75

def average(dict) :
    maxAvg = 0
    avg_name = ""
    for i in dict :
        avg = sum(dict[i]["marks"]) / len(dict[i]["marks"])
        dict[i]["avg marks"] = avg
        if avg > maxAvg :
            maxAvg = avg
            avg_name += str(i)
    print("Highest average marks are,",maxAvg,"Achieved by",avg_name)
    # print(dict)

studentRecord = {}
n = int(input("Enter number of students : "))
for i in range(n) :
    name = input("Enter name of student : ")
    studentRecord[name] = {}
    rollNumber = int(input("Enter roll number of student : "))
    studentRecord[name]["Roll Number"] = rollNumber
    age = int(input("Enter age of student : "))
    studentRecord[name]["Age"] = age
    studentRecord[name]["marks"] = []
    mathMarks = int(input("Enter marks of maths : "))
    physicsMarks = int(input("Enter marks of physics : "))
    chemistryMarks = int(input("Enter chemistry marks : "))
    studentRecord[name]["marks"].append(mathMarks)
    studentRecord[name]["marks"].append(physicsMarks)
    studentRecord[name]["marks"].append(chemistryMarks)
# print(studentRecord)
average(studentRecord)