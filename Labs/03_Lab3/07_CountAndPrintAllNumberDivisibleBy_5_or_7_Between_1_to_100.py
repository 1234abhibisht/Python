print("Numbers divisible by 5 and 7 are : ",end="")
for i in range(1,101) :
    if i % 5 == 0 & i % 7 == 0 :
        print(i," ",end="")
        