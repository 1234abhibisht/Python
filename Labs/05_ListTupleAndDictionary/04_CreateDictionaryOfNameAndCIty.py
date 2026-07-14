# Create a dictionary of n persons where key is name and value is city. 
# a) Display all names
# b) Display all city names
# c) Display student name and city of all students.
# d) Count number of students in each city.

name_City = {}
n = int(input("Enter number of entries : "))
for i in range(n) :
    key = input("Enter name : ")
    value = input("Enter city : ")
    name_City.update({key : value})

allNames = list(name_City.keys())
print(allNames)
allCity = list(name_City.values())
print(allCity)

print(name_City)



