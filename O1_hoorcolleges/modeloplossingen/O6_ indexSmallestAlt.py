def index_smallest_of(*values):
  """
    Return the position of the smallest element in the
    given sequence of values.
    - If several smallest elements can be found, the
      function returns the position of the leftmost
      smallest element.
    - None is returned if no such smallest element can be
      found.
  """

  if len(values) == 0:
    return None

  ind_smallest = 0
  ind_current = 1

  while ind_current < len(values):

    if values[ind_current] < values[ind_smallest]:
      ind_smallest = ind_current

    ind_current += 1

  return ind_smallest



assert index_smallest_of(77,-20,-4,100) == 1
assert index_smallest_of(-9,4,-20,-20,1,-20,-1) == 2
assert index_smallest_of(-300,-20,-4,100) == 0
assert index_smallest_of(-80,20,-4,-100) == 3
assert index_smallest_of() == None
assert index_smallest_of(3) == 0