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

from math import sqrt, ceil

BULL_RADIUS = 0.5
NUMBER_CIRCLES = 9
CIRCLE_WIDTH = 1.0
DARTBOARD_RADIUS = BULL_RADIUS + (NUMBER_CIRCLES * CIRCLE_WIDTH)

x = float(input("Enter the x-value: "))
y = float(input("Enter the y-value: "))

# The score is easier calculated from the distance to the edge of the board.
# Given the distance to the edge D, the score S is such that S-1 <= D < S.
# For a distance to the edge of 0.2, the score must then be then be 1.
# For a distance to the edge of 9.3 (in the bull), the score must be 10.
# A negative distance to the edge means that the dart has not hit the board.

# distance wrt center
distance = sqrt(x**2+y**2)

# distance wrt outer circle
outer_distance = DARTBOARD_RADIUS - distance

# points should not be negative
points = max(0,int(ceil(outer_distance)))

print("You scored", points, "point(s)")
