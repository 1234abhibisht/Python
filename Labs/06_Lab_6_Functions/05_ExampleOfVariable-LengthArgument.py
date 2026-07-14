# sum of numbers using variable-length argument

def sumNumbers(*args) :
    sum = 0
    for i in args :
        sum = sum + i
    return sum
print(sumNumbers(10, 20, 30))
