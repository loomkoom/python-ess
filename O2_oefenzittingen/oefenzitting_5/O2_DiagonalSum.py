"""
Write a function that calculates the sum of all the elements on the main
diagonal of a square matrix.

The main diagonal of a square matrix are all elements at positions [i][i].
"""

def diagonal_sum(matrix):
    """
    Calculate the sum of all the elements on the main diagonal of a
    square matrix.
    The main diagonal of a square elements collect all elements at
    positions [i][i].
    """
    val_sum = 0

    for i in range(len(matrix)):
        value = matrix[i][i]
        val_sum += value
    return val_sum

##TESTS

assert diagonal_sum([ [11, 33, 44], [33, 13, 55], [44, 55, 19] ]) == 43
assert diagonal_sum([ [22] ]) == 22
