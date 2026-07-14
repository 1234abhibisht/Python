str = input("Enter a string : ")
sub = input("Enter a substring : ")
count = 0
for i in range(0, len(str) - len(sub) + 1) :
    if(str[i : i + len(sub)] == sub) :
        count += 1
print(count)