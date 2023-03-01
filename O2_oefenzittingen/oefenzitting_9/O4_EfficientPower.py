# The function expects x to be a number and n to be some non-negative integer number.

# Work out a more efficient version in which the number of multiplications is reduced
# by replacing x by the square of x whenever the resulting power is even. As an example,
# the computation of x**12 can be computed as (x*x)**6.

# Work out the loop invariant, and develop the code starting from that description.
# Prove the correctness of the algorithm

def power(x, n):
    """ Return x to the power n.
    x must be a number and n must be a non-negavite integer number."""
    pass
#     r = 1
#
#     if isinstance(x, int) and isinstance(n, int) and n >= 0:
#         while n != 0:
#             if n % 2 == 0:
#                 r *= x * x
#                 n //= 2
#             else:
#                 r *= x
#                 n -= 1
#         print(r, x, n)
#         return r

def power(x, n):
    """ Return x to the power n.
    x must be a number and n must be a non-negavite integer number."""
    result = 1
    k = n
    fac = x

    if isinstance(x, int) and isinstance(n, int) and n >= 0:
        while k != 0:
            assert result*fac**k == x**n
            if k % 2 == 0:
                fac *= fac
                k //= 2
            else:
                result *= fac
                k -= 1
        print(result, x, k)
        return result

## TESTS
# n is zero
assert power(3, 0) == 1
# n is positive and not all even.
assert power(3, 5) == 243
# n is all even
assert power(3, 4) == 81

## CORRECTNESS
'''
#BASE CASE
# Given:
  counter == n
  result == 1
  factor == x
# To prove: 
  result == (x**n) * (factor**(-counter)) == 1
# Proof:
  By replacement of the given expressions we get:
  result == (x**n) * (x**(-n))
  <=> result == 1

#INDUCTION STEP
# Given: 
  result' == (x**n) * (factor'**(-counter'))
# To prove: 
  The given invariant is satisfied at the end of the loop body,
  result == (x**n) * (factor**(-counter))
# Proof:
Case 1:
    counter%2 == 0
    We get that factor == factor'**2 and counter = counter'/2
    Result is not adapted, so we get that the following equality should hold:
    result' == result
    <=> (x**n) * (factor'**(-counter')) == (x**n) * (factor**(-counter))
    <=> (x**n) * (factor'**(-counter')) == (x**n) * ( (factor'**2)**(-counter'/2)) #Replacing factor and counter
    <=> (x**n) * (factor'**(-counter')) == (x**n) * ( (factor')**(-counter') #Working out the powers in the rhs
Case 2:
    counter%2 != 0
    We get result == result'*factor and counter == counter' - 1 and (implicitly) factor == factor'
    result == result' * factor
    <=> result == (x**n) * (factor'**(-counter')) * factor
    <=> result == (x**n) * (factor**(-counter' +1)) #as factor == factor'
    <=> result == (x**n) * (factor**(-counter)) #As counter == counter' - 1 


#EPILOGUE
#Given: result == (x**n) * (factor**(-counter))
       counter == 0
#To prove: result == x**n
#Proof: 
    result == (x**n) * (factor**(-counter))
    <=>result == (x**n) * (factor**(-0)) #As counter == 0
    <=> result == (x**n)
'''
