def simple_hello():
    print("Hello from simple function")


def simple_decorator(function):
    print("we are about to call {}".format(function.__name__))
    return function


decorated = simple_decorator(simple_hello)
decorated()
