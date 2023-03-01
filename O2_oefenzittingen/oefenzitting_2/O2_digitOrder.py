# Write a program that checks whether the digits in an integer number are in ascending order. As an example, the digits in 1335677 are in ascending order, whereas they are not in 1324.
#	The program must read the integer from the standard input stream. You may assume that the end user supplies a positive integer number.
#   The program must print a message like "The digits in the number XXX are (not) in ascending order".
#
# Start with a description of the algorithm in pseudo code (inspiring yourself on the pseudo code for the algorithm to calculate the sum of the digits, as listed in the course notes).
# Verify the correctness of your Python program with the numbers 1335677 (True), 1324 (False), 7 (True) and 12340 (False).


number = input("number: ")
huidige_positie = 0
ASCENDING = True

while huidige_positie < len(number) - 1:
    if number[huidige_positie] > number[huidige_positie + 1]:
        ASCENDING = False
        break

    huidige_positie += 1

if ASCENDING:
    print('the digits in',number, "are ascending")
else:
    print('the digits in',number, "are not ascending")





