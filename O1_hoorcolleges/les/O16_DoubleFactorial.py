#! Go to the settings/preferecnces of Pycharm
#! Select Project: Your Project Name / Python Interpreter
#! Click on +, search for numpy and click install package.

import numpy


def double_factorial(n):
    """
      Return the double factorial of the given number.
      The resulting value is equal to 1*3_5*...*(n-2)*n.
      The given number must be a positive odd number.

      - The version computes the product from left to right
    """
# ! recursief
    # if n == 1:
    #     return 1
    # else:
    #     return n*double_factorial(n-2)

    index = 1
    ans = 1

    # INVARIANT
    # ans is gelijk aan het product 1*3*5**...*(index-2)
    while index <= n:
        assert ans == numpy.product(range(1,index,2))
        ans *= index
        index += 2
    return ans

print(double_factorial(7))

assert double_factorial(7) == (7 * 5 * 3)
assert double_factorial(1) == 1


def double_factorial(n):
    """
      Return the double factorial of the given number.
      The resulting value is equal to 1*3_5*...*(n-2)*n.
      The given number must be a positive odd number.

      - The version computes the product from right to left
    """

    ans = 1
    index = n
    # INVARIANT
    # ans is gelijk aan het product n*(n-2)*...*(index+2)*index
    while index >= 1:
        assert ans == numpy.product(range(n,index,-2))
        ans *= index
        index -= 2
    return ans


assert double_factorial(7) == (7 * 5 * 3)
assert double_factorial(1) == 1

