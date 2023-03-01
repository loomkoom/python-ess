def is_sorted(*values):

  """
    Check whether the elements of the given sequence are
    sorted in ascending order.
  """

  current_pos = 1

  while current_pos < len(values):

    if values[current_pos-1] > values[current_pos]:
      return False
    current_pos += 1

  return True


assert is_sorted()
assert is_sorted(1,2,6,6,8)
assert not is_sorted(1,0,4,6,8)
assert not is_sorted(1,2,3,4,5,4)
