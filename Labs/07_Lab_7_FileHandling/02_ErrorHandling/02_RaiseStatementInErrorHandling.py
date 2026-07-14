# raise statement is used to manuall trigger an error
# for this we don't use try: and except:

age = int(input("enter age : "))
if age < 18 :
    raise "age must be > 18"
else :
    print("you are eligible")