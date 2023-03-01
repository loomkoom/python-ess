def factorial(n):

    if n == 1:
        return 1

    else:
        red_n = n-1
        result = n* factorial(red_n)
        return result

assert factorial(3) == 6