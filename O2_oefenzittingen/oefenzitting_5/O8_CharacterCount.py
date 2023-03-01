"""
Write a function that counts the amount of occurrences of each character in a
given string. The function should return a dictionary with the characters as
keys, and the number of occurrences of the character as value
"""


def character_count(str):
    """
    Calculate the number of occurrences for each character in the string.
    Return a dictionary containing the number of occurrences for each character
    in the string
    """
    dic = {}

    for i in str:
        dic[i] = dic.get(i, 0) + 1
    return dic


##TESTS
assert character_count("") == {}
assert character_count("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
assert character_count("abracadabra") == \
       {'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
assert character_count("aibohphobia") == \
       {'a': 2, 'b': 2, 'i': 2, 'h': 2, 'o': 2, 'p': 1}
assert character_count("comproportionation") == \
       {'a': 1, 'c': 1, 'i': 2, 'm': 1, 'o': 5, 'n': 2, 'p': 2, 'r': 2, 't': 2}
assert character_count("abcdefghijklmnopqrstuvwxyz") == \
       {'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'h': 1, 'f': 1, 'i': 1,
        'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1,
        'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}
