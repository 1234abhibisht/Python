import math
x = int(input("Enter coeff of x square : "))
y = int(input("Enter coeff of x : "))
z = int(input("Enter constant : "))
root1 = (-y + math.sqrt(y**2 - (4 * x * z))) / 2 * x
root2 = (-y - math.sqrt(y**2 - (4 * x * z))) / 2 * x

print("roots are",root1, root2)