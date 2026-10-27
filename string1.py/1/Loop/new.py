class Student:
    clg_name = "abc college"
    def __init__(self,fullname,marks):
        self.anything = fullname
        self.marks = marks
        print("here you will find name ")

s1 = Student("prottoy",97)
print(s1.anything,s1.marks)
print(s1.clg_name)

s2 = Student("mahir",98)
print(s2.anything,s1.marks)

print(s2.clg_name)