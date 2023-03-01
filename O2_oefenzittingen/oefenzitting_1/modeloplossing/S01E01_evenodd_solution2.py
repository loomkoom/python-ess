"""
A program that reads an integer number, and determines
whether that number is even, odd or zero.

The program writes out one of the strings "Even", "Odd"
or "Zero". In case 0 is input, the program produces Zero
 and not Even (although in mathematics, 0 is also an even number).
"""

number = int(input("Enter a number: "))

if number == 0:
  print("Zero")
elif number % 2 == 0:
  print("Even")
else:
  print("Odd")
