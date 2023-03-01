def overwrite(list,value):

    """
      A function that given a list, overwrites all elements of the list with the given value.
      Nothing is returned: the given list is modified.
    """

    for index in range(len(list)):
        list[index] = value


## TESTS
lst = [1, 2, 3]
overwrite(lst, "a")
assert lst == ["a", "a", "a"]

lst = []
overwrite(lst, 7)
assert lst == []

lst = ["a", 7, 0.5, 24]
overwrite(lst, 42)
assert lst == [42, 42, 42, 42]

