def countDigit(a) :
    count = 0
    while a > 0 :
        a = int(a / 10)
        count = count + 1
    return count

n = int(input("Enter a number : "))
lastdigit = 0
sum = 0
store = n
totalDigits = countDigit(n)
while n > 0 :
    lastdigit = int(n % 10)
    sum = sum + (lastdigit**totalDigits)
    n = int(n / 10)

if (store == sum) :
    print("Armstrong Number")
else :
    print("Not Armstrong Number")
