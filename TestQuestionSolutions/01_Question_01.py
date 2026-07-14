# WAP that accepts n integers from user and stores them in a list. From this list, create another
# list conataining only even numbers using list comprehension. Remove duplicate elements from the new
# list and sort in decreasing order. Finally, display maximum and minimum values from sorted list 
# returned from a function

def max_min(li) :
    maxEle = max(li)
    minEle = min(li)
    return maxEle, minEle

n = int(input("Enter number of integers : "))
li1 = []
for i in range(n) :
    ele = int(input("Enter element : "))
    li1.append(ele)
li2 = [i for i in li1 if i % 2 == 0]
li2 = set(li2)  # li2 is converted to a set to remove duplicate elements
sorted(li2, reverse=True)  # set is sorted in decreasing order
li2 = list(li2)  # li2 is converted to list again
a, b = max_min(li2)
print("max element",a,",min element",b)
