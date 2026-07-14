# it is a mechanism where a child class can aquire the properties and methods from a parent class

# code reusability
# better organisation
# reduce duplicacy

# note ->  parent class is also known as base class
#      ->  child class is also known as derived class



class Bird :
    def eat(self) :
        print("Eat") 
    def fly(self) :
        print("Fly")

class Dog :
    def eat(self) :
        print("Eat")
    def run(self) :
        print("Run")

class Fish :
    def eat(self) :
        print("Eat")
    def swim(self) :
        print("Swim")
        
# now there is major problem, 
# def eat(self) :
#   print("Eat")
# the above function or code is repeating in each class, so there is duplicacy

# so to solve above problem, we will use inheritence


class Animal :
    def eat(self) :
        print("Eat")
        
class Bird(Animal) :   # now this class will inherit the properties of Animal class
    def fly(self) :
        print("Fly")

class Dog(Animal) :
    def run(self) :
        print("Run")

class Fish(Animal) :
    def swim(self) :
        print("Swim")

bird1 = Bird()
bird1.fly()
bird1.eat()   # as now, this object is also accessing from Animal class