# Write a program that shifts a given string by a given amount.
#    All elements of the string will be shifted to the left by the given amount,
#      look at the examples if you're unsure what exactly is meant by "shift".
#
#    You may assume that the user enters an integer number for the shift amount.
#    HINT: This can be implemented without using while loops
#
#    Test your program:
#       string = "12345", shift = 3, solution = 45123
#       string = "12345", shift = 6, solution = 23451
#       string = "12345", shift = -1, solution = 51234

string = input('geef een string:')
shift = int(input('amount ot shift: '))

if shift > len(string):
    shift = shift % len(string)

string = string[shift:] + string[:shift]
print(string)
