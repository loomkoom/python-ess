""" 
  Merge the given sorted sequences (in ascending order) into a new tuple using
  RECURSION. The resulting tuple contains all the elements of both given 
  sequences in ascending order, but NO DUPLICATES. You may NOT use the sort 
  function for this exercise. Use the fact that the 2 
  provided lists are already sorted to come up with a more efficient algorithm.
"""


def merge_do_duplicates(seq1, seq2, previous_val = None):
    result = ()

    if len(seq1) == 0 and len(seq2) == 0:
        return result

    if len(seq1) == 0:
        if seq2[0] != previous_val:
            result += (seq2[0],)
        return result + merge_do_duplicates(seq1, seq2[1:], seq2[0])
    elif len(seq2) == 0:
        if seq1[0] != previous_val:
            result += (seq1[0],)
        return result + merge_do_duplicates(seq1[1:], seq2, seq1[0])


    elif seq1[0] <= seq2[0]:
        if seq1[0] != previous_val:
            result += (seq1[0],)
        return result + merge_do_duplicates(seq1[1:], seq2, seq1[0])
    elif seq1[0] > seq2[0]:
        if seq2[0] != previous_val:
            result += (seq2[0],)
        return result + merge_do_duplicates(seq1, seq2[1:], seq2[0])


assert merge_do_duplicates((), ()) == ()
assert merge_do_duplicates((), (3, 7, 11)) == (3, 7, 11)
assert merge_do_duplicates((3, 7, 11), ()) == (3, 7, 11)
assert merge_do_duplicates((14,), (3, 7, 11)) == (3, 7, 11, 14)
assert merge_do_duplicates((3, 7, 11), (2, 18)) == (2, 3, 7, 11, 18)
assert merge_do_duplicates((3, 3, 11), (4, 12, 12)) == (3, 4, 11, 12)
assert merge_do_duplicates((3, 3), (3, 3, 8)) == (3, 8)
assert merge_do_duplicates("ace", "bd") == ("a", "b", "c", "d", "e")
