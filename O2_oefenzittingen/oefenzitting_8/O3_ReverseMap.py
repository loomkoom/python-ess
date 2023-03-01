def reverse_map(function, nested_list):
    """ Recursively reverse the elements of the given nested list,
        applying the given function to each single element """

    if isinstance(nested_list, list):
        return list(reversed(list(map(lambda x: reverse_map(function, x), nested_list))))
    return function(nested_list)


identity_function = lambda x: x
assert reverse_map(identity_function, [1, 2, 3]) == [3, 2, 1]
assert reverse_map(identity_function, [[54, [1, 2, 3]], [9, [4, 5]], 2, 1]) == [1, 2, [[5, 4], 9], [[3, 2, 1], 54]]
assert reverse_map(lambda x: x ** 2, ([1, [2, [3, [4, [5], [6, 7, 8]]]]])) == [[[[[64, 49, 36], [25], 16], 9], 4], 1]
