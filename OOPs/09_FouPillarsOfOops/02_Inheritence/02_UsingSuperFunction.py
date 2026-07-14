# if we have a parent class and a child class, now we want to access the instance variable(inside construct)
# of parent class from child class, then we need to use super() function

# means to access methods and constructor variables from parent class in child class

class Company :
    def __init__(self, company_name) :
        self.company_name = company_name
        
    def address(self) :
        print("Bangalore")

class Employee(Company) :
    def __init__(self, emp_name, emp_id, company_name) :
        self.emp_name = emp_name
        self.emp_id = emp_id
        super().__init__(company_name)  # accessed constructor variable in parent class
    def work(self) :
        print("Work")
        
e1 = Employee("xyz", 123, "google")

e1.work()
e1.address()
print(e1.emp_name, e1.emp_id)
print(e1.company_name)



# from super(), one more issue can be resolved, if parent and child has same function name

class Company :
    def __init__(self, company_name) :
        self.companyname = company_name
    def name(self) :
        return self.companyname

class Employee(Company) :
    def __init__(self, emp_name, company_name) :
        self.emp_name = emp_name
        super().__init__(company_name)
        
    def name(self) :
        return self.emp_name
    
    def return_companyname(self) :
        print (super().name())    # here we have accessed name() function from parent class, using super() function
    
e1 = Employee("xyz", "google")
print(e1.name())
e1.return_companyname()