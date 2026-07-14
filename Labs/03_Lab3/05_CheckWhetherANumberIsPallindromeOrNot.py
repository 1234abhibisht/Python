n = int(input("Enter a number : "))
lastdigit = 0
newNum = 0
store = n
while n > 0 :
    lastdigit = int(n % 10)
    newNum = (newNum*10) + lastdigit
    n = int(n / 10)
if newNum == store :
    print("Pallindrome")
else :
    print("Not Pallindrome")
    