# as we said, through encapsulation we can restrict access to some components of object,
# or we can say we can restrict attributes(variable) of class

# we can do this by using private variable
# if we want to restrict any variable of class, make that variable private variable
# to make that variable a private variable, use __ (double underscore) before that variable
#  ex -> self.__privateVariable


# private variable is a variable that can be accessible only within the class where it was declared
# and any user can't directly access that variable

class Account :
    def __init__(self, name_input, balance_input):
        self.name = name_input
        self.__balance = balance_input  # now balance has become a private variable, but we can't access it outside class 

u1 = Account("Rohan", "10000")
print(u1.__balance)  # we can't directly print private variable outside class
