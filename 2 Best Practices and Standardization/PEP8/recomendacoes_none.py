"""
# Bad:

if x == None:
    print("A")
"""

# Good
x = None
if x is None:
    print("A")
