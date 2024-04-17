"""
# Bad:

if name[:4] == 'Adam':
    # do something
"""

# Good
name = "Adam"
if name.startswith('Adam'):
    # do something
    ...
