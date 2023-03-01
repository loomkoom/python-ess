def get_mantissa(number,n=32):
    i= 1
    remaining = number
    mantissa = ""
    while i <= n:
        if 1/(2**i) <= remaining:
            remaining -= 1/(2**i)
            mantissa += "1"
        elif i == n and (abs(remaining- 1/(2**i)) <= abs(remaining)):
            mantissa += "1"
        else:
            mantissa += "0"
        i += 1
    return mantissa


def get_mantissa(number,n=53):
    bit = 1/2
    remaining = number
    mantissa = ""
    while len(mantissa) < n:
        if bit <= remaining:
            remaining -= bit
            next = "1"
        elif len(mantissa) == n-1 and (abs(remaining - bit) <= abs(remaining)):
            next = "1"
        else:
            next = "0"
        bit /= 2
        mantissa += next
    return mantissa

import random
import math

for n in range(100):
    nb = random.uniform(0.0,0.99)
    print(get_mantissa(nb),bin(math.frexp(nb)[0]),sep=" | ")
    #assert get_mantissa(nb) == math.frexp(nb)[0]