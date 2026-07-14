# Create a contact book where users can store, search, update, and delete contacts. 
# Use dictionary for storing contacts.

n = int(input("Enter number of contacts you want to store : "))
phoneBook = {}

# storing phone numbers
for i in range(n) :
    name = input("Enter name : ")
    phoneNo = int(input("Enter phone number : "))
    phoneBook.update({name : phoneNo})

while True :
    print("Enter 1 to update phone number")
    print("Enter 2 to enter new name and phone number")
    print("Enter 3 to delete a contact")
    print("Enter 4 to exit phone book")
    ask = int(input("Enter choice : "))

    match ask :
        case 1 : 
            nameInput = input("Enter whose phone number you want to update : ")
            if(nameInput not in phoneBook) :
                print(nameInput, "Do not exists in PhoneBook")
            else :
                newPhone = int(input("Enter new phone number : "))
                phoneBook[nameInput] = newPhone

        case 2 :
            newName = input("Enter a new name : ")
            newPhoneNo = int(input("Enter new phone number : "))
            phoneBook.update({newName : newPhoneNo})
            
        case 3 :
            contactDelete = input("Enter a contact name to delete")
            del phoneBook[contactDelete]
        case 4 :
            print("Your phone book is updated")
            break

print(phoneBook)