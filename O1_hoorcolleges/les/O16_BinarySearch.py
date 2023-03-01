def binary_search(seq, val, start=0, end=None):
    """
      Check whether the given value is part of the slice
      seq[start:end].
      - The given sequence must be sorted in ascending
        order.
      - A default value of None for the end position
        actually means a value of len(seq).
    """

    if end == None:
        end = len(seq)

    orig_start = start
    orig_end = end

    # INVARIANT
    # Alle elementen tussen orig_start en start zijn kleiner dan val.
    # Alle elmenten tussen end en orig_end zijn groter dan val
    while start < end:
        assert all([seq[index] < val for index in range(orig_start,start)])                         # Lijst van booleaanse waarden !
        # assert all([elem < val for elem in seq[orig_start:start]])

        assert all([seq[index] > val for index in range(end,orig_end)])
        # assert all([elem > val for elem in seq[end:orig_end]])

        mid = (start + end) // 2

        if seq[mid] == val:
            return True
        elif seq[mid] < val:
            start = mid + 1
        else:
            end = mid

    return False


assert binary_search((2, 4, 6, 7, 9, 12, 33, 77), 33)
assert binary_search((2,), 2)
assert not binary_search((2, 4, 6, 7, 9, 12, 33, 77), 11)
assert not binary_search((2, 4, 6, 8, 10), 8, 0, 2)
assert not binary_search((2, 4, 6, 8, 10), 4, 2)
assert not binary_search((2, 5, 7), 5, 2, 1)
assert not binary_search((), 5)
