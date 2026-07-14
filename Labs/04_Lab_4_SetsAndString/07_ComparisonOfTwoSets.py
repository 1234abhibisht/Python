    # 7. Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
    # a) Fruits which are in both sets s1 and s2
    # b) Fruits only in s1 but not in s2
    # c) Count of all fruits from s1 and s2
    
st1 = set()
st2 = set()
n1 = int(input("Enter number of fruits for s1 : "))
n2 = int(input("Enter number of fruits for s2 : "))
for i in range(n1) :
    fruit1 = input("Enter fruit : ")
    st1.add(fruit1)
    
for i in range(n2) :
    fruit2 = input("Enter fruit : ")
    st2.add(fruit2)

# a) 
commonFruit = st1.intersection(st2)
print("Common fruit ->",commonFruit)

# b) -> st1 - st2
notCommon = st1 - st2
print("Fruits in st1 but not in st2 ->", notCommon)

# c)
count1 = len(st1)
count2 = len(st2)
totalFruits = count1 + count2
print("Total fruits ->",totalFruits)