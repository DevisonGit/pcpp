class WarehouseDecorator:
    def __init__(self, material):
        self.material = material

    def __call__(self, our_function):
        def internal_wrapper(*args, **kwargs):
            print(f"* Wrapping items from {our_function.__name__} with {self.material}")
            our_function(*args, **kwargs)
            print()
        return internal_wrapper


@WarehouseDecorator('Kraft')
def pack_books(*args):
    print("we'll pack books", args)


@WarehouseDecorator('foil')
def pack_toys(*args):
    print("we'll pack toys", args)


@WarehouseDecorator('cardboard')
def pack_fruits(*args):
    print("we'll pack fruits", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
