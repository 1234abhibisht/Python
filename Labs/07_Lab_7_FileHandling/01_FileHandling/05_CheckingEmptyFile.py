# we can tell whether file is empty or not using f.see() and f.tell()

import os
f = open("filename.txt","r")

# first bring pointer to end
f.seek(0, os.SEEK_END)

file_size = f.tell()

if file_size == 0 :
    print("File is empty")
else :
    print("File is not empty")