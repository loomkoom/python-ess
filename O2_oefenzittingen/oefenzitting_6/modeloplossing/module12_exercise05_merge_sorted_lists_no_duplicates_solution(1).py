""" 
  Merge the given sorted sequences (in ascending order) into a new tuple using
  RECURSION. The resulting tuple contains all the elements of both given 
  sequences in ascending order, but NO DUPLICATES. You may NOT use the sort 
  function for this exercise. Use the fact that the 2 
  provided lists are already sorted to come up with a more efficient algorithm.
"""

def merge_do_duplicates(seq1, seq2):
  if len(seq1) == 0 and len(seq2) == 0:
    return ()
  else:
    # For the recursive call further on, we would like to have the 
    # smallest element of both seq1 and seq2 to be in seq[0].
    if (len(seq1) == 0) or \
       (len(seq2) != 0 and seq1[0] > seq2[0]):
      seq1, seq2 = seq2, seq1
    # Here we know that seq1[0] is the smallest element of 
    # both seq1 and seq2. It must therefore be the first 
    # element of the solution and we solve the rest of the 
    # problem with a recursive call. 
    rest = merge_do_duplicates(seq1[1:], seq2)
    # To prevent duplicates we must check whether the first 
    # elemenet of the recurive solution (i.e. rest[0]), if any, 
    # is equal to seq1[0]
    if len(rest) == 0 or seq1[0] != rest[0]:
      return (seq1[0],) + rest
    else:
      return rest

assert merge_do_duplicates((),()) == ()
assert merge_do_duplicates((),(3,7,11)) == (3,7,11)
assert merge_do_duplicates((3,7,11),()) == (3,7,11)
assert merge_do_duplicates((14,),(3,7,11)) == (3,7,11,14)
assert merge_do_duplicates((3,7,11),(2,18)) == (2,3,7,11,18)
assert merge_do_duplicates((3,3,11),(4,12,12)) == (3,4,11,12)
assert merge_do_duplicates((3,3),(3,3,8)) == (3,8)
assert merge_do_duplicates("ace","bd") == ("a","b","c","d","e")
