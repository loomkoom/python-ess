def binary_search(s, seq):
    """
      Recursively check wether an item is present in a sorted seqence. Use the fact that
      the input sequence is sorted in ascending order. This allows you to implement an
      algoritm that is, on average, faster than linearly searching the list.

      Hint: when searching for x, if the middle element of the sorted list is greater then x,
            then x can only occur it the smaller half of the list
    """

    mid = len(seq) // 2

    if len(seq) == 0:
        return False

    if seq[mid] == s:
        return True

    elif seq[mid] < s:
        return binary_search(s, seq[mid + 1:])
    else:
        return binary_search(s, seq[:mid])


assert binary_search("a", "abcdef")
assert not binary_search("z", "abcdef")
assert binary_search(2, [1, 2, 5, 6, 8, 9])
assert binary_search("jkl", ["abc", "def", "ghi", "jkl", "mno", "pqr"])
assert not binary_search(100, range(0, 100))
assert binary_search(99, range(0, 100))
