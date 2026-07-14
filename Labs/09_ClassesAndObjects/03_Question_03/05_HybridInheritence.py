# any inheritence apart from these are hybrid inheritence

class A :
    def a(self) :
        print("A")

class B(A) :
    def b(self) :
        print("B")

class C(A) :
    def c(self) :
        print("C")
        
class D(C) :
    def d(self) :
        print("D")


# here D is child class of C, but C and B are child class of A
# it is neither multiple inheritence, nor multilevel, nor hierarchical