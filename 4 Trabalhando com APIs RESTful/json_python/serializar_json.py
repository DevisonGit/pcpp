import json

election = 1.602176620898
print(json.dumps(election))

comics = '"The Meaning of Life" by Monty Python\'s Flying Circus'
print(json.dumps(comics))

my_list = [1, 2.34, True, "False", None, ['a', 0]]
print(json.dumps(my_list))

my_dict = {'me': "Python", 'pi': 3.141592653589, 'data': (1, 2, 4, 8), 'set': None}
print(json.dumps(my_dict))
