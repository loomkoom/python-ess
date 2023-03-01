def matching_subsum(seq, sum):
    """ Return a tuple of numbers from the given sequence whose
    total is equal to the given sum. The function returns None,
    if no such tuple can be formed."""

    if sum == 0:
        return ()
    elif len(seq) == 0:
        return None
    else:
        # Try to get a matching sum including the first element.
        result = matching_subsum(seq[1:], sum - seq[0])
        if result is not None:
            return (seq[0],) + result
        else:
            # Try to get a matching sum without the first element.
            return matching_subsum(seq[1:], sum)


assert matching_subsum((), 0) == ()
assert matching_subsum((), -1) == None
assert matching_subsum((0,), 0) == () or \
       matching_subsum((0,), 0) == (0,)
assert matching_subsum((4,), 4) == (4,)
assert matching_subsum((5,), -1) == None
assert matching_subsum((1, 5, 9, 13), 14) == (1, 13) or \
       matching_subsum((1, 5, 9, 13), 14) == (13, 1) or \
       matching_subsum((1, 5, 9, 13), 14) == (5, 9) or \
       matching_subsum((1, 5, 9, 13), 14) == (9, 5)
assert matching_subsum((1, 2, 3), 3) == (1, 2) or \
       matching_subsum((1, 2, 3), 3) == (3,)
assert matching_subsum((0, 3, 0, 4, -7), 3) == (3,) or \
       matching_subsum((0, 3, 0, 4, -7), 3) == (0, 3,) or \
       matching_subsum((0, 3, 0, 4, -7), 3) == (3, 0,) or \
       matching_subsum((0, 3, 0, 4, -7), 3) == (0, 0, 3,) or \
       matching_subsum((0, 3, 0, 4, -7), 3) == (0, 3, 0,) or \
       matching_subsum((0, 3, 0, 4, -7), 3) == (3, 0, 0,) or \
       matching_subsum((0, 3, 0, 4, -7), 3) == (4, -7) or \
       matching_subsum((0, 3, 0, 4, -7), 3) == (-7, 4)
