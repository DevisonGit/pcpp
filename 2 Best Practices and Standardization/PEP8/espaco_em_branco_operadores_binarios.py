"""
# Bad:

x=x+3
x -=1

x = x * 2 - 1
x = (x - 1) * (x + 2)
"""

# Good
x = 0
x = x + 3
x -= 1

x = x*2 - 1
x = (x-1) * (x+2)
