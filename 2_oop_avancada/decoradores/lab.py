from datetime import datetime
import time


def print_timestamp(our_function):
    def internal_wrapper(*args):
        print("Start", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        our_function(*args)
        print("Finish", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return internal_wrapper


@print_timestamp
def add_number(*args):
    total = sum(args)
    print("Total", total)


@print_timestamp
def add_number_sleep(*args):
    total = sum(args)
    time.sleep(5)
    print("Total", total)


add_number(2, 30, 369)
add_number_sleep(5, 3)
