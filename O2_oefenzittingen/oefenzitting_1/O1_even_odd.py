"""
Write a program that reads an integer number, and determines
whether that number is even, odd or zero.

The program writes out one of the strings "Even", "Odd"
or "Zero". In case 0 is input, the program produces Zero
 and not Even (although in mathematics, 0 is also an even number).
"""

getal = int(input('geef getal: '))

if getal==0 :
    print(getal,'is nul')
elif (getal % 2 == 0):
    print(getal,'is even')
else:
    print(getal,'is oneven')