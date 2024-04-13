class MyMeta(type):
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.custom_attribute = 'Added by MyMeta'
        return obj


class MyObject(metaclass=MyMeta):
    pass


print(MyObject.__dict__)
