"""
You are given a sequence of integer numbers. Take from this sequence the numbers that have exactly two digits, and
calculate the sum of their digits.
To do this, implement the function has_n_digits, that should check if a number has exactly n digits. (Come up with a
simple algorithm to do this yourself, or search the web)

- Provided: sum_digits_iterative, an iterative algorithm to solve the problem.

- To implement:
 * sum_digits_recursive: A recursive version that doesn't change the contents of the original sequence.
 * sum_digits_comprehension: A version that uses list comprehension.
 * sum_digits_map_filter: A version that uses the filter and map functions.
"""


def has_n_digits(number, digits = 2):
    """
    Returns true if the given number consists of exactly n digits,
    otherwise return false.
    """
    nb_str = str(abs(number))

    return len(nb_str) == digits


def digits(number):
    number = abs(number)
    seq = []
    while number > 0:
        seq.append(number % 10)
        number //= 10
    seq.reverse()
    return seq


def sum_digits_iterative(seq):
    """
    Returns the sum of the digits of all two-digit numbers
    in the given collection of numbers.
    """

    # sum = 0
    # for number in seq:
    #     if has_n_digits(number, 2):
    #         number = abs(number)
    #         digit_units = number % 10
    #         digit_tens = number // 10
    #         sum += digit_units + digit_tens
    # return sum

    sum_digits = 0
    for number in seq:
        if has_n_digits(number, 2):
            sum_digits += sum(digits(number))
    return sum_digits


def sum_digits_recursive(seq):
    """
    Returns the sum of the digits of all two-digit numbers
    in the given collection of numbers.
    """
    if len(seq) == 0:
        return 0

    # if has_n_digits(seq[0], 2):
    #     number = abs(seq[0])
    #     digit_units = number % 10
    #     digit_tens = number // 10
    #     return digit_tens + digit_units + sum_digits_recursive(seq[1:])
    # return sum_digits_recursive(seq[1:])

    number = seq[0]
    sum_next = sum_digits_recursive(seq[1:])
    if has_n_digits(number, 2):
        return sum(digits(number)) + sum_next
    return sum_next


def sum_digits_comprehension(seq):
    """
    Returns the sum of the digits of all two-digit numbers
    in the given collection of numbers.
    """

    # return sum([abs(k) // 10 + abs(k) % 10 for k in seq if has_n_digits(k, 2)])
    return sum([sum(digits(number)) for number in seq if has_n_digits(number, 2)])


def sum_digits_map_filter(seq):
    """
    Returns the sum of the digits of all two-digit numbers
    in the given collection of numbers.

    Filter the non-two digit numbers, map the numbers to digits and calculate the sum.
    """

    # return sum(list(map(lambda n: abs(n) // 10 + abs(n) % 10, filter(lambda x: has_n_digits(x, 2), seq))))
    return sum(list(map(lambda nb: sum(digits(nb)), filter(has_n_digits, seq))))


if __name__ == "__main__":
    functions = [sum_digits_iterative, sum_digits_recursive,
                 sum_digits_comprehension, sum_digits_map_filter]

    for f in functions:
        print("Testing function:", f.__name__)
        assert f([]) == 0
        assert f([10, 44, 11]) == 11
        assert f([-1, -2, -3, 333, 320847]) == 0
        assert f([-42, -12, 1, 5, 9, 11, -88, 8430, 32, 23, 8, -2, 37]) == 47
        print("OK.")
