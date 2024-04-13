"""Errors should never pass silently.
try:
    print(1/0)
except Exception as e:
    pass
"""
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print("Don't divide by zero")

try:
    number = int(input("Enter an integer number: "))
except:
    number = 0
