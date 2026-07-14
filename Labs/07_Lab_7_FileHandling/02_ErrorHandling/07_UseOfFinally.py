def addition(a, b) :
    try : 
        sum = a + b
        return sum
    except ValueError :
        print("Error : Invalid values entered")
        return -1
    finally : 
        print("Program has no error")
print(addition(a = 5, b = 10))
