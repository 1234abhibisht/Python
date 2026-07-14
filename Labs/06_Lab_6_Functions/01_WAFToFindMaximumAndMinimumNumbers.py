def maxNumber(li) :
    minimum = li[0]
    for i in range(1,len(li)) :
        if(li[i] > minimum) :
            minimum = li[i]
    return minimum

def minNumber(li) :
    minimum = li[0]
    if(li[i] < minimum) :
        minimum = li[i]
    return minimum
n = int(input("Enter number of elements : "))
li = []
for i in range(n) :
    numbers = int(input("Enter number : "))
    li.append(numbers)
print("Maximum Number is ->",maxNumber(li))
print("Minimum Number is ->",minNumber(li))
