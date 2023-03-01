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

from math import sqrt

BULL_RADIUS = 0.5
NUMBER_CIRCLES = 9
CIRCLE_WIDTH = 1.0
DARTBOARD_RADIUS = BULL_RADIUS + (NUMBER_CIRCLES * CIRCLE_WIDTH)

x = float(input("Enter the x-value: "))
y = float(input("Enter the y-value: "))

MAX_SCORE = NUMBER_CIRCLES + 1

# distance from center
dist = sqrt(x**2 + y**2)

if dist < BULL_RADIUS:
    score = MAX_SCORE
else:
    # the circle that was hit (the bull is considered to be circle 0, hence + 1)
    circle = 1 + int((dist - BULL_RADIUS) // CIRCLE_WIDTH)
    score = max(MAX_SCORE - circle, 0)

print("You scored", score, "point(s)")
