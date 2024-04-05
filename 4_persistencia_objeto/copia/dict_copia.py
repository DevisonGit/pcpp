import copy

a_dict = {"first_name": "James", "last_name": "Bond", 'movies': ['Goldfinger (1964)', "You Only Live Twice"]}
b_dict = copy.deepcopy(a_dict)
print("Memory chunks", id(a_dict), id(b_dict))
print("Let's modify the movie list")
a_dict['movies'].append("Diamonds Are Forever (1971)")
print('a_dict movies', a_dict['movies'])
print('b_dict movies', b_dict['movies'])
