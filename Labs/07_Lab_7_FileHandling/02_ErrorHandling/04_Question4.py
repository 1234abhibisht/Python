# Input two values from user where the first line contains N, the number of test cases. 
# The next N lines contain the space separated values of a and b. 
# Perform integer division and print a/b. 
# Handle exception in case of ZeroDivisionError or ValueError. 

num = input("Enter first number : ")
denom = input("Enter second number : ")
try :
    div = int(num) / int(denom)
    print(div)
except ZeroDivisionError :
    print("Error : Denominator is zero")
except ValueError :
    print("Error : Invalid values entered")
finally :
    print("Program finished")