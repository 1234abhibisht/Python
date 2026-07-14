# Write a Python function that takes a positive integer and returns the sum of the cube of all the 
# positive integers smaller than the specified number.

import math
def ansFun(n) :
    sum = 0
    check = 0
    while(check < n) :
        sum = sum + math.pow(check, 3)
        check += 1
    return sum

while(True) : 
    n = int(input("Enter a positive integer : "))
    if(n > 0) :
     break
    else :
        print("Invalid input")
print(ansFun(n))