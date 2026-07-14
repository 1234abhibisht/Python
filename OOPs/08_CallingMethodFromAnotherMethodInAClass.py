class Student :
    def __init__(self, totalMarks) :
        self.marks = totalMarks
    def percentage(self) :
        marks_percentage = (self.marks / 100) * 100
        return marks_percentage
    def result(self) :
        result_marks = self.percentage()   # to call a method use self.method_name()
        if result_marks > 40 :
            print("pass")
        else :
            print("fail")

s1 = Student(50)
s1.result()