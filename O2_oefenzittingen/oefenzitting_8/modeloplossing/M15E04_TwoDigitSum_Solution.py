from math import log10, floor


def has_n_digits(number, digits=2):
    """
    Returns true if the given number consists of exactly n digits,
    otherwise return false.
    """
    return digits == floor(log10(abs(number))) + 1


def digits(number):
    """
    Returns a sequence of all the individual digits in the number,
    in order.
    """
    number = abs(number)
    seq = []
    while number:
        seq.append(number % 10)
        number = number // 10
    seq.reverse()
    return seq


def sum_digits_iterative(seq):
    """
    Returns the sum of the digits of all two-digit numbers
    in the given collection of numbers.
    """
    sum = 0
    for number in seq:
        if has_n_digits(number, 2):
            number = abs(number)
            digit_units = number % 10
            digit_tens = number // 10
            sum += digit_units + digit_tens
    return sum


def sum_digits_recursive(seq):
    """
    Returns the sum of the digits of all two-digit numbers
    in the given collection of numbers.
    """
    if not seq:
        return 0
    else:
        summ = sum_digits_recursive(seq[1:])
        number = seq[0]
        if has_n_digits(number, 2):
            summ = summ + sum(digits(number))
        return summ


def sum_digits_comprehension(seq):
    """
    Returns the sum of the digits of all two-digit numbers
    in the given collection of numbers.
    """
    return sum([sum(digits(number)) for number in seq if has_n_digits(number, 2)])


def sum_digits_map_filter(seq):
    """
    Returns the sum of the digits of all two-digit numbers
    in the given collection of numbers.

    Filter the non-two digit numbers, map the numbers to digits and calculate the sum.
    """
    new_seq = list(map(lambda x: sum(digits(x)),filter(has_n_digits,seq)))

    return sum(new_seq)


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