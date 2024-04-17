"""
# Bad:

if not x is None:
    print("It exists")
"""

# Good
x = "string"
if x is not None:
    print("It exists")
