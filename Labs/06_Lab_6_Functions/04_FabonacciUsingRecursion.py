def fabonacci(n) :
    if(n == 1 or n == 2) :
        return 1
    return fabonacci(n - 1) + fabonacci(n - 2)

n = int(input("Enter n : "))
for i in range(1, n + 1) :
    print(fabonacci(i),end=" ")