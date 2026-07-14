    # 1. Add few names, one name in each row, in “name.txt file”.
    #     a. Count no of names
    #     b. Count all names starting with vowel
    #     c. Find longest name
    
f = open("file.txt","w+")
# fileInput = input("Enter few names in different lines : ")
n = int(input("Enter how many names you want to enter : "))
for i in range(n) :
    name = input("Enter name : ")
    f.write(name + "\n")  # concatenating name and \n
f.seek(0) # brings pointer to starting of file, so that f.readlines() can read data
data = f.readlines()
f.close()

# now data = ['name1\n','name2\n','name3\n']

# removing \n from each element string of list

data = [i.strip() for i in data]
# data = ['name1','name2','name3']

# a)
count = len(data)
print(count)

# b)
vowelNameCount = 0
vowels = ('a', 'e', 'i', 'o', 'u')
for i in data :
    i = i.lower()
    if i.startswith(vowels) : 
        vowelNameCount += 1
print(vowelNameCount)

# c)
maxLen = 0
maxName = ""
for i in data :
    if len(i) > maxLen :
        maxLen = len(i)
        maxName = i
print(maxName)
    
