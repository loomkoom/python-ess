def power(x,n):
    """ Return x to the power n.
      x must be a number and n must be a non-negative integer number."""


    # if n == 0:
    #     return 1
    # assert power(x,n-1)% x == 0
    # return x*power(x,n-1)

    # r = 1
    # for i in range(1,n+1):
    #     r *= x
    #     print(r,x,i)
    #     assert r == x**i

    k = 0
    power_so_far = 1

    if isinstance(x,int) and isinstance(n,int) and n >= 0:
        while k != n:
            assert power_so_far == x ** (k)
            # INVARIANT: power_so_far is equal to x to the power k.
            power_so_far *= x
            k += 1
        print(power_so_far,x,k)
    return power_so_far


# n is zero
assert power(3,0) == 1
# n is positive
assert power(3,2) == 9


