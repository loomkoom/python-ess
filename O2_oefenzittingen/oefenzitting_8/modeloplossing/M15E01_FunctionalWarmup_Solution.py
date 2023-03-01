"""
Rewrite the following code in a functional style using lambda, map, filter.
Each value can be calculated on a single line.
"""

# Functional warmup 1: calculate the difference between the third and the second
# power of each number in range(-5,5).

x1 = list(map(lambda n: n**3-n**2, range(-5,5)))

assert x1 == [-150, -80, -36, -12, -2, 0, 0, 4, 18, 48]


# Functional warmup 2: give the list of all odd numbers that have a square
# between 110 and 260.

x2 = list(filter(lambda n: n%2==1 and 110 <= n**2 <= 260, range(100)))

assert x2 == [11, 13, 15]

# Functional warmup 3: calculate the square of all odd numbers in range(50)
# that are divisible by 5

x3 = list(map(lambda n: n**2, filter(lambda n: n%2==1 and n%5==0,range(50))))

assert x3 == [25, 225, 625, 1225, 2025]
