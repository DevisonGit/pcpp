""" Flat is better than nested.
x = float(input("Enter a number: "))

if x > 0:
    if x > 1:
        if x > 2:
            if x > 3:
                if x >= 4:
                    if x <= 6:
                        print("x is a number between 4 and 6.")
else:
    print("x is not a number between 4 and 6.")
"""
x = float(input("Enter a number: "))

if 4 <= x <= 6:
    print("x is a number between 4 and 6")
else:
    print("x is not a number between 4 and 6")
