"""
Pascal's triangle is a triangular scheme that lists the binomial
coefficients (search the internet for more information). Each of
the rows of the triangle consists of adding together adjacent
numbers in the row exactly above:

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# """


def next_sum(lst):
    if len(lst) == 1:
        return []
    return [lst[0] + lst[1]] + next_sum(lst[1:])


def pascal_triangle(n):
    if n == 0:
        return [1]
    previous_row = pascal_triangle(n - 1)
    new_row = [1] + next_sum(previous_row) + [1]
    return new_row


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
