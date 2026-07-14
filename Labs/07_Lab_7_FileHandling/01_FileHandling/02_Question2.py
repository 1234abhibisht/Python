    # 2. Store integers in a file.
    #     a. Find the max number
    #     b. Find average of all numbers
    #     c. Count number of numbers greater than 100
    
f = open("file.txt", "w")
n = int(input("Enter number of integers to be entered: "))
for i in range(n) :
    integer = input("Enter integer : ")
    f.write(integer + "\n")
f.close()
f = open("file.txt", "r") 
data = f.readlines()

# remove \n from each element for list
data = [i.strip() for i in data]

# a)
maxNumber = int(data[0])  # data[0] is a character
for i in range(1, len(data)) :
    if int(data[i]) > maxNumber :
        maxNumber = int(data[i])
print(maxNumber)

# b)
sum = 0
for i in data : 
    sum = sum + int(i)
average = sum / len(data)
print(average)

# c)
count_greater_100 = 0
for i in data :
    if int(i) > 100 :
        count_greater_100 += 1
print(count_greater_100)
