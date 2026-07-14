# Given a string containing both upper and lower case alphabets. 
# Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same.

str = input("Enter a string : ")
n = len(str)
count = 0

countFreq = {}
for i in str :
    i = i.lower()
    if(i in countFreq) :
        countFreq[i] += 1
    else :
        countFreq[i] = 1
print(countFreq)

