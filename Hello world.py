class Student:
    student_count = 0

    def __init__(self, name, student_id, age):
        self.name, self.student_id, self.age = name, student_id, age
        Student.student_count += 1

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.student_id}, Age: {self.age}")

students = [
    Student("Monjurul", 5708, 22),
    Student("Prottoy", 5779, 23)
]

print(f"Number of Students: {Student.student_count}")
print("Student Details:")
for student in students:
    student.display_details()