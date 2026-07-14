import math
r = int(input("Enter radius of cone : "))
h = int(input("Enter height of cone : "))
volume = lambda x, y : (1/3)*math.pi*(x * x)*y
print(volume(r, h))