"""
Write a function to calculate the sum of two matrices.

The sum of two matrices is a matrix whose elements are equal to
the sum of the elements at the corresponding positions in the given matrices.
"""


def sum(left, right):
    """ Return the sum of the given matrices.
    The sum of two matrices is a matrix whose elements are
    equal to the sum of the elements at corresponding positions.
    """

    if len(left) != len(right) or len(left[0]) != len(right[0]):
        return None

    sum = [[0 for col in range(len(left[0]))] for row in range(len(left))]

    for i in range(len(left)):
        for j in range(len(left[i])):
            sum[i][j] = left[i][j] + right[i][j]

    return sum


##TESTS
mat1 = [[11, 22, 33],
        [44, 55, 66]]
mat2 = [[100, 200, 300],
        [400, 500, 600]]
assert sum(mat1, mat2) == \
       [[111, 222, 333],
        [444, 555, 666]]

mat1 = [[22]]
mat2 = [[33]]
assert sum(mat1, mat2) == [[55]]
