# here one child class inherit with a parent class

class Company :
    def address(self) :
        print("Bangalore")
        
class Employee(Company) :
    def work(self) :
        print("Work")
        
e1 = Employee() 
e1.work()
e1.address() 