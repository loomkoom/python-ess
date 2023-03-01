# Calculate the square root of a given number.
#   - The program assumes it can read a non-negative number
#     that is not infinite.
#   - It prints an approximation of the square root of
#     the given number. The difference in absolute value
#     between the squared approximation and the given
#     number does not exceed 1.0E-200, unless the program
#     signals otherwise.

number =\
  float(input("Enter a non-negative number: "))

PRECISION = 0.1E-200

prev_approx = 1.0
approx_root = (prev_approx +number/prev_approx)/2

while (prev_approx != approx_root) and \
        (abs(approx_root*approx_root - number) >\
            PRECISION):
  prev_approx = approx_root
  approx_root =\
      (prev_approx + number/prev_approx)/2

print("sqrt(", number, ") =", approx_root)
if abs(approx_root**2 - number) > PRECISION:
  print("   Precision probably not reached!")
