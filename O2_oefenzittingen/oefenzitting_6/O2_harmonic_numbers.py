def harmonic(n):
    """ For n > 0,  return the nth harmonic number H(n) = 1 + 1/2 + 1/3 + ... + 1/n
        For n <= 0, return 0 """
    if n <= 0:
        return 0
    else:
        return 1 / n + harmonic(n - 1)


assert harmonic(-1) == 0
assert harmonic(0) == 0
assert harmonic(1) == 1.0
assert harmonic(3) == 1.0 + 1.0 / 2 + 1.0 / 3
assert harmonic(5) == 1.0 + 1.0 / 2 + 1.0 / 3 + 1.0 / 4 + 1.0 / 5
