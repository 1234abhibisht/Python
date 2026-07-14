n = int(input("Enter a number : "))
a = int(input("Enter number of left shifts and right shifts: "))
leftShift = n << a
rightShift = n >> a
print("Left Shift of ",n,"is",leftShift)
print("Right Shift of ",n,"is",rightShift)