"""
Write a program that reads three integer numbers and sorts them from smallest
to biggest. As a bonus, try to find a solution by using as few if statements
as possible.
"""

first  = int(input("Enter the first number: "))
second = int(input("Enter the second number:"))
third  = int(input("Enter the third number: "))

if first > third:
  first , third = third , first
if first > second:
  first , second = second , first
if second > third:
  second , third = third , second

print(first,second,third)
