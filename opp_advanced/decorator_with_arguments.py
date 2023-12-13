class WarehouseDecorator:
    def __init__(self, material) -> None:
        self.material = material

    def __call__(self, own_function):
        def internal_wrapper(*args, **kwargs):
            print("<strong></strong> Wrapping items from {} with {}".format(own_function.__name__, self.material))
            own_function(*args, **kwargs)
            print()
        return internal_wrapper
    

@WarehouseDecorator('Kraft')
def pack_books(*args):
    print("we'll pack books:", args)


@WarehouseDecorator('foil')
def pack_toys(*args):
    print("we'll pack toys:", args)


@WarehouseDecorator('cardboard')
def pack_fruits(*args):
    print("we'll pack fuits:", args)


pack_books("Alice in wonderland", "winnie the pooh")
pack_toys("doll", "car")
pack_fruits('plum', 'pear')
