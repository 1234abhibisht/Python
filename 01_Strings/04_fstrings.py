# keyword argument
age = 20
name = "abc"
print(f"{name} is {age} years old")

# format specifiers
pi = 3.14
print(f"{pi:.2f}")

str = "Hello"
# string truncate
print(f"{str:.3}")


# alignment string
print(f"{str:<10}")  # pad string to left having total padded size 10 -> "Hello       "
print(f"{str:>10}")  # pad string to right having total padded size 10 -> "     Hello"
print(f"{str:^11}")  # pad string to centre having both side spaces with total padded string size 11
print(f"{str:*^10}") # pad string to centre having both side * with total padded string size 11

