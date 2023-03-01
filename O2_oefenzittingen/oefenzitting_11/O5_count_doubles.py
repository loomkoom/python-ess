"""
Write a program, that given a list of integers, counts all duplicate values that are present in the list.
E.g. for the list [4, 6, 3, 2, 4, 1, 8, 3, 8], there are 3 duplicate values: 4, 3, and 8.

If the list would contain more than 2 items with same value, count each possible pair of duplicates.
E.g. in the list [2, 2, 1, 2, 2], count 6 duplicates
(note: this makes the program easier, not harder! :-))

What is the time complexity of your algorithm?
Can you do better if the list would be sorted?
"""


def count_doubles(seq):
    pass


assert count_doubles([]) == 0
assert count_doubles([1, 1]) == 1
assert count_doubles([1, 1, 1]) == 3
assert count_doubles([2, 2, 1, 2, 2]) == 6
assert count_doubles([4, 6, 3, 2, 4, 1, 8, 3, 8]) == 3


def count_doubles_sorted(seq):
    return count_doubles(seq)


assert count_doubles_sorted([]) == 0
assert count_doubles_sorted([1, 1]) == 1
assert count_doubles_sorted([1, 1, 1]) == 3
assert count_doubles_sorted([1, 2, 2, 2, 2]) == 6
assert count_doubles_sorted([1, 2, 3, 3, 4, 4, 6, 8, 8]) == 3
