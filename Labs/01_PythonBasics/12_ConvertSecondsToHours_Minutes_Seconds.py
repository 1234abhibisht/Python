n = int(input("Enter seconds : "))
min = int(n / 60)
sec = n - min * 60
hour = int(min / 60)
min = min - hour * 60
print("hours :",hour," minutes :",min," seconds :",sec)