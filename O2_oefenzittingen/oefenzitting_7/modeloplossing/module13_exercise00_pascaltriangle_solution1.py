"""
Pascal's triangle is a triangular scheme that lists the binomial
coefficients (search the internet for more information). Each of
the rows of the triangle consists of adding together adjacent
numbers in the row exactly above:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
"""


def pascal_triangle(n, previous_row=[1]):
    """
    A function that returns the n-th row of Pascal's triangle,
    in a recursive manner. The first row in the triangle is [1],
    with n == 0.
    """

    if n == 0:
        return previous_row
    else:
        new_row = [1]

        i = 1
        while i < len(previous_row):
            # LOOP INVARIANT:
            # The elements in 'new_row' at position p, in range 0..i-1,
            # are the correct pascal triangle numbers, based on the
            # elements in 'row' (the previous row).
            new_row += [previous_row[i - 1] + previous_row[i]]
            i += 1

        new_row += [1]

        return pascal_triangle(n - 1, new_row)


def pascal_triangle_full(n, row=0, col=1, triangle=[[1]]):
    """
    A function that returns the n-th row of Pascal's triangle,
    in a recursive manner. The first row in the triangle is [1],
    with n == 0.

    This implementation doesn't use any internal loops.
    """
    # n rows have been completed (row_1 - row_n)
    if row == n + 1:
        return triangle[n]
    # at the end of a row, start new row
    elif col == row + 1:
        return pascal_triangle_full(n, row + 1, 0, triangle + [[]])
    # in the process of completing a row
    else:
        # handle no-left coefficient
        # line is a conditional expression,
        # see http://docs.python.org/2.5/whatsnew/pep-308.html
        left = 0 if col == 0 else triangle[row - 1][col - 1]
        # handle no-right coefficient
        right = 0 if col == row else triangle[row - 1][col]
        coeff = left + right

        # add coefficient at the end of the current row
        triangle[row] += [coeff]
        # move one column to the right
        return pascal_triangle_full(n, row, col + 1, triangle)


if __name__ == "__main__":
    result = \
        [[1],
         [1, 1],
         [1, 2, 1],
         [1, 3, 3, 1],
         [1, 4, 6, 4, 1],
         [1, 5, 10, 10, 5, 1],
         [1, 6, 15, 20, 15, 6, 1],
         [1, 7, 21, 35, 35, 21, 7, 1],
         [1, 8, 28, 56, 70, 56, 28, 8, 1],
         [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
         [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]]

    print("Tests..."),
    for i in range(len(result)):
        assert result[i] == pascal_triangle(i) == pascal_triangle_full(i)
    print("done.")
