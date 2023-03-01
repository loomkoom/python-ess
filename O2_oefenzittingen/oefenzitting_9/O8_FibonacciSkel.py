def fibonacci(N):
    """  Return a list containing the first N numbers of the Fibonacci series.
    The resulting list is such that the first 2 elements, if any, are 0 and 1.
    All successive elements are equal to the sum of the two preceding elements."""

    if N == 0:
        return []
    elif N == 1:
        return [0]
    k = 2
    fib_numbers = [0,1]
    next = fib_numbers[0] + fib_numbers[1]

    while k != N:
        # INVARIANT element op index k = som van elementen op index k-1 en k-2
        assert all(fib_numbers[i] == fib_numbers[i-1] + fib_numbers[i-2] for i in range(2,k))
        fib_numbers.append(next)
        next = fib_numbers[k] + fib_numbers[k-1]
        k+= 1
    return fib_numbers

assert fibonacci(0) == []
assert fibonacci(1) == [0]
assert fibonacci(2) == [0,1]
assert fibonacci(12) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
