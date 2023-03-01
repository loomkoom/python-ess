# A program that calculates the greatest common divisor of two positive integer numbers.
#
# You may assume that the user enters two positive integer numbers
# (i.e. the program may crash, loop infinitely, ... if the input is not correct)
# Use the theorem of Euclid to compute the greatest common divisor.
# This theorem states that the greatest common divisor of two integer numbers a and b
# (with a > b > 0) is equal to the greatest common divisor of a - b and b
#
# As an example, consider the gcd of a=12 and b=18:
# 	gcd(12, 18) = gcd(12, 18-12) = gcd(12, 6) = gcd(12-6, 6) = gcd(6, 6) = 6

# (1) Start with a description of the algorithm in pseudo code.
# (2) Implement the algorithm in Python.
# (3) Verify the correctness of your program with the following pairs:
#    [81,45]: gcd is 9
#      [1,1]: gcd is 1
# [113, 271]: gcd is 1


a = int(input('give the larger positive integer number: '))
b = int(input('give the smaller positive integer number: '))

while a != b :
    if a > b:
        a = a - b
    if b > a:
        b = b - a

gcd = a                         # wanneer a == b

print(gcd)




