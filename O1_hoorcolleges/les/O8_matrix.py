def is_matrix(thing):

    """
      Check whether the given matrix satisfies all conditions imposed on
      matrices.
    """
    if not isinstance(thing,(list,tuple)):
        return False
    nb_rows = len(thing)
    if (nb_rows == 0):
        return False

    nb_cols = None
    for row in range(nb_rows):
        if not isinstance(thing[row],(list,tuple,str,range)):
            return False
        if nb_cols == None:
            nb_cols = len(thing[row])
        elif nb_cols != len(thing[row]):
            return False
    if nb_cols == 0:
        return False
    return True

assert is_matrix([[1]])
assert is_matrix(("abc","123","xyz"))
assert not is_matrix([])
assert not is_matrix([1,2,3])
assert not is_matrix(((1,2,3),("a","b"),(4,5,6)))


def multiply(matrix,vector):
    """
      Return a vector that is the product of the given matrix with the given vector.
    """
    result = []

    # for row in range(len(vector)):
    for row in range(0,len(matrix)):
        value = 0

       # for index in range(len(matrix)):
        for index in range(0,len(matrix[0])):

            value += matrix[row][index] * vector[index]

        result.append(value)

    return result

def multiply(matrix,vector):
    """
      Return a vector that is the product of the given matrix with the given vector.
    """
    result = [None for k in range(0,len(matrix))]

    # for row in range(len(vector)):
    for row in range(0,len(matrix)):
        value = 0

       # for index in range(len(matrix)):
        for index in range(0,len(matrix[0])):

            value += matrix[row][index] * vector[index]

        result[row] = value

    return result


assert multiply([[1,1,1],[2,2,2],[3,3,3]],[10,20,30]) ==    [60,120,180]
assert multiply([[1,1,1],[2,2,2]],[3,3,3]) ==    [9,18]                       # werkt niet voor rechthoekige matrices !!
assert multiply([[12]],[3]) ==    [36]                       # werkt niet voor rechthoekige matrices !!