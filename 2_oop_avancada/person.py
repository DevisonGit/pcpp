class Person:
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary

    def __add__(self, other):
        return self.weight + other.weight


person_1 = Person(30, 40, 50)
person_2 = Person(35, 45, 55)

print(person_1 + person_2)

