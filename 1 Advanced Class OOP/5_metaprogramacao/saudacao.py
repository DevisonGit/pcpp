def greetings(self):
    print("Just a greeting function, but it cloud be something more serious like a check sum")


class MyMeta(type):
    def __new__(cls, name, bases, dictionary):
        if 'greetings' not in dictionary:
            dictionary['greetings'] = greetings
        obj = super().__new__(cls,  name, bases, dictionary)
        return obj


class MyClassOne(metaclass=MyMeta):
    pass


class MyClassTwo(metaclass=MyMeta):
    def greetings(self):
        print("We are ready to great you!")


my_obj1 = MyClassOne()
my_obj1.greetings()

my_obj2 = MyClassTwo()
my_obj2.greetings()
