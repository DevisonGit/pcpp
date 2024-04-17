"""
# Bad:

my_boolean_value = 2 > 1
if my_boolean_value == True:
    print("A")
else:
    print("B")
"""

# Good
my_boolean_value = 2 > 1
if my_boolean_value is True:
    print("A")
else:
    print("B")

# Better
my_boolean_value = 2 > 1
if my_boolean_value:
    print("A")
else:
    print("B")
