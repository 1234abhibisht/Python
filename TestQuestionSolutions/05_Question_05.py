# Delvelop a modular program using OOP to handle numerical data stored in a file. Create a class that
# reads integers from a file and provides method to find the maximum value, compute the average, and count
# how many numbers are greater than 100. Implement appropriate exception handling to manage error such as
# missing files or invalid data. Demostrate the working of class with suitable input

# here we have a problem -> if integers/digits in file are without space consider them one digit
# and if they have spaces, consider them as seperate digits

class ReadIntegers :
    def __init__(self, filename) : 
        self.filename = filename
    def readFile(self) :
        try : 
            integers = []
            number = ""
            with open(self.filename, "r") as f :
                ch = f.read()
            for i in ch :
                if i.isdigit() == True :
                    number += i
                else :
                    if number != "" :
                        integers.append(int(number))
                    number = ""
            if number != "" :   # if digit is a last position, so after scanning while string, last digit will stay in number, we need to manually store in integer
                integers.append(int(number))
            return integers
        except FileNotFoundError :
            print("file not found")
        except IOError :
            print("error in reading/writing in file")
    def maxValue(self) :
        integers = self.readFile()
        max_int = max(integers)
        print(f"maximum value is {max_int}")
    def average(self) :
        integers = self.readFile()
        averageIntegers = sum(integers) / len(integers)
        print(integers)
        print(f"average of all integers is {averageIntegers}")
    def countGreater100(self) :
        integers = self.readFile()
        count = 0
        for i in integers :
            if i > 100 :
                count += 1
        print(f"Elements greater than 100 are {count}")
    
filename = "integers.txt"
input_data = input("enter input data for file : ")
try : 
    with open(filename, "w") as f :
        f.write(input_data)
except FileNotFoundError :
    print("file not found")
except IOError :
    print("error in reading/writing in file")
f1 = ReadIntegers(filename)
f1.maxValue()
f1.countGreater100()
f1.average()
# print(integers)