"""Use RECURSION to implement the function factorial"""

def factorial(n):
    """ For n > 0, return the factorial of n, n! = 1 * 2 * 3 * ... * n
        For n = 0, return 1 (!0 = 1)
        For n < 0  return 0 (factorial is undefined)"""
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

assert factorial(-3) == 0
assert factorial(0)  == 1
assert factorial(1)  == 1
assert factorial(3)  == 6
assert factorial(5)  == 120
assert factorial(5)  == 120
assert factorial(12) == 479001600
