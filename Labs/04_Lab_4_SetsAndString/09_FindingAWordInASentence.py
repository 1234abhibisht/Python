sentence = input("Enter a sentence : ")
word = input("Enter a word to find : ")
if sentence.find(word) != -1 :
    print(word,"found in string")
else :
    print(word,"not found in string")