class RocketNotReadyError(Exception):
    pass


def personal_check():
    try:
        for i in range(len(role)):
            print(f"The {crew[i]}'s name is {role[i]}")
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
    try:
        print(f"The tank is full in {100 / 0}%")
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with the fuel') from e


def batteries_check():
    try:
        print(f"The battery charge in {100 / 0}")
    except ZeroDivisionError as e:
        raise RocketNotReadyError("Problem with the batteries") from e


def circuits_check():
    try:
        print(f"Circuits{int('a')}")
    except ValueError as e:
        raise RocketNotReadyError("Problem with the circuits") from e


role = ['captain', 'pilot', 'mechanic', 'navigator']
crew = ['John', 'Mary', 'Mike']
circuits = [True, False]
check_list = [personal_check, fuel_check, batteries_check, circuits_check]

print("Final check procedure")

for check in check_list:
    try:
        check()
    except RocketNotReadyError as err:
        print(f'General exception: {err} caused by "{err.__cause__}"')
