#! Version computing the multiple factorial from left to right
# ! using a while statement
def multiple_factorial(n, base):
    """ Return the multiple factorial of the given number. in the given base.
    The resulting values is equal to 1*(base+1)*(2*base+1)*...*(n-base)*n.
    The given number diminished by 1 must be a positive multiple of the given
    base."""

    multifac = 1
    c = 1
    assert ((multifac - 1) % base == 0) and ((multifac - 1) // base >= 0)
    while c <= n // base:
        multifac *= (c * base + 1)
        c += 1
        assert ((multifac - 1) % base == 0) and ((multifac - 1) // base >= 0)
    return multifac


assert multiple_factorial(10, 3) == (1 * 4 * 7 * 10)
assert multiple_factorial(1, 4) == 1


# ! Version computing the multiple factorial from right to left
# ! using a for statement
def multiple_factorial_alt(n, base):
    """ Return the multiple factorial of the given number. in the given base.
    The resulting values is equal to 1*(base+1)*(2*base+1)*...*(n-base)*n.
    The given number diminished by 1 must be a postive multiple of the given
    base."""

    multifac = 1

    for c in range(1, n // base + 1):
        assert ((multifac - 1) % base == 0) and ((multifac - 1) // base >= 0)
        multifac *= (c * base + 1)
        c += 1
        assert ((multifac - 1) % base == 0) and ((multifac - 1) // base >= 0)
    return multifac


assert multiple_factorial_alt(10, 3) == (1 * 4 * 7 * 10)
assert multiple_factorial_alt(1, 4) == 1
