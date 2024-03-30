def combiner(a, b, *args, **kwargs):
    super_combiner(*args, **kwargs)


def super_combiner(*args, **kwargs):
    print("args", args)
    print("kwargs", kwargs)


combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')
