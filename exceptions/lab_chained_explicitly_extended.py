class RocketNotReadError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[4])
    except IndexError as e:
        raise RocketNotReadError("Crew is incomplete") from e


def fuel_check():
    try:
        print("Fuel tank is full in {}%".format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadError("Problem with fuel gauge") from e


def batteries_check():
    try:
        print("The batteries are {}%".format(int('90A')))
    except ValueError as e:
        raise RocketNotReadError("Problem with the batteries") from e


def circuits_check():
    try:
        print("The circuits are {}".format())
    except Exception as e:
        raise RocketNotReadError("Problem with the circuits") from e


crew = ['John', "Mary", 'Mike']
fuel = 100
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print("Final check procedure")

for check in check_list:
    try:
        check()
    except RocketNotReadError as f:
        print('General exception "{}", caused by "{}"'.format(f, f.__cause__))
