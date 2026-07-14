# it is the process of hiding implementation process from user and showing only essential functionality

# ex - in atm, when we withdraw money, we only see balance, transitions, etc
#      but, we don't see backend processes, network calls, etc


# we can make a abstract class
# to this use (ABC) -> Abstract Base Class in bracket with the class which we want to make abstract class
# and use @abstractmethod inside that abstract class


# why to use abstract class ?
# -> if we want a method to guaranteed implement in all the child classes of that parent class
#    then we will make that parent class abstract
#    -> this is the rule

from abc import ABC, abstractmethod
class Shape(ABC) :
    @abstractmethod
    def area(self) :
        pass
class rectangle(Shape) :
    def __init__(self, length, breadth) :
        self.length = length
        self.breadth = breadth
    def area(self) :
        area_rectange = self.length * self.breadth
        print(f"area of rectange is {area_rectange}")

s1 = rectangle(10,20)
s1.area()