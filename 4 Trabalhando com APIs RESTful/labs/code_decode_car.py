import json


dict_types = {
    "registration_number": {"text": "Registration number: ", "type_of_input": str},
    "year_production": {"text": "Year of production: ", "type_of_input": int},
    "passenger": {"text": "Passenger [y/n]: ", "type_of_input": bool},
    "mass": {"text": "Vehicle mass: ", "type_of_input": float}
}


class Vehicle:
    def __init__(self, registration_number, year_production, passenger, mass):
        self.registration_number = registration_number
        self.year_of_production = year_production
        self.passenger = passenger
        self.mass = mass


class MyDecode(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_vehicle)

    def decode_vehicle(self, vehicle):
        return Vehicle(**vehicle)


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def valid_input(text, type_of_input=str):
    user_input = None
    while not isinstance(user_input, type_of_input):
        user_input = input(text)
        if len(user_input) > 0 and type_of_input is not str:
            if is_integer(user_input):
                user_input = int(user_input)
            elif is_float(user_input):
                user_input = float(user_input)
            elif user_input == 'n' and type_of_input is bool:
                user_input = False
            elif user_input == 'y' and type_of_input is bool:
                user_input = True
            else:
                print('Value invalid\n')
        elif len(user_input) == 0:
            user_input = None
            print('Value invalid\n')
    return user_input


def code():
    dict_vehicle = {}
    for k, v in dict_types.items():
        user_input = valid_input(**v)
        dict_vehicle.update({k: user_input})
    vehicle = Vehicle(**dict_vehicle)
    return json.dumps(dict_vehicle)


def decode():
    try:
        vehicle_json = input('Enter vehicle JSON string: ')
        vehicle_decode = json.loads(vehicle_json, cls=MyDecode)
        return vehicle_decode.__dict__
    except TypeError as e:
        return 'Is not Json Vehicle serializable'
    except json.decoder.JSONDecodeError:
        return 'Is not Json Vehicle serializable'


while True:
    print('What can I do for you?')
    print('1 - produce a JSON string describing a vehicle')
    print('2 - decode a JSON string into vehicle data')
    choice = input('Your choice: ')
    if choice in ["1", "2"]:
        if choice == '1':
            result = code()
            print(f"Resulting JSON string is:\n{result}")
        elif choice == '2':
            result = decode()
            print(result)
        break
    print('Choice invalid\n')
