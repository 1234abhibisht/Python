class Car :   # first letter of name of class should be in Capital letter
    # variables
    brand = "Toyota"
    wheels = 4
    
    # functions/behaviour
    def accelerate(self) :   # in fuctions inside a class, we must use self
        print("Fast")
    def brake(self) :   # these functions are called methods
        print("brake")
        
# we have created a class Car,it is just a template/blueprint
# now we will create a real object

car1 = Car()  # car1 is the object of class Car, means car1 object can access variables and functions of object
print(car1.brand)
print(car1.wheels)
car1.accelerate()  # we can also access functions inside Car class using this object
                   # note -> use () after funtion to call it
