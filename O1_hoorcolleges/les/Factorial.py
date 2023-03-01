def factorial(n):

  """
    Return the factorial of a given positive number n.
    The factorial of n is defined as the product
    1*2*...*(n-1)*n.
  """

  if (n == 1):
    return 1
  else:
    return n * factorial(n - 1)


assert factorial(1) == 1
assert factorial(4) == 1 * 2 * 3 * 4


def factorial(n):

  """
    Return the factorial of a given positive number n.
    The factorial of n is defined as the product
    1*2*...*(n-1)*n.
  """

  if (n == 1):
    return 1
  else:
    red_n = n - 1
    result = n * factorial(red_n)
    return result


assert factorial(1) == 1
assert factorial(4) == 1*2*3*4
