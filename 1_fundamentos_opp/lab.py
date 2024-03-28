class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        return f"your age is {self.age} years old"


student = Student(name="Devison", age=36)
print(student.name)
print(student.print_age())
