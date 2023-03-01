def multiply(a,b):
    """
      Return the product of a and b.
      - Both a and b must be non-negative integer
        numbers.
      - The function computes the product by means
        of successive additions.
    """

    if b == 0:
        return 0
    else:
        return a + multiply(a,b-1)

assert multiply(3,0) == 0
assert multiply(3,4) == 12

def multiply(a,b):
    """
      Return the product of a and b.
      - Both a and b must be integer numbers.
      - The function computes the product by means
        of successive additions.
    """

    if b == 0:
        return 0
    elif b > 0:
        return a + multiply(a,b-1)
    else:
        return -a + multiply(a,b+1)

assert multiply(3,0) == 0
assert multiply(3,4) == 12
assert multiply(-3,4) == -12
assert multiply(3,-4) == -12
assert multiply(-3,-4) == 12