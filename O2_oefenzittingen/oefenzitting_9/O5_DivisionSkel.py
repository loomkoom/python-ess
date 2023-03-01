def integer_division(dividend, divisor):
    """ Return the quotient and the remainder (in that order)
    resulting from the integer division of the given dividend
    by the given divisor."""
    quotient = None
    remainder = None
    n = 1
    while n == 1:
        # ! It is often easier to specify the loop invariant in a more formal,
        # ! mathematical way.
        # LOOP INVARIANT
        quotient = dividend // divisor
        remainder = dividend % divisor
        assert dividend == quotient * divisor + remainder
        n += 1
    return quotient, remainder


##TESTS
assert integer_division(5, 13) == (0, 5)
assert integer_division(27, 4) == (6, 3)
assert integer_division(20, 4) == (5, 0)
assert integer_division(10, 1) == (10, 0)

## CORRECTNESS

# BASE CASE
# Given: ...
# To prove: dividend == quotient*divisor + remainder
#   ...


# INDUCTION STEP
# Denote values of quotient and remainder at the start of the body as
# quotient', respectively remainder'
# Given: ...
# To prove: dividend == quotient*divisor + remainder
#   ...

# EPILOGUE
# Given: ...
# To prove: (dividend == quotient*divisor + remainder) and (remainder < divisor)
#   ...


## CORRECTNESS

#BASE CASE
# Given: (quotient == 0) and (remainder == dividend)
# To prove: dividend == quotient*divisor + remainder
#   The assertion to prove reduces to dividend == 0*divisor + dividend

#INDUCTION STEP
# quotient', respectively remainder' denote the values of quotient,
# respectively of remainder at the start of the body.
# Given: dividend == quotient'*divisor + remainder'
# Given remainder >= divisor
# To prove: dividend == quotient*divisor + remainder
#   From the body we can derive:
#     (quotient = quotient'+1) and (remainder = remainder'-divisor)
#   Substituting the left-hand sides by the right-hand sides in the assertion
#   to prove yields:
#     dividend == (quotient'+1)*divisor + (remainder')-divisor
#   which can be reduced to the first given fact.

#EPILOGUE
# Given: dividend == quotient*divisor + remainder
# Given remainder < divisor
# To prove: (dividend == quotient*divisor + remainder) and (remainder < divisor)
#   The assertion to prove directly follows from the given facts.
