class Car :
    name = "Toyota"  # if variable is not declared inside constructor function, it is class variable

car1 = Car()
print(car1.name)  # Toyota

car2 = Car()
print(car2.name)  # Toyota

# as class variable is shared to each object, so we can access same name for each object


# but we can change data of name variable for different objects
car3 = Car()
car3.name = "Hundai"
print(car3.name)   # Hundai
# remember data of name variable is changed only for this object, it is not changed permanently in class 
# or for other objects

car4 = Car()
print(car4.name)  # Toyota
# data of name variable for car4 object is still Toyota
# until we manually change it for this particular object
# as name is class variable, it is shared to this object too as Toyota (default data)