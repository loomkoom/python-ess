"""
Write a function that returns the flattened form of a given set of tuples.  The
flattened form of a set of tuples is the set of all elements that are part of at
least one of the tuples of the given set.

As an example, the flattened form of the set {(1, 2), (3,) , (5, 6)} is
{1, 2, 3, 5, 6}.  As another example, the flattened form of the set
{(1, 2), ((3, 4), 5)} is {1, 2, (3, 4), 5}. The last example shows that the
flattening does not proceed to deeper levels. Complement the definition of your
function with a description of the loop invariant.
"""


def flatten(sett):
    """ Return the flattened form of a set of tuples.
    The flattened form of a set of tuples is the set of all elements
    that are part of at least one of the tuples of the given set. """

    flattened = set()

    for tup in sett:  # itereren over de lijst ipv over de index
        for element in tup:
            flattened.add(element)
    return flattened


assert flatten({(1, 2), (3, 4, 2), (1, 6, 5)}) == {1, 2, 3, 4, 5, 6}
assert flatten(set()) == set()
assert flatten({((2, 3), 5), ("abc", "def"), ((2, 3), "abc")}) == \
       {(2, 3), 5, "abc", "def"}
