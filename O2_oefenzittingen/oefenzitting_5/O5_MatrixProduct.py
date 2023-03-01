"""
Write a function to calculate the product of two matrices.

The product of two matrices is a matrix whose elements are equal to
the product of the elements at the corresponding row of the leftmost
matrix with the elements of the corresponding column of the rightmost matrix.
"""


def product(left, right):
    """ Return the product of the given matrices.
    The product of two matrices is a matrix whose elements
    are equal to the product of the corresponding row of
    the leftmost matrix with the corresponding column of
    the rightmost matrix.
    """

    if len(left[0]) != len(right):
        return None

    result = [[0 for c in range(len(right[0]))] for r in range(len(left))]

    for i in range(len(left)):  # row left
        for j in range(len(right[0])):  # col right
            for k in range(len(right)):  # row right
                result[i][j] += left[i][k] * right[k][j]
    return result


##TESTS
matrix1 = [[1, 2, 3],
           [4, 5, 6]]
matrix2 = [[10, 20],
           [30, 40],
           [50, 60]]
assert product(matrix1, matrix2) == \
       [[220, 280],
        [490, 640]]

matrix1 = [[2]]
matrix2 = [[3]]
assert product(matrix1, matrix2) == [[6]]
