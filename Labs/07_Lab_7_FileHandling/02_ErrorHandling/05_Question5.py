# Write a program to create a counter to show that how many times the program is executed.

filename = "counter.txt"
try : 
    f = open(filename,"r")
    count = int(f.read())
except FileNotFoundError :
    print("Error : File not found")
    count = 0
except ValueError :
    print("Error : File is corrupted")
    count = 0
count += 1
try : 
    f = open(filename, "w")
    f.write(str(count))
    print("Program is executed",count,"times")
except IOError :
    print("Error : Can't write in file")
