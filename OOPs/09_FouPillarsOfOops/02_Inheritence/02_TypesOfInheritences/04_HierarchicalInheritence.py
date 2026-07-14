# when multiple child classes inherit one parent class

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
bird1.eat()