"""
Write a function to check whether a given square matrix is symmetric.

A square matrix is symmetric if and only if each element at position [i][j]
is equal to the element at position [j][i].
"""

def is_symmetric(matrix):
    """ Check whether the given square matrix is a symmetric matrix.
    A square matrix is symmetric if each element below the main diagonal
    is equal to the symmetric position above the main diagonal."""

    i = 0
    while i < len(matrix):
        j = 0                           # altijd voor de while de while statement zetten om zeker te
        while j < len(matrix[i]):
            if matrix[i][j] != matrix[j][i]:
                return False
            j += 1
        i += 1
    return True


def is_symmetric(matrix):
    """ Check whether the given square matrix is a symmetric matrix.
    A square matrix is symmetric if each element below the main diagonal
    is equal to the symmetric position above the main diagonal."""

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

##TESTS
assert is_symmetric([ [10, 33, 44], [33, 20, 55], [44, 55, 30] ])
assert not is_symmetric([ [10, 33, 44], [33, 20, 55], [44, 56, 30] ])
assert is_symmetric([ [22] ])


