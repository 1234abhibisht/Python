n = int(input("Enter a number : "))
flag = False
for i in range(2, n) :
    if n % i == 0 :
        flag = True
        break
if n == 1 :
    print(n,"is neither prime nor composite")
elif flag == True :
    print(n, "is composite")
elif flag == False:
    print(n, "is prime")