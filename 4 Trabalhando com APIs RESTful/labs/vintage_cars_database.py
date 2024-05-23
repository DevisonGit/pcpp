import requests
import json

URL = 'http://localhost:3000'
key_names = ['id', 'brand', 'model', 'production_year', 'convertible']
key_width = [10, 20, 10, 20, 15]


def check_server(cid=None):
    try:
        reply = requests.get(URL + '/cars/1', timeout=3)
    except requests.RequestException:
        print("Communication Error")
    else:
        if reply.status_code < 500:
            return True
        else:
            return False


def print_menu():
    menu = 'MENU'
    width = 7
    print_header()
    for letter in menu:
        print(letter, end=' ')
    print()
    print('=' * width)
    print('1. List cars')
    print('2. Add new cars')
    print('3. Delete cars')
    print('4. Update cars')
    print('0. Exit')


def read_user_choice():
    user_choice = input('Enter your choice (0..4): ')
    if user_choice in ['0', '1', '2', '3', '4']:
        return user_choice
    return None


def print_header():
    header = 'Vintage Cars Database'
    width = 30
    print(f'+{"-" * width}+')
    print("|"+header.center(width)+"|")
    print(f'+{"-" * width}+')


def print_car(car):
    for (n, w) in zip(key_names, key_width):
        print(str(car[n]).ljust(w), end='|')
    print()


def list_cars():
    try:
        cars = requests.get(URL + '/cars/')
        if cars.status_code == requests.codes.ok:
            for (n, w) in zip(key_names, key_width):
                print(n.ljust(w), end='|')
            print()
            for car in cars.json():
                print_car(car)
    except requests.RequestException:
        print("Communication Error")


def name_is_valid(name):
    # checks if name (brand or model) is valid;
    # valid name is non-empty string containing
    # digits, letters and spaces;
    # returns True or False;
    if name is not '' and name.isalnum():
        return True
    else:
        return False


def enter_id(car_id):
    try:
        car_id = int(car_id)
    except TypeError:
        car_id = None
    return car_id
    # allows user to enter car's ID and checks if it's valid;
    # valid ID consists of digits only;
    # returns int or None (if user enters an empty line);


def enter_production_year(year):
    try:
        year = int(year)
        if 1900 <= year <= 2000:
            year = None
    except TypeError:
        year = None
    return year
    # allows user to enter car's production year and checks if it's valid;
    # valid production year is an int from range 1900..2000;
    # returns int or None  (if user enters an empty line);


def enter_name(what):
    name = None
    if what == 'brand':
        name = name_is_valid(input('Car brand (empty string to exit): '))
    elif what == 'model':
        name = name_is_valid(input('Car brand (empty string to exit): '))
    return name
    # allows user to enter car's name (brand or model) and checks if it's valid;
    # uses name_is_valid() to check the entered name;
    # returns string or None  (if user enters an empty line);
    # argument describes which of two names is entered currently ('brand' or 'model');


def enter_convertible():
    convertible = None
    input_user = input("Is this car convertible? [y/n] (empty string to exit)")
    if input_user.lower() == 'y':
        convertible = True
    elif input_user.lower() == 'n':
        convertible = False
    return  convertible
    # allows user to enter Yes/No answer determining if the car is convertible;
    # returns True, False or None  (if user enters an empty line);


def delete_car():
    # asks user for car's ID and tries to delete it from database;
    try:
        while True:
            car_id = enter_id(input('Car ID (empty string to exit): '))

            reply = requests.delete('/cars/')
    except TypeError:
        pass


def input_car_data(with_id):
    # lets user enter car data;
    # argument determines if the car's ID is entered (True) or not (False);
    # returns None if user cancels the operation or a dictionary of the following structure:
    # {'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }
    pass


def add_car():
    # invokes input_car_data(True) to gather car's info and adds it to the database;
    pass


def update_car():
    # invokes enter_id() to get car's ID if the ID is present in the database;
    # invokes input_car_data(False) to gather new car's info and updates the database;
    pass


while True:
    if not check_server():
        print("Server is not responding - quitting!")
        exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == '0':
        print("Bye!")
        exit(0)
    elif choice == '1':
        list_cars()
    elif choice == '2':
        add_car()
    elif choice == '3':
        delete_car()
    elif choice == '4':
        update_car()
