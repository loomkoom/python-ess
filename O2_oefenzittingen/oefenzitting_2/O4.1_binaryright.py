# A program that calculates the binary representation of some integer number.
#   The program prompts for an integer number and prints out its binary
#   representation, using the Python syntax rules. The behavior of the
#   program is undefined if no integer number is entered.
#   This version calculates the binary representation from right to left
#   (i.e., starting with the least significant digit)
#
# pseudo-code:
# Read the integer number from the standard input stream
# Account for negative numbers
# Initialize the binary number to the empty string
# while the given number is different from 0
#   Determine the remainder of dividing the number at stake by 2
#   if the remainder is 0
#     Extend the binary number with "0" to its left
#   otherwise
#     Extend the binary number with "1" to its left
#   Replace the number at stake with the quotient of the division of the number by 2.
# Print the resulting binary number on the standard output stream preceded by "0B" or "-0B", depending on whether the original number was positive or negative, 
# or "0B0" if the number was zero.


# examples:
#   18 : 0B10010
#    0 : 0B0
#  -31 : -0B11111

number = int(input('give an integer number: '))
getal = abs(number)
binair = str()

while getal != 0:
    remainder = getal % 2
    if remainder == 0:
        binair = '0' + binair
    else:
        binair = '1' + binair

    getal = getal // 2

if number > 0:
    print('0B',binair,sep='')
if number < 0:
    print('-0B',binair,sep='')
elif number == 0:
    print('0B0')




