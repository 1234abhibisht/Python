def recursion(n, a) :
    if a > n :
        return
    print(a)
    recursion(n, a + 1)
    
n = int(input("Enter n : "))
recursion(n, 1)