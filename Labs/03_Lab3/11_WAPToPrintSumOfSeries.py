# 1 + 1/2 + 1/3 + 1/4 + ---- 1/n

n = int(input("Enter n : "))
sum = 0
for i in range(1,n + 1) :
    sum = float(sum + 1 / i)
print(sum)