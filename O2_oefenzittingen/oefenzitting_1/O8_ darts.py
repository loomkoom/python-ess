"""
A program that calculates the score for throwing a dart
at a dart board.

The program reads the two coordinates at which the dart has hit
the board, assuming that the center of the board is at
coordinate 0.0 : 0.0.

The center of the board, called the bull, has a radius of 0.5 cm.
Around that centre are 9 concentric circles, each with a width
of 1.0 cm.

You get 10 points for hitting the bull, 9 points for the circle
immediately adjacent to the bull, Hitting a line separating two
concentric circles yields the lowest score of both circles.

Examples of inputs and outputs:
 - bull hit:
   x = 0, y = 0                 | You scored 10 point(s)
   x = 0, y = 0.5               | You scored 9 point(s)
   
 - 1st concentric circle:
   x = 1, y = -1                | You scored 9 point(s)
   x = -1, y = 1                | You scored 9 point(s)
   
 - Separating line:
  x = 3, y = 4                  | You scored 5 point(s)

 - Boundary on board:
  x = 0, y = 9.49999999999999   | You scored 1 point(s)

 - Boundary outside of board:
  x = 0, y = 9.50000000000001   | You scored 0 point(s)
"""

from math import *

x = float(input("x: "))
y = float(input("y: "))

distance = sqrt(x*x + y*y)

points = - floor(distance + 0.5) + 10

print('you scored',points,'point(s)')

# if distance >= 9.5:
#     points = 0
# elif distance >= 8.5:
#     points = 1
# elif distance  >= 7.5:
#     points = 2
# elif distance  >= 6.5:
#     points = 3
# elif distance  >= 5.5:
#     points = 4
# elif distance  >= 4.5:
#     points = 5
# elif distance  >= 3.5:
#     points = 6
# elif distance >= 2.5:
#     points = 7
# elif distance  >= 1.5:
#     points = 8
# elif distance  >= 0.5:
#     points = 9
# else:
#     points = 10









