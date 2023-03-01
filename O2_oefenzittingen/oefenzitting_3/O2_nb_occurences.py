"""A function that counts the number of occurrences of a given letter in a given string.
The function must accept the letter as its first argument and the string as second argument.
The function must always return an integer value.

Some example outputs for given inputs:
'e', "methodiek van de informatica"         3
't',"hottentottententententoonstelling"     10
'a', "python"                               0


At the bottom of this file we test for expected behavior using 'assert'. If you
define a function named 'nb_occurrences' you can run this file (which runs the
assertions) to test your implementation. An 'assert' checks a boolean value and
crashes the program with an error if that boolean is false, e.g. assert 1 == 0.

This approach of having automated test cases makes programming easier. Add your
own tests throughout your exercises!

"""

def nb_occurences(letter,str):

    nb = 0

    for index in range(len(str)):
        if str[index] == letter:
            nb += 1
    return nb


# EXTENSION
"""
A function that examines whether two strings have the same number of occurences
of a specific letter.
The function must accept the letter as first argument and the two string to compare as second and third argument.
The function must always return a boolean.
"""

def has_equal_occurences(letter,str_1,str_2):

    nb_1 = 0
    nb_2 = 0

    for index in range(len(str_1)):
        if str_1[index] == letter:
            nb_1 += 1
    for index in range(len(str_2)):
        if str_2[index] == letter:
            nb_2 += 1

    if nb_2 == nb_1:
        return True
    return False


# TESTS
assert nb_occurences('e', "methodiek van de informatica") == 3
assert nb_occurences('t',"hottentottententententoonstelling") == 10
assert nb_occurences('a', "python") == 0


# TESTS extension
assert has_equal_occurences('e', "methodiek van de informatica", "burgerlijk ingenieur") == True
assert has_equal_occurences('o',"python", "toledo" ) == False
