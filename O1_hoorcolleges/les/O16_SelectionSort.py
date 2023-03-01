def index_smallest_of(sequence, start_index=0):
    """
      Return the position of the smallest element
      in the given sequence starting from the given
      position.
      If several smallest elements can be found, the
      function returns the position of the leftmost
      smallest element.
      None is returned if no such smallest element
      can be found.
    """

    if (start_index < 0) or \
            (start_index >= len(sequence)):
        return None

    ind_smallest = start_index
    ind_current = start_index + 1

    # INVARIANT

    while ind_current < len(sequence):
        if sequence[ind_current] < \
                sequence[ind_smallest]:
            ind_smallest = ind_current
        ind_current += 1

    return ind_smallest


def sort(lst):
    """
      Sort the elements of the given list in ascending
      order.
    """

    index_current = 0

    # INVARIANT
    # Alle elementen in het behandeld/gesorteerd stuk zijn gesorteerd van klein naar groot
    # alle elementen in het behandeld/gesorteerd deel zijn kleiner of gelijk aan dan het andere deeel
    while index_current < len(lst):
        assert all([lst[index] <= lst[index + 1]
                    for index in range(0, index_current - 1)])
        assert all([lst[index1] <= lst[index2]
                    for index1 in range(0, index_current)
                    for index2 in range(index_current, len(lst))])

        index_smallest = index_smallest_of(lst, index_current)
        lst[index_current], lst[index_smallest] = \
            lst[index_smallest], lst[index_current]
        index_current += 1


# Empty list
lst = []
sort(lst)
assert len(lst) == 0

# List with one element
lst = [20]
sort(lst)
assert lst == [20]

# List with several elements
lst = [10, 20, -100]
lst2 = lst
sort(lst)
assert lst == [-100, 10, 20]
# ! The assertion below is not needed. A function is able to
# ! change individual elements of a list. A function is not able
# ! to replace the entire list supplied to it by some other list.
assert lst is lst2
