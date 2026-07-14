def pallindrome(string, i, j) :
    if i >= j :
        return True
    if(string[i] != string[j]) :
        return False
    return pallindrome(string, i + 1, j - 1)

string = input("Enter a string : ")
check = pallindrome(string, 0, len(string) - 1)
if check == True :
    print("Pallindrome")
else :
    print("Not Pallindrome")