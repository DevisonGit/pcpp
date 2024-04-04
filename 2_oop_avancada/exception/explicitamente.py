class RocketNotReadyError(Exception):
    pass


def personal_check(crews, roles):
    try:
        for i in range(len(roles)):
            print(f"The {crews[i]}'s name is {roles[i]}")
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


role = ['captain', 'pilot', 'mechanic', 'navigator']
crew = ['John', 'Mary', 'Mike']
print("Final check procedure")
personal_check(crew, role)
