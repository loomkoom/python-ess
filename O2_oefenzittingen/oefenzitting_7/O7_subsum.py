def matching_subsum(seq, sum, current_solution = ()):
    """ Return a tuple of numbers from the given sequence whose
    total is equal to the given sum. The function returns None,
    if no such tuple can be formed."""

    seq = sorted(seq, reverse = True)
    if sum == 0:
        return current_solution

    for nb in seq:
        if nb <= sum:
            current_solution += (nb,)
            current_solution = matching_subsum(seq, sum - nb, current_solution)
            if current_solution != ():
                return current_solution

    return None


def matching_subsum(seq, sum):
    """ Return a tuple of numbers from the given sequence whose
    total is equal to the given sum. The function returns None,
    if no such tuple can be formed."""

    if sum == 0:
        return ()
    elif not seq:
        return None
    else:
        # probeer 1e element met de rest
        result = matching_subsum(seq[1:], sum - seq[0])
        if result is not None:
            return (seq[0],) + result
        # probeer alles zonder 1e element
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
       matching_subsum((1, 2, 3), 3) == (2, 1) or \
       matching_subsum((1, 2, 3), 3) == (3,)
assert matching_subsum((0, 3, 0, -4, 7), 3) == (3,) or \
       matching_subsum((0, 3, 0, -4, 7), 3) == (0, 3,) or \
       matching_subsum((0, 3, 0, -4, 7), 3) == (3, 0,) or \
       matching_subsum((0, 3, 0, -4, 7), 3) == (0, 0, 3,) or \
       matching_subsum((0, 3, 0, -4, 7), 3) == (0, 3, 0,) or \
       matching_subsum((0, 3, 0, -4, 7), 3) == (3, 0, 0,) or \
       matching_subsum((0, 3, 0, -4, 7), 3) == (-4, 7) or \
       matching_subsum((0, 3, 0, -4, 7), 3) == (7, -4)
