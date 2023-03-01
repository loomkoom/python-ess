import math

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
  root_determinant = sqrt(determinant)
  print("Root 1:", (-b+root_determinant) / (2*a))
  print("Root 2:", (-b-root_determinant) / (2*a))
