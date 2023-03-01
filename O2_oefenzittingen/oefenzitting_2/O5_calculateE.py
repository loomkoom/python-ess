# Write a program that calculates the floating point number that is as close as possible to the number e.
# The number e can be calculated (approximated) from the formula 1 + 1/1! + 1/2! + 1/3! + ... 
# Verify the correctness of the program. The program should print 2.71828182846 as the closest approximation.

from math import *

e = 1
n = 1

while n < 40:
    e += 1/factorial(n)
    n += 1
print(e)
