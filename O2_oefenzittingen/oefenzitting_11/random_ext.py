import random


def random_list(size):
    """
    Generate a random list of integers of the given size.
    The generated list contains integers from -size to size.
    """
    return [random.randint(-size, size) for _ in range(size)]


def random_dict(size):
    """
    Generate a random dictionary of the given size.
    The generated dictionary contains the numbers 1..size as keys, and random strings of length 5 as values.
    """
    result = {}
    for i in range(size):
        result[i+1] = random_string(5)
    return result


def random_string(size):
    """
    Generate a random string of the given size.
    The generated string only contains alphanumeric characters.
    """
    from string import digits, ascii_uppercase, ascii_lowercase
    charset = digits + ascii_uppercase + ascii_lowercase
    result = ""
    for i in range(size):
        result += random.choice(charset)
    return result


def random_number(nb_digits):
    """
    Generate a random number with the given number of digits.
    The generated number contains digits from 1 to 9.
    """
    result = random.randint(1, 9)
    for i in range(nb_digits-1):
        result = result*10 + random.randint(0, 9)
    return result

if __name__ == "__main__":
    print(random_list(3))
    print(random_dict(3))
    print(random_string(3))
    print(random_number(3))