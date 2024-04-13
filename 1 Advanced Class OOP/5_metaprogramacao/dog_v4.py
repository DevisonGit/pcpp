def bark(self):
    print('woof, woof')


class Animal:
    @staticmethod
    def feed():
        print('It is feeding time')


Dog = type("Dog", (Animal, ), {'age': 0, 'bark': bark})


print("the class name is", Dog.__name__)
print("The class is an instance of", Dog.__class__)
print("The class is based on", Dog.__bases__)
print("The class attributes", Dog.__dict__)

doggy = Dog()
doggy.feed()
doggy.bark()
