"""
A program that reads an integer number, and determines
whether that number is even, odd or zero.

The program writes out one of the strings "Even", "Odd"
or "Zero". In case 0 is input, the program produces Zero
 and not Even (although in mathematics, 0 is also an even number).
"""

number = int(input("Enter a number: "))

is_zero = (number == 0)
is_even = (number % 2 == 0)
is_odd = (number % 2 == 1)

if is_zero:
  print("Zero")
elif is_even:
  print("Even")
elif is_odd:
  print("Odd")
