def fabonacci(n) :
    if n == 1 or n == 2 :
        return 1
    return fabonacci(n - 2) + fabonacci(n - 1)

n = int(input("Enter n : "))
for i in range(1, n + 1) :
    print(fabonacci(i), end=" ")