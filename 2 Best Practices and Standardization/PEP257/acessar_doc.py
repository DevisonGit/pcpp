def my_fun(a: int, b: int) -> int:
    """The summary line goes here

    A more elaborate description of the function

    Parameters:
    :param a: int (description)
    :param b: int (description)

    Returns:
    :return: int Description of the return value
    """
    return a * b


print(my_fun.__doc__)
help(my_fun)
