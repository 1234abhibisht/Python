# Scan n values in range 0-3 and print the number of times each value has occurred.

li = [1,2,0,0,2,3,1,3,1,2]
dict = {}
for i in li :
    for i in dict :
        dict[i] += 1
    else :
        dict[i] = 1
print(dict)
