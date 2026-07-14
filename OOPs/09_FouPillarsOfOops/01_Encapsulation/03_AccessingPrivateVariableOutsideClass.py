# A good example of this private variable is for bank balance systems


class Account :
    def __init__(self, name_input, balance_input):
        self.name = name_input
        self.__balance = balance_input  
        
    # to make this private variable accessible outside this class, we need to use functions
    def get_balance(self) :
        return self.__balance
        
    def deposite_amount(self, amount) :
        self.__balance += amount
        return self.__balance
        
    def withdraw_amount(self, withdraw) :
        if withdraw > self.__balance :  # we are using check for that private variable
            return 0
        remaining = self.__balance - withdraw
        return remaining
        
u1 = Account("Rohan", 100)
print(u1.get_balance())
print(f"Updated balance : {u1.deposite_amount(500)}")
print(f"Remaining balance after withdraw is : {u1.withdraw_amount(300)}")

# but why we need this private variable and functions to access this variable ?
# -> because now we can set some limitations or any check in that function before returning variable
# -> secondly direct access is not there for this variable, and no one can directly update that variable

# so to access this variable, we can use function(methods) inside class and then return desired output




# another good exmple of use of this private variable in email and passwords
# -> as a person can update his/her password but can't look or print it

class Details :
    def __init__(self, username, password) :
        self.username = username
        self.__password = password
        
    def update_password(self, new_password) :
        self.__password = new_password
        return self.__password
     
user1 = Details("a1b2", 123)
print(user1.__password)  # user can't print directly his/her password
print(f"New password : {user1.update_password(456)}")  # but user can update password using function



# getter and setter 
# getter -> all the functions that help to print or access private variable are called getter functions
# setter -> all the functions that help to modify private variable are called getter functions
# basically they are just standard terms 