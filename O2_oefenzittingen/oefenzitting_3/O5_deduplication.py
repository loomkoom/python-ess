def average_number_from_string(str):
    sum = 0

    for n in range(len(str)):
        sum += int(str[n])
    avg = sum / len(str)

    return avg

def average_number(ints1, ints2):
    """A function that takes two strings of numbers as arguments.
    For each string individually we calculate the average of the numbers.

    Both results are concatenated into a
    string and returned in the form: return str(ints1_avg) + " : " + str(ints2_avg)

    This functions contains code duplication. You will notice that two sections
    of the implementation are nearly identical. Code duplication is bad
    practice since it also duplicates bugs and makes code harder to
    read/maintain. Create a helper function 'average_number_from_string' to
    move the duplication to a function. Call 'average_number_from_string' from
    'average_number' to keep the same functionality.

    Some example calls for the function:
    average_number("1234", "5678") # returns: "2.5 : 6.5"
    average_number("5678", "1234") # returns: "6.5 : 2.5"

    Conclusion: Duplication in real application code is often more subtle than
    the duplication demonstrated here, but a thing to keep in mind is that
    copy-pasting code is never a good idea and you should encapsulate that bit
    in a function instead. (You don't want to copy-paste a bug twenty times
    only to figure it out an hour later!)

    """

    avg_1 = average_number_from_string(ints1)
    avg_2 = average_number_from_string(ints2)

    return str(avg_1) + " : " + str(avg_2)

    # n = 0
    # ints1_sum = 0
    #
    # while n < len(ints1):
    #     ints1_sum += int(ints1[n])
    #     n += 1
    #
    # ints1_avg = ints1_sum / len(ints1)
    #
    #
    # n = 0
    # ints2_sum = 0
    #
    # while n < len(ints2):
    #     ints2_sum += int(ints2[n])
    #     n += 1
    #
    # ints2_avg = ints2_sum / len(ints2)
    #
    # return str(ints1_avg) + " : " + str(ints2_avg)





assert average_number("1234", "5678") == "2.5 : 6.5"
assert average_number("5678", "1234") == "6.5 : 2.5"
