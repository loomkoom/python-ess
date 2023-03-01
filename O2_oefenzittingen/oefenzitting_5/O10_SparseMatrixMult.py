"""
 Write a function that multiplies two sparse matrices
 The keys of the sparse matrices are row-column tuples = '(row,column)'
 The values are corresponding values of the matrix
 Dense matrix = {(row, column): value}
"""


def sparse_matrix_mult(matrixA, matrixB):
    """
    Calculate the product of given 2 sparse matrices
    Return a new sparse matrix of the same format '{(row, column): value}'
    """

    result = {}

    for akey in matrixA:  # row,column A
        for bkey in matrixB:  # row,column B
            if akey[1] == bkey[0]:
                key = akey[0], bkey[1]

                if key not in result:
                    result[key] = 0
                result[key] += matrixA[akey] * matrixB[bkey]

    print(result, "\n")
    return result


##TESTS
assert sparse_matrix_mult({(0, 0): 2},
                          {(0, 0): 4}) \
       == {(0, 0): 8}
assert sparse_matrix_mult({(0, 0): 1, (0, 1): 2, (1, 0): 3, (1, 1): 4},
                          {(0, 0): 2, (0, 1): 0, (1, 0): 1, (1, 1): 2}) \
       == {(0, 1): 4, (1, 0): 10, (0, 0): 4, (1, 1): 8}

assert sparse_matrix_mult({(10, 10): 2, (100, 10): 3, (50, 80): 4},
                          {(10, 5): 10, (10, 8): 100}) \
       == {(100, 5): 30, (10, 8): 200, (10, 5): 20, (100, 8): 300}
