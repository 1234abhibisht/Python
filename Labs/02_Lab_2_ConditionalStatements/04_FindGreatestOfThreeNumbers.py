# no two numbers are same

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
z = int(input("Enter third number : "))
if (x > y and x > z) :
    print(x, "is greatest")
elif (y > x and y > z) :
    print(y, "is greatest")
elif (z > y and z > x) :
    print(z, "is greatest")
else :
    print("Invalid data")