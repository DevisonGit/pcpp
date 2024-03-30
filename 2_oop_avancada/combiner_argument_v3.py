def combiner(a, b, *args, c=20, **kwargs):
    super_combiner(c, *args, **kwargs)


def super_combiner(c, *args, **kwargs):
    print("args", args)
    print("c", c)
    print("kwargs", kwargs)


combiner(10, '20', 40, 60, 30, c=2, argument1=50, argument2='66')
