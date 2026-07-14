# WAP that accepts list from user. Use map() with a lambda function to generate new list 
# containing squares of elements. Use filter() with a lambda function to extract numbers greater
# than 20 from the squared list. Define a recursive function to compute the factorial of largest 
# number in filtered list and print it

def factorial(largest) :
    if largest == 1 or largest == 0:
        return 1
    return largest * factorial(largest - 1)

n = int(input("Enter number of elements : "))
li1 = []
for i in range(n) :
    ele = int(input("Enter element : "))
    li1.append(ele)
li2 = map(lambda x : x * x, li1)
li2 = list(li2)  # making li2 a list after doing map
li2 = filter(lambda x : x > 20, li2)
li2 = list(li2)  # making li2 a list again after doing filter
largest = max(li2)
print(factorial(largest))