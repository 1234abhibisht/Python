import math

principle = float(input("Enter principle : "))
rate = float(input("Enter rate : "))
time = float(input("Enter time in years: "))
SI = (principle * rate * time) / 100
print("Simple interest is : ", SI)

amount = principle * (1 + (rate / 100))**time
CI = amount - principle
print(CI)
