def index_smallest_of(sequence, start=0):

  """
    Return the position of the smallest element in the
    given sequence starting from the given position.
    - If several smallest elements can be found, the
      function returns the position of the leftmost
      smallest element.
    - None is returned if no such smallest element can be
      found.
  """

  if (start < 0) or (start >= len(sequence)):
    return None

  ind_smallest = start
  ind_current = start+1

  while ind_current < len(sequence):
    if sequence[ind_current] < sequence[ind_smallest]:
      ind_smallest = ind_current
    ind_current += 1

  return ind_smallest


assert index_smallest_of((77,-20,-4,100),0) == 1
assert index_smallest_of((-9,4,-20,-20,1,-20,-1),1) == 2
assert index_smallest_of((-300,-20,-4,100),0) == 0
assert index_smallest_of((-80,20,-4,-100),2) == 3
assert index_smallest_of("cbabc",0) == 2
assert index_smallest_of((),0) == None
assert index_smallest_of((1,2,3),3) == None
assert index_smallest_of((1,2,3),-1) == None
