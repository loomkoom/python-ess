def length_plateau_at(seq, start):
    """
      Return the length of the plateau starting at the
      given position in the given sequence.
      - All elements in seq[start:start+result] are equal,
        and either start+result is just beyond the last
        element of the sequence or the element at position
        start+result is different from the element at
        position start.
    """

    pass


##TESTS for length_plateau_at
# Plateau in the middle
seq = (1, 2, 3, 3, 3, 4, 5)
assert length_plateau_at(seq, 2) == 3
# Plateau at the start
seq = (1, 1, 3, 7, 9)
assert length_plateau_at(seq, 0) == 2
# Plateau at the end
seq = (1, 2, 3, 3, 3, 3, 3)
assert length_plateau_at(seq, 2) == 5
# Singleton sequence
seq = [1]
assert length_plateau_at(seq, 0) == 1


def find_longest_plateau(seq):
    """
      Return the index of the longest plateau in the given
      sequence.
      - A plateau is defined as a sequence of successive
        elements that are identical.
    """

    start_longest_plateau_so_far  = 0
    length_longest_plateau_so_far = length_plateau_at(seq,0)
    index = length_longest_plateau_so_far

    # INVARIANT
    # er is geen langer plateau dan het langste to nu toe geinitialiseerd
    while len(seq)- index < length_longest_plateau_so_far:

        assert all([ length_plateau_at(seq,pos) <= length_longest_plateau_so_far
                     for pos in range(0,index)])

        length_current_plateau = length_plateau_at(seq,index)
        if length_current_plateau > length_longest_plateau_so_far:
            start_longest_plateau_so_far = index
            length_longest_plateau_so_far = length_current_plateau

        index += length_current_plateau

    return start_longest_plateau_so_far


##TESTS for find_longest_plateau
# Longest plateau in the middle
seq = (1, 2, 3, 3, 3, 4, 5)
assert find_longest_plateau(seq) == 2
# Longest plateau at the start
seq = (1, 1, 3, 7, 9)
assert find_longest_plateau(seq) == 0
# Longest plateau at the end
seq = (1, 2, 3, 3, 3, 3, 3)
assert find_longest_plateau(seq) == 2
# Longest plateau at the end, just one element longer than longest so far.
seq = (1, 2, 3, 3)
assert find_longest_plateau(seq) == 2
# Empty sequence
seq = tuple()
assert find_longest_plateau(seq) == 0
# Singleton sequence
seq = (1,)
assert find_longest_plateau(seq) == 0
# Longest plateau covers entire sequence.
seq = (1, 1, 1, 1,)
assert find_longest_plateau(seq) == 0
