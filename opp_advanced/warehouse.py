def warehose_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print("<strong>*</strong> Wrapping items from {} with {}".format(our_function.__name__, material))
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper

@warehose_decorator('kraft')
def pack_books(*args):
    print("we'll pack books:", args)


@warehose_decorator('foil')
def pack_toys(*args):
    print("we'll pack toys:", args)


@warehose_decorator('cardboard')
def pack_fruit(*args):
    print("we'll pack fruits:", args)


pack_books("alice in wonderland", "winnie the pooh")
pack_toys("doll", "car")
pack_fruit("plum", "pear")
