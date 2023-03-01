def length(vector):

    """
        Return the length of the given sparse vector.
    """

    return max(dict.keys(vector)) + 1          # dict.keys geeft alle sleutels => neem hiervan de grootste + 1( beginnend van 0 )


def vector_sum(left,right):

    """
        Compute the sum of two sparse vectors.
        The resulting vector is also a sparse vector, whose
        elements are the sum of the elements at corresponding
        positions in the given vectors.
    """


    length_largest_vector = max(length(left), length(right))
    result = {length_largest_vector - 1:0.0}                # laatste element is 0

    for index in range(0, length_largest_vector):

        value = dict.get(left,index,0.0) +  dict.get(right,index,0.0)

        if value != 0.0:
            result[index] = value

    return result

# zeer traag algoritme omdat die ook alle nullen berekenen
# ==> zoek efficienter algortime




vector1 = { 4:2.3, 10:7.8, 23:9.9, 150:0.0 }
vector2 = { 1:4.2, 10:3.0, 112:10.0, 150:0.0 }
assert vector_sum(vector1,vector2) ==    { 1:4.2, 4:2.3, 10:10.8, 23:9.9, 112:10.0, 150:0.0 }

vector1 = { 4:2.3, 10:0.0 }
vector2 = { 1:4.2, 20:10.0, 30:0.0 }
assert vector_sum(vector1,vector2) ==    { 1:4.2, 4:2.3, 20:10.0, 30:0.0 }

vector1 = { 4:2.3, 10:7.8, 23:9.9, 150:0.0 }
vector2 = { 4:-2.3, 20:56.8, 160:0.0}
assert vector_sum(vector1,vector2) ==    { 10:7.8, 20:56.8, 23:9.9, 160:0.0 }

vector1 = { 4:2.3, 10:7.8, 23:9.9, 150:10.0, 160:0.0 }
vector2 = { 4:-2.3, 10:-7.8, 23:-9.9, 150:-10.0, 160:0.0 }
assert vector_sum(vector1,vector2) == { 160:0.0 }

vector1 = { 0:0.0 }
vector2 = { 0:0.0 }
assert vector_sum(vector1,vector2) == { 0:0.0 }
