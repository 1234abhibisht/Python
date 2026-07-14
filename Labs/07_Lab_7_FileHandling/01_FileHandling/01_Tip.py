# instead of using
f = open("filename.txt", "r")

# use 
with open("filename.txt", "r") as f :
    data = f.read()
    

# as using with open("filename.txt", "r") as f :, automatically closes file
# we don't need to manually close file using f.close()