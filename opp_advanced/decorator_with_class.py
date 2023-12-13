class SimpleDecorator:
    def __init__(self, own_function) -> None:
        self.func = own_function

    def __call__(self, *args, **kwargs):
        print("{} was called with the following arguments".format(self.func.__name__))
        print("\t{}\n\t{}\n".format(args, kwargs))
        self.func(*args, **kwargs)
        print("decotator is still operating")


@SimpleDecorator
def combiner(*args, **kwargs):
    print("\thelllo from the decoreated function, received arguments:", args, kwargs)


combiner('a', 'b', exec='yes')
