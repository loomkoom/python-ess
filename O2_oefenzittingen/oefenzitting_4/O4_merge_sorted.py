def merge(seq_1, seq_2):

    """
      Merge the given sorted sequences (ascending order) into a new tuple.
      The resulting tuple contains all the elements of both given sequences in
      ascending order. It does not contain any duplicates, although both given
      sequences may store the same element several times.

      You may NOT use the sort function for this exercise.
      Use the fact that the 2 provided lists are already sorted to come up
      with a more efficient algorithm.

      Some example outputs:

      (),()                 |   ()
      (),(3,7,11)           |   (3,7,11)
      (3,7,11),()           |   (3,7,11)
      (14,),(3,7,11)        |   (3,7,11,14)
      (3,7,11),(2,18)       |   (2,3,7,11,18)
      (3,3,11),(4,12,12)    |   (3,4,11,12)
      (3,3),(3,3,8)         |   (3,8)
      "ace","bd"            |   ("a","b","c","d","e")

    """

    result = []
    index_1, index_2,index = 0, 0, 0

    if seq_1 == ():
        return seq_2
    elif seq_2 == ():
        return seq_1

    while (len(result) < len(seq_1) + len(seq_2)):
        if seq_1[index_1] < seq_2[index_2] and seq_1:
            result.append(seq_1[index_1])
            index_1 += 1
        else:
            result.append(seq_2[index_2])
            index_2 += 1
        if index_1 == len(seq_1) or index_2 == len(seq_2):
            result.extend(seq_1[index_1:] or seq_2[index_2:])

    while index in range(0,len(result)):
        if result[index-1] == result[index]:

            del result[index]
            index = index - 1

        index += 1

    merged_tuple = tuple(result)

    return merged_tuple


## TESTS
# empty sequences
assert merge((),()) == ()
# first sequence empty
assert merge((),(3,7,11)) == (3,7,11)
# second sequence empty
assert merge((3,7,11),()) == (3,7,11)
# first sequence with largest element
assert merge((14,),(3,7,11)) == (3,7,11,14)
# second sequence with largest element
assert merge((3,7,11),(2,18)) == (2,3,7,11,18)
# sequences with duplicates
assert merge((3,3,11),(4,12,12)) == (3,4,11,12)
# sequences with common elements
assert merge((3,3),(3,3,8)) == (3,8)
# sequences with None-elements
# given sequences are strings
assert merge("ace","bd") == ("a","b","c","d","e")

