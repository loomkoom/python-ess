"""
A program that reads a two polar coordinates, r and theta and converts it
into Cartesian coordinates (x, y).

Examples of conversions:
r = 1, theta = 0                    | x = 1.0 , y = 0.0
r = 2.0, theta = -1.5707963267948   | x = 0, y = -2 (x should be almost zero)
r = 4.5, theta = 2.68               | x = -4.02904937628, y = 2.00418590044
r = 0, theta = 0                    | x = 0, y = 0
r = 0, theta = 1                    | x = 0, y = 0
"""

import math
r = float(input('geef r: '))
theta = float(input('geef theta: '))

x = r * math.cos(theta)
y = r* math.sin(theta)

print('x =',x,'y = ',y)

