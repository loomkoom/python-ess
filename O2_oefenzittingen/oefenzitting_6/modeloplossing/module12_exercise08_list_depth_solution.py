# implement using recursion


def depth(l):
    """ Returns the depth of a list of lists, where the the last list is an empty list"""
    if len(l) == 0:
        return 0
    else:
        return 1 + depth(l[0])


assert depth([]) == 0
assert depth([[]]) == 1
assert depth([[[[[[[[]]]]]]]]) == 7
