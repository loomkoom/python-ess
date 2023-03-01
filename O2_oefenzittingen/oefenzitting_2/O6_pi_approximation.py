#this program will use monte carlo simulation to calculate an approximation of pi
# pi is approximately equal to (M/N)*4
# where:
#   - N is the number of random points considered (in square (-1,-1) to (1,1))
#   - M the number of random point that lie within the circle (center (0,0) and radius 1)
from random import *
from math import *

N = 0
M = 0

while N < 100000 :
    x = random() * 2.0 - 1
    y = random() * 2.0 - 1

    if sqrt(x * x + y * y) <= 1:
        M += 1

    N += 1

pi = (M/N)*4
print(pi)
