from datetime import datetime
from random import choice
from time import sleep


def get_instantiation_time(self):
    return self.instantiation_time


class MyMeta(type):
    instantiated_classes = []

    def __new__(cls, name, bases, dictionary):
        dictionary['get_instantiation_time'] = get_instantiation_time
        obj = super().__new__(cls, name, bases, dictionary)
        return obj

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        cls.instantiated_classes.append(cls.__name__)
        instance.instantiation_time = datetime.now()
        return instance


class LegacyOne(metaclass=MyMeta):
    pass


class LegacyTwo(metaclass=MyMeta):
    pass


class LegacyThree(metaclass=MyMeta):
    pass


legacy = [LegacyOne, LegacyTwo, LegacyThree]
for _ in range(5):
    obj_legacy = choice(legacy)()
    print(obj_legacy.get_instantiation_time())
    sleep(1)

print("List of class legacy", MyMeta.instantiated_classes)
