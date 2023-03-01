from math import sqrt


def power(x, n):
    """ Return x to the power n.
        x must be a number and n must be a non-negavite integer number.
        This function should also use the property that the nth power of
        some number x is equal to the square of the (n/2)th power of x,
        provided n is an even number."""

    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x, n / 2) * power(x, n / 2)
    else:
        return x * power(x, n - 1)


assert power(0, 0) == 1
assert power(3, 0) == 1
assert power(3, 1) == 3
assert power(3, 2) == 9
assert power(4, 2) == 16
