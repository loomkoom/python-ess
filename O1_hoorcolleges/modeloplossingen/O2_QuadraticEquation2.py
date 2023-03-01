from math import *

# Calculate the roots of a quadratic equation.
#   The program reads the coefficients a, b and c
#   of the equation ax**2+bx+c.
#   It either prints that the given equation has
#   no roots, exactly one root or two roots.
#   In the latter cases, the program also displays
#   the values of the roots.

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

determinant = b*b - 4*a*c

if determinant < 0.0:
  print("No roots")
elif determinant == 0.0:
  print("Single root:", -b / (2*a))
else:
  # This version only computes the biggest root in absolute value.
  # The other root is derived from the property that the product of both
  # roots is equal to c/a.
  root_determinant = sqrt(determinant)
  if b < 0.0:
    root1 = (-b+root_determinant) / (2*a)
    root2 = c / (a*root1)
  else:
    root1 = (-b-root_determinant) / (2*a)
    root2 = c / (a*root1)
  print("Root 1:", root1)
  print("Root 2:", root2)
