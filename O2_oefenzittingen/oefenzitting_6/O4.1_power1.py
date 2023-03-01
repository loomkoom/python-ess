def power(x, n):
    """ Return x to the power n.
        x must be a number and n must be a non-negative integer number.
        This function should use the property that the nth power of some
        number x is equal to the (n-1)th power of x multiplied with x."""

    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


assert power(0, 0) == 1
assert power(3, 0) == 1
assert power(3, 1) == 3
assert power(3, 2) == 9
assert power(4, 2) == 16
