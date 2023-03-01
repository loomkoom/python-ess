ALL_EQUAL = 0
ASCENDING = 1
DESCENDING = 2
UNORDERED = -1


def get_ordering(seq):
  """
    Return the ordering of the elements of the given
    sequence. The function returns one of the following
    values:
      ALL_EQUAL: all elements are equal to one another.
      ASCENDING: elements are in ascending order and at
        least one element is strict smaller than its
        successor.
      DESCENDING: elements are in descending order and at
        least one element is strict smaller than its
        successor.
      UNORDERED: elements are not ordered. At least one
        element is strict smaller than its successor and
        at least one element is strict greater than its
        successor.
  """

  all_equal = True
  all_less_than_or_equal = True
  all_greater_than_or_equal = True
  current_pos = 1

  while (all_less_than_or_equal or \
               all_greater_than_or_equal or all_equal) \
        and current_pos < len(seq):

    if seq[current_pos - 1] > seq[current_pos]:
      all_less_than_or_equal = False
      all_equal = False
    elif seq[current_pos - 1] < seq[current_pos]:
      all_greater_than_or_equal = False
      all_equal = False

    current_pos += 1

  if all_equal:
    return ALL_EQUAL
  elif all_less_than_or_equal:
    return ASCENDING
  elif all_greater_than_or_equal:
    return DESCENDING
  else:
    return UNORDERED


assert get_ordering(()) == ALL_EQUAL
assert get_ordering((1,)) == ALL_EQUAL

assert get_ordering((1, 2, 3)) == ASCENDING
assert get_ordering((1, 1, 2)) == ASCENDING

assert get_ordering((3, 2, 1)) == DESCENDING
assert get_ordering((3, 3, 1)) == DESCENDING

assert get_ordering((3, 3, 3)) == ALL_EQUAL

assert get_ordering((3, 4, 2)) == UNORDERED
