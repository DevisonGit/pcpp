class Example:
    def __init__(self, internal) -> None:
        self.__internal = internal

    
    def get_internal(self):
        return self.__internal
    

example1 = Example(10)
example2 = Example(99)
print(example1.get_internal())
print(example2.get_internal())

