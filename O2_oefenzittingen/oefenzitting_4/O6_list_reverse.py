def reverse(lst):
    """
      A function that given a list, reverses this list. Nothing is returned and
      the given list is modified.

      For this exercise you are not allowed to use python's builtin function for reversing lists.
    """

    for index in range(len(lst)//2):
        lst[index],lst[len(lst)-index-1] = lst[len(lst)-index-1],lst[index]

## TESTS
lst = [1, 2, 3, 4]
reverse(lst)
assert lst == [4, 3, 2, 1]

lst = ["a", "b", "c", "d", "e"]
reverse(lst)
assert lst == ["e", "d", "c", "b", "a"]

lst = []
reverse(lst)
assert lst == []

lst = [1]
reverse(lst)
assert lst == [1]

lst = [1,2]
reverse(lst)
assert lst == [2, 1]

lst = [1, 2, 3]
reverse(lst)
assert lst == [3, 2, 1]

lst = [1, 20.5, "x", [1,2,3], -100, (7,8)]
reverse(lst)
assert lst == [(7,8), -100, [1,2,3], "x", 20.5, 1]
