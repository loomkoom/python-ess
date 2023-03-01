def is_sorted(seq):

  """
    Check whether the elements of the given sequence are
    sorted in ascending order.
  """

  current_pos = 1

  while current_pos < len(seq):

    if seq[current_pos-1] > seq[current_pos]:
      return False
    current_pos += 1

  return True


assert is_sorted(())
assert is_sorted((1,2,6,6,8))
assert not is_sorted((1,0,4,6,8))
assert not is_sorted((1,2,3,4,5,4))

print(is_sorted("sorted"))
#print(is_sorted((1,True,4.5,"abc")))
#print(is_sorted((1,None)))
#print(is_sorted((None,1)))
print(is_sorted(((1,2),(3,4,5),(3,4,5,6))))
