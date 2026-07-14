n = int(input("Enter n : "))
a = 1
b = 1
sum = 0
print(a,b, end = " ")
for i in range(1, n - 1) :
    sum = a + b
    a = b
    b = sum
    print(sum, end = " ")