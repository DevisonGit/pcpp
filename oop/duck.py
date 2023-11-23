# a class
class Duck:
    def __init__(self, heigth, weight, sex):
        self.height = heigth
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print("Quack")
    
# instances
duckling = Duck(heigth=10, weight=3.4, sex="male")
drake = Duck(heigth=25, weight=3.7, sex="male")
hen = Duck(heigth=20, weight=3.4, sex="female")

# to call a method
duckling.quack()
# to access an attribute 
print(duckling.height)

# type
print(Duck.__class__)
print(duckling.__class__)
print(duckling.sex.__class__)
print(duckling.quack.__class__)
