class Account :
    def __init__(self, acc_name, acc_balance) :
        self.name = acc_name
        self.__balance = acc_balance

    @property   # now this function will act as a variable
    def display(self) :
        return self.__balance
    
 
    def update(self, new_balance) :
        self.__balance += new_balance
        return self.__balance
    
a1 = Account("abc", 100)
print(a1.display)   # we don't need to add () after a1.display

n = int(input("Enter amount to add : "))
updated = a1.update(n)
print(f"New balance : {updated}")