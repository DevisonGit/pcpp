""" Beautiful is better than ugly.
from math import sqrt
sidea = float(input("The length of the 'a' side:"))
sideb = float(input("The length of thr 'b' side:"))
sidec = sqrt(sidea**2+sideb**2)
print("The length of the hypotenuse is", sidec)
"""
from math import sqrt

side_a = float(input("The length of the 'a' side:"))
side_b = float(input("The length of the 'b' side:"))
hypotenuse = sqrt(side_a ** 2 + side_b ** 2)

print("The length of the hypotenuse is", hypotenuse)
