def is_sorted(sequence):

    """
      A function that verifies whether a sequence is sorted in increasing order.

      Some example outputs for given sequences:
      ()                     True
      (5,)                   True
      (3, 7, 11)             True
      (3, 7, 5, 11)          False
      (3, 7, 7, 11)          True
      ("aaabc", "aab", "b")  True
      ("aabc", "aab", "b")   False
    """


    for index in range(1,len(sequence)):
        if sequence[index-1] > sequence[index]:
            return False
    return True

## TESTS

# empty sequence
assert is_sorted(())

# 1 element sequence
assert is_sorted((5,))

# sorted sequence with several elements
assert is_sorted((3, 7, 11))

# unsorted sequence with several elements
assert not is_sorted((3, 7, 5, 11))

# sorted sequence with duplicates
assert is_sorted((3, 7, 7, 11))

# sorted sequence with strings
assert is_sorted(("aaabc", "aab", "b"))

# unsorted sequence with strings
assert not is_sorted(("aabc", "aab", "b"))

