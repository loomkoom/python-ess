# implement using recursion


def depth(l):
    """ Returns the depth of a list of lists, where the the last list is an empty list"""
    diepte = 0

    if len(l) == 0:
        return diepte

    else:
        diepte += 1

    return depth(l[0]) + diepte


assert depth([]) == 0
assert depth([[]]) == 1
assert depth([[[[[[[[]]]]]]]]) == 7
