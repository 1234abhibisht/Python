# WAP using OOP concepts to model a simple banking system. Create a class BankAccount with attributes
# account holder name, account number, and balance. Include methods to deposit and withdraw money, and
# display the current balace. Use appropriate validation to prevent invalid transitions such as 
# withdrawing more than the available balance. Extend the program by creating a subclass 
# SavingsAccount that adds an interest calculation method. Demostrate the working of the classes with
# suitable examples.

class BankAccount :
    def __init__(self, holderName, accNumber, balance) :
        self.name = holderName
        self.acc = accNumber
        self.__balance = balance
    def withdrawBalance(self) :
        withdrawAmount = int(input("Enter withdraw amount : "))
        if withdrawAmount <= self.__balance :
            print("amount withdrawn successfully")
        else :
            print("insufficient amount")
name_input = input("enter account holder's name : ")
acc_number_input = int(input("enter account number : "))
balace_input = int(input("enter current account balace : "))
a1 = BankAccount(name_input, acc_number_input, balace_input)
a1.withdrawBalance()