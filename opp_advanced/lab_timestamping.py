from datetime import datetime

def final_time(collective_material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            timestamp = datetime.now()
            string_timestamp = timestamp.strftime('%Y-%m-%d %H:%m:%S')
            print(collective_material, string_timestamp)
        return internal_wrapper
    return wrapper


def initial_time(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            timestamp = datetime.now()
            string_timestamp = timestamp.strftime('%Y-%m-%d %H:%m:%S')
            print(material, string_timestamp)
            our_function(*args)
        return internal_wrapper
    return wrapper

@final_time('final')
@initial_time('inicio')
def sun_func(*args):
    print(sum(args))

sun_func(5, 5)
