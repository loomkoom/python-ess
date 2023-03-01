"""
A function that returns the greatest common divisor
of two positive integer numbers

* Reuse your the solution to this problem from the previous session! This exercise focuses on defining an using functions!

* You may assume that the user enters two positive integer numbers
(i.e. the program may crash, loop infinitely, ... if the input is not correct)

* Use the theorem of Euclid to compute the greatest common divisor.
This theorem states that the greatest common divisor of two integer numbers a and b (with a > b > 0)
is equal to the greatest common divisor of a - b and b.
As an example, the computation of the gcd of 12 and 18, can be reduced to the computation of the gcd of 12 and 6,
which can be reduced to the computation of the gcd of 6 and 6. The gcd of 6 and 6 is obviously 6.
"""

def gcd(a,b):

    '''

    '''

    # a = int(input('give the larger positive integer number: '))
    # b = int(input('give the smaller positive integer number: '))

    while a != b:
        if a > b:
            a = a - b
        if b > a:
            b = b - a

    gcd = a  # wanneer a == b

    return gcd


assert gcd (12,18) == 6





#TESTS
## Call the function to compute the greatest common divisor of 75 and 165,
##	once using postional arguments and and once using keyword arguments.
## e.g., invoking the 'print' function with a positional "hello" argument:
##   print("hello")
