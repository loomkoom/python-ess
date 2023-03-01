"""
Implement a functional version of the quicksort algorithm. The function quicksort(compare, list) should return a new
list `result' with the same elements as the given list such that compare(result[i],result[i+1]) <= 0 for all i.

1. Choose an element from the list, this is called the `pivot'.
2. Split the remainder of the list (without the pivot) in two parts: the first part contains all elements x such that
   compare(x,pivot) <= 0, the second part contains the rest.
3. Recursively sort the two shorter lists and paste the results together to form a sorted list.
"""


def quicksort(compare, lst):
    """
    Returns a new list `result' with the same elements as 
    the given list such that 
    compare(result[i],result[i+1]) <= 0 for all i.
    """
    if len(lst) < 2:
        return lst

    pivot = lst[0]
    rest = lst[1:]
    smaller = list(filter(lambda x: compare(x, pivot) <= 0, rest))
    larger = list(filter(lambda x: compare(x, pivot) > 0, rest))

    return quicksort(compare, smaller) + [pivot] + quicksort(compare, larger)


# The functions below are used for testing, don't change them
def is_sorted(compare, lst):
    """
    Checks if the given list is sorted according to the given compare function.
    """
    return all(compare(lst[i], lst[i + 1]) <= 0 for i in range(0, len(lst) - 1))


def is_permutation(lst1, lst2):
    """
    Checks whether the two given lists are permutations of each other
    """
    from collections import Counter
    return Counter(lst1) == Counter(lst2)


compare1 = lambda x, y: abs(x) - abs(y)
list1 = range(-10, 10)
sorted1 = quicksort(compare1, list1)
assert is_sorted(compare1, sorted1)
assert is_permutation(list1, sorted1)

compare2 = lambda x, y: x % 10 - y % 10
list2 = range(0, 100, 7)
sorted2 = quicksort(compare2, list2)
assert is_sorted(compare2, sorted2)
assert is_permutation(list2, sorted2)
