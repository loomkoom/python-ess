"""
A program that reads a two Cartesian coordinates, x and y, and converts it
into Polar coordinate pair (r, theta).

Examples of conversions:
x = 1, y = 0                            | r = 1.0 , theta = 0
x = 0, y = -2                           | r = 2.0 , theta = -1.57079632679
x = -4.02904937628, y = 2.00418590044   | r = 4.5 , theta = 2.68
x = 0, y = 0                            | r = 0 , theta = 0
x = 3, y = 4                            | r = 5.0 , theta = 0.927295218002
x = -3, y = -4                          | r = 5.0 , theta = -2.21429743559
"""
from math import *

x = float(input('geef x: '))
y = float(input('geef y: '))


r = sqrt(x*x+y*y)
theta = atan2(y,x)

print('r= ',r,'theta = ',theta)