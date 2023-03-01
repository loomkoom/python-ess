# Write a recursive function that calculates the greatest common divisor of 
# two positive integer numbers.
#
# Use the theorem of Euclid to compute the greatest common divisor.
# This theorem states that the greatest common divisor of two integer numbers a and b
# (with a > b > 0) is equal to the greatest common divisor of a - b and b
#
# As an example, consider the gcd of a=12 and b=18:
# gcd(12, 18) = gcd(12, 18-12) = gcd(12, 6) = gcd(12-6, 6) = gcd(6, 6) = 6

def gcm(a, b):
  if a == b:
    return a
  if b > a:
    a, b = b, a
  return gcm(a - b, b)

assert gcm(2,6)   == 2
assert gcm(24,32) == 8
assert gcm(45,55) == 5
assert gcm(13,29) == 1
