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


def pascal_triangle(n):
    """
    A function that returns the n-th row, starting at 0, of
    Pascal's triangle, in a recursive manner.
    """
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    else:
        pt = pascal_triangle(n-1)
        return [1] + [pt[i]+pt[i+1] for i in range(0,len(pt)-1)] + [1]


if __name__ == "__main__":
    print("Tests..."),
    assert pascal_triangle(0) == [1]
    assert pascal_triangle(1) == [1, 1]
    assert pascal_triangle(2) == [1, 2, 1]
    assert pascal_triangle(3) == [1, 3, 3, 1]
    assert pascal_triangle(4) == [1, 4, 6, 4, 1]
    assert pascal_triangle(5) == [1, 5, 10, 10, 5, 1]
    assert pascal_triangle(10) == [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
    print("done.")
