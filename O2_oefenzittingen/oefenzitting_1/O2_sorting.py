"""
Write a program that reads three integer numbers and sorts them from smallest
to biggest. As a bonus, try to find a solution by using as few if statements
as possible.
"""

first = int(input('geef getal 1: '))
second = int(input('geef getal 2: '))
third = int(input('geef getal 3: '))

if first > third:                             # a <-> c
    first,third = third,first

if second > third:                            # b <-> c
    second, third = third, second

if second < first:                            # a <-> b
   first, second = second, first


print(first, second, third)













