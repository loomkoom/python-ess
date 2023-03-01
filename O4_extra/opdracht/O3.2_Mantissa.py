# Calculate the binary representation of the mantissa
# with the required number of bits of the given
# floating-point number.
#   - The given number must be in the range 0.0 .. 1.0.
#   - The required number of bits must be positive.
#   - The actual mantissa is preceded by a zero and a dot.
#   - The difference in absolute value between the value
#     of the mantissa and the given number is as small as
#     possible, meaning that the last bit of the mantissa
#     is rounded.
