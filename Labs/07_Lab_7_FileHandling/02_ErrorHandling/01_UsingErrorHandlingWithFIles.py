try : 
    with open("file.txt", "r") as f :
        data = f.read()
    print(data)
except FileNotFoundError :
    print("file not found")
except IOError :
    print("error in reading/writing in file")
    