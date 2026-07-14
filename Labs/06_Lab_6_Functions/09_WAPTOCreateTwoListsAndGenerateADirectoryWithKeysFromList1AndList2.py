# 09_WAP TO Create Two Lists And Generate A Directory With Keys From List1 And Values From List2

n1 = int(input("Enter number of elements for list 1 : "))
n2 = int(input("Enter number of elements for list 2 : "))
list1 = []
list2 = []
for i in range(n1) :
    ele1 = int(input("Enter element for list 1 : "))
    list1.append(ele1)

for i in range(n2) :
    ele2 = int(input("Enter element for list 2 : "))
    list2.append(ele2)

# using loops

dict = {}
i = 0
j = 0
while i <= len(list1) - 1 and j <= len(list2) - 1 :
    dict.update({list1[i] : list2[j]})
    i += 1
    j += 1
print(dict)


    