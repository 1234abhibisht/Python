# WAP to input a list of scores for N students in a list data type. 
# Find the score of the runner-up and print the output.

# Taking input in list from user
li = []
n = int(input("Enter number of students : "))
for i in range(n) :
    element = int(input(f"Enter score of student {i + 1}: "))
    li.append(element)
    
li.sort()
secondHighest = li[n - 2]
print(secondHighest)

