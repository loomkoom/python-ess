""" 
  Merge the given sorted sequences (in ascending order) into a new tuple using
  RECURSION. The resulting tuple contains all the elements (including 
  duplicates) of both given sequences in ascending order. If an element appears 
  n times in seq1 and m times in seq2, it appears n+m times in the new tuple.
  You may NOT use the sort function for this exercise. Use the fact that the 2 
  provided lists are already sorted to come up with a more efficient algorithm.
"""


def merge(seq1, seq2):
    result = ()

    if len(seq1) == 0:
        result = tuple(seq2)
        return result
    elif len(seq2) == 0:
        result = tuple(seq1)
        return result

    elif seq1[0] < seq2[0]:
        result += (seq1[0],)
        return result + merge(seq1[1:], seq2)
    else:
        result += (seq2[0],)
        return result + merge(seq1, seq2[1:])


assert merge((), ()) == ()
assert merge((), (3, 7, 11)) == (3, 7, 11)
assert merge((3, 7, 11), ()) == (3, 7, 11)
assert merge((14,), (3, 7, 11)) == (3, 7, 11, 14)
assert merge((3, 7, 11), (2, 18)) == (2, 3, 7, 11, 18)
assert merge((3, 3, 11), (4, 12, 12)) == (3, 3, 4, 11, 12, 12)
assert merge((3, 3), (3, 3, 8)) == (3, 3, 3, 3, 8)
assert merge("ace", "bd") == ("a", "b", "c", "d", "e")
