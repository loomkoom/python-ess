""" 
  Merge the given sorted sequences (in ascending order) into a new tuple using
  RECURSION. The resulting tuple contains all the elements (including 
  duplicates) of both given sequences in ascending order. If an element appears 
  n times in seq1 and m times in seq2, it appears n+m times in the new tuple.
  You may NOT use the sort function for this exercise. Use the fact that the 2 
  provided lists are already sorted to come up with a more efficient algorithm.
"""

def merge(seq1, seq2):
  if len(seq1) == 0:
    return tuple(seq2)
  elif len(seq2) == 0:
    return tuple(seq1)
  else:
    # Here we know both seq1 and seq2 are not empty and
    # we can compare the first elements of seq1 and seq2
    if seq1[0] > seq2[0]:
      seq1, seq2 = seq2, seq1
    # Here we know that seq1[0] <= seq2[0] and so seq1[0] 
    # is the smallest element of both seq1 and seq2. It must
    # therefore be the first element of the solution and we 
    # solve the rest of the problem with a recursive call.
    return (seq1[0],) + merge(seq1[1:], seq2)

assert merge((),()) == ()
assert merge((),(3,7,11)) == (3,7,11)
assert merge((3,7,11),()) == (3,7,11)
assert merge((14,),(3,7,11)) == (3,7,11,14)
assert merge((3,7,11),(2,18)) == (2,3,7,11,18)
assert merge((3,3,11),(4,12,12)) == (3,3,4,11,12,12)
assert merge((3,3),(3,3,8)) == (3,3,3,3,8)
assert merge("ace","bd") == ("a","b","c","d","e")
