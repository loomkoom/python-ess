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
    pass


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
