# here there is child class which have a parent class, and that parent class also have a parent class
# so that child class can access from its parent class, and also from the parent class of it's parent class


class GrandFather :
    def house(self) :
        print("House")
        
class Father(GrandFather) :
    def car(self) :
        print("Car")
        
class Child(Father) :
    pass

# here Father is parent class of Child, and GrandFather is parent class of Father

c1 = Child()
c1.car()
c1.house()

f1 = Father()
f1.house()

# so Child class can access methods of both Father and GrandFather class
# and Father class can access methods of GrandFather class only