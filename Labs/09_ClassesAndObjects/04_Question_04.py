# Create a class to implement method Overriding.



class Company :
    def work(self) :
        print("Company work")

class Employee(Company) :
    def work(self) :
        print("Employee work")   # redefines the method work()
        
    def company_work(self) :
        print(super().work())   # this super function will access the method from parent class
    
emp1 = Employee()  # object of child class
emp2 = Company()  # object of parent class

emp1.work()   # output -> Employee work
emp2.work()   # output -> Company work

emp1.company_work()  # accessing the method of parent class 

# so MRO works in method overriding