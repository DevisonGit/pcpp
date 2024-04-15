"""
######### Bad:

my_list_one = [1, 2, 3,
    4, 5, 6
]

a = my_function_name(a, b, c,
    d, e, f)


########## Good:

my_list_one = [
    1, 2, 3,
    4, 5, 6,
    ]

a = my_function_name(a, b, c,
                       d, e, f)
"""