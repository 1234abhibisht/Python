# method overriding means, if a method is implemented in parent class, then the same method can be used and 
# overridden with new implementation in child class


class Company :
    def work(self) :
        print("Company work")

class Employee(Company) :
    def work(self) :
        print("Employee work")   # redefines the method 'work()'
        
    def company_work(self) :
        print(super().work())   # this super function will access the method from parent class
    
emp1 = Company()  # object of parent class, as the above parent class is not abstract, we can make object of that parent class
emp2 = Employee()  # object of child class
        
emp1.work()   # output -> Company work
emp2.work()   # output -> Employee work   # overridden method 'work()' of parent class

emp2.company_work()  # accessing the method of parent class 

# so MRO works in method overriding