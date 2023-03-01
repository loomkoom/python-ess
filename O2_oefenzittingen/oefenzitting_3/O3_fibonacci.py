"""
A function that returns the n-th fibonacci number.
The function takes as argument n.
The function must always return a number.

A Fibonnaci sequence exists of the numbers:
1, 1, 2 ,3, 5, 8, 13, 21, 34, 55, 89, ...

The first two numbers in the sequence are 1.
The consecutive number is the addition of the previous two numbers.

For example: the 4th fibonacci number is 3
             the 6th fibonacci number is 8
"""

def fibonacci(n):
    fib = [1,1]
    index = 1


    for index in range(n):
        fib_nr = fib[index-1] + fib[index]
        list.append(fib,fib_nr)

    return fib[n-1]


# TESTS
assert fibonacci(5) == 5
assert fibonacci(12) == 144
assert fibonacci(37)== 24157817
assert fibonacci(2) == 1
