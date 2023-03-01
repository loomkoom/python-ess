"""
A function that examines whether a given number is a perfect number,
i.e. a number equal to the sum of its divisors (including 1).
The function must accept the number as argument.
The function must always return a boolean.

Some example outputs for given inputs:
6       True
496     True
35      False
"""

def is_perfect_number(int):

    divisors = []
    sum = 0

    for n in range(1,int):
        if int % n == 0:
            divisors. append(n)
    for i in range(len(divisors)):
        sum += divisors[i]
    if sum == int:
        return True
    return False




# TESTS
assert is_perfect_number(6) == True
assert is_perfect_number(496) == True
assert is_perfect_number(35) == False

