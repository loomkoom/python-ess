"""
In the course notes and lecture example, bubble sort is worked out with the outer loop going right to left.
Write an alternative implementation of bubble sort that goes from left to right,
analyze the time complexity for worst and best case, and perform measurements to verify your results.

Your implementation should modify the list itself, but also return the list at the end (for convenient testing).
"""
def bubblesort_left_to_right(lst):
    # TODO
    return lst

assert bubblesort_left_to_right([]) == []
assert bubblesort_left_to_right([1]) == [1]
assert bubblesort_left_to_right([3, 2, 1]) == [1, 2, 3]
assert bubblesort_left_to_right([1, 2, 3]) == [1, 2, 3]
assert bubblesort_left_to_right([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert bubblesort_left_to_right([9, 5, 1, 8, 2, 3, 7, 6, 4, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]