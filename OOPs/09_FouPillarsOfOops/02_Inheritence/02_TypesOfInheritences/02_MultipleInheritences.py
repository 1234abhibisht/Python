# where one single child class inherit with multiple parent class

class Father :
    def drive(self) :
        print("Drive")

class Mother :
    def cook(self) :
        print("Cook")

class Child(Father, Mother) :
    def play(self) :
        print("Play")
        
c1 = Child()
c1.play()
c1.cook()
c1.drive()