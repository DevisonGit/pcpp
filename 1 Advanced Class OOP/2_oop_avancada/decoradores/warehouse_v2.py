def big_container(collective_material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print(f"* The whole order would be packed with", collective_material)
            print()
        return internal_wrapper
    return wrapper


def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print(f"<strong>*</strong> Wrapping items from {our_function.__name__} with {material}")
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper


@big_container('plain cardboard')
@warehouse_decorator('Kraft')
def pack_books(*args):
    print("we'll pack books", args)


@big_container('colourful cardboard')
@warehouse_decorator('foil')
def pack_toys(*args):
    print("we'll pack toys", args)


@big_container('strong cardboard')
@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("we'll pack fruits", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
