def combiner(a, b, *args, **kwargs):
    super_combiner(*args, **kwargs)


def super_combiner(*my_args, **my_kwargs):
    print('my_args', my_args)
    print('my_kwargs', my_kwargs)


combiner(10, '20', 40, 60, 30, arguments_1=50, arguments_2='66')
