"""
Write a function that prints the elements of a given matrix row by row. Use one line per row.
Write another function that prints the elements of a given matrix column by column. Use one line per column.
"""


def print_by_row(matrix):
    """ Print the elements of the given matrix, row by row."""
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col],end=' ')
        print()

def print_by_column(matrix):
    """ Print the elements of the given matrix, column by column."""
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            print(matrix[row][col], end = ' ')
        print()

##TESTS
matrix = [[10, 11, 12], [20, 21, 22]]

print("Matrix row by row")
print_by_row(matrix)
# Expected print-out
# 10 11 12
# 20 21 22
print("\n")

print("Matrix column by column")
print_by_column(matrix)
# Expected print-out
# 10 20
# 11 21
# 12 22
