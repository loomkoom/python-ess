"""
Write a function that returns the product of two sparse vectors.

The product of two vectors is the sum of the product of corresponding elements
in both vectors.  Complement the definition of your function with a description
of loop invariants.
"""


def length(vector):
    """ Return the length of the given sparse vector.  The returned value is
    equal to the highest index at which a non-zero element is stored +1.
    """
    if len(vector) == 0:
        return 0
    else:
        return max(vector.keys()) + 1


assert length({1: 3, 6: 12, 100: -67.9}) == 101
assert length({}) == 0


def vector_product(left, right):
    """ Compute the product of two given sparse vectors.
    The resulting value is the sum of the products of corresponding
    elements in both given vectors.
    """
    # neem eerst de lanngste

    result = 0

    for key in left:
        if key in right:
            result += left[key] * right[key]

    return result


vector1 = {4: 2, 10: 7, 23: 9}
vector2 = {1: 4, 10: 3, 112: 10}
assert vector_product(vector1, vector2) == 21

vector3 = {4: -2, 10: 1, 20: 6}
assert vector_product(vector1, vector3) == 3

vector4 = {5: 6, 12: -7}
assert vector_product(vector1, vector4) == 0

assert vector_product(vector1, {}) == 0
