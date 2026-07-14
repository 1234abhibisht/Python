str = input("Enter a string : ")
resultStr = ""
for char in str : 
    if 'a' <= char <= 'z' :
       resultStr += chr(ord(char) - 32)
    else :
        resultStr += char
print(resultStr)
    