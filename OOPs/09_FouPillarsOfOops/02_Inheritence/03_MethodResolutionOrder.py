class Father :
    def drive(self) :
        print("Drive")

class Mother :
    def drive(self) :
        print("Cook")

class Child(Father, Mother) :
    pass
        
# now we have same function name, in both the parent classes

c1 = Child()
c1.drive()  
# now which drive will this Child class access
# wheter it will access from Mother parent class or Father parent class

# for this MRO(Method Resolution Order) is used
# python uses C3 Linearization Algorithm for this MRO

# if we have multiple inheritence, if two parent have same method name in them, then to access that
# method names, as above, python will go from left to right
# -> means, the parent class in left side will be called first, the from right
# -> this pattern is from left -> right

# note -> it doesn't skip any parent, while goind from left -> right
