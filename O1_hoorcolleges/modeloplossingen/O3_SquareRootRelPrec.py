# Calculate the square root of a given number.
#   - The program assumes it can read a positive number
#   that is not infinite.
#   - It prints an approximation of the square root
#     of that number. The relative precision of the
#     approximation does not exceed 1.0E-15.

number =\
  float(input("Enter a non-negative number: "))

PRECISION = 0.1E-15

prev_approx = 1.0
approx_root = (prev_approx +number/prev_approx)/2

while (prev_approx != approx_root) and\
        (abs((approx_root*approx_root - number)/number) >\
            PRECISION) :
  prev_approx = approx_root
  approx_root =\
      (prev_approx + number/prev_approx)/2

print("sqrt(", number, ") =", approx_root)
if abs((approx_root**2 - number)/number) > PRECISION:
  print("   Precision probably not reached!")
