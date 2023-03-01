from O6_IndexSmallest import index_smallest_of
def sort(lst):

    """
        Sort the elements of the given list in ascending
        order.
    """

    for index_current in range(0, len(lst)-1):
        index_smallest = index_smallest_of(lst, index_current)
        lst[index_current], lst[index_smallest] = \
            lst[index_smallest], lst[index_current]

# Empty list
lst = []
sort(lst)
assert len(lst) == 0

# List with one element
lst = [20]
sort(lst)
assert (len(lst) == 1) and (lst[0] == 20)

# List with several elements
lst = [10, 20, -100]
lst2 = lst
sort(lst)
assert (len(lst) == 3) and (lst[0] == -100) and \
       (lst[1] == 10) and (lst[2] == 20)
assert lst is lst2




def sort(lst):

    """
        Sort the elements of the given list in ascending
        order.
    """

    index_current = 0

    while index_current < len(lst):
        index_smallest = index_smallest_of(lst, index_current)

        lst[index_current], lst[index_smallest] =\
            lst[index_smallest], lst[index_current]

        index_current += 1


# Empty list
lst = []
sort(lst)
assert len(lst) == 0

# List with one element
lst = [20]
sort(lst)
assert (len(lst) == 1) and (lst[0] == 20)

# List with several elements
lst = [10, 20, -100]
lst2 = lst
sort(lst)
assert (len(lst) == 3) and (lst[0] == -100) and\
       (lst[1] == 10) and (lst[2] == 20)
# ! The assertion below is not needed. A function is able to
# ! change individual elements of a list. A function is no able
# ! to replace the entire list supplied to it by some other list.
assert lst is lst2
