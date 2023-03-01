def find_shortest_path(matrix, start, destination, excluded_cities=set()):
    # Determine the shortest path from a start city to a destination city, based
    # on a given distance matrix. Each city is indexed by an integer, starting from 0
    # up to the dimension of the distance matrix - 1. The element in row i and column j of
    # the matrix contains the distance between city i and city j. A distance of 0 is used when no path exists
    # between two cities.
    # The function should return a tuple with two elements.
    # The first element shows the minimum distance between start and destination.
    # The second element is a list of cities, in the right order, which functions as a shortest path route description
    # to be followed from start to destination (excluding the start city).
    # None is returned if no path exists between start and destination



distance_matrix = [[0,15,0,0,8,0,0,0],\
            [15,0,10,20,0,0,0,0],\
            [0,10,0,8,6,6,0,0],\
            [0,20,8,0,0,10,0,0],\
            [8,0,6,0,0,15,0,0],\
            [0,0,6,10,15,0,0,12],\
            [0,0,0,0,0,0,12,0]]

assert find_shortest_path(distance_matrix,3,5) == ((10,[5]))
assert find_shortest_path(distance_matrix,5,4) == ((12,[2,4]))
assert find_shortest_path(distance_matrix,0,3) == ((22,[4,2,3]))
assert find_shortest_path(distance_matrix,0,6) == (None,None)


#variation on the exercise above:
def find_all_paths(matrix, start, destination, excluded_cities=set()):
    # Determine all possible paths from a start city to a destination city, based
    # on a given distance matrix.
    # The function should return a set containing a collection of tuples. Each tuple showing a possible path
    # from start city to destination city (excluding the start city).
    # An empty set is returned if no path exists between start and destination


assert find_all_paths(distance_matrix,0,3)=={(1, 2, 4, 5, 3), (1, 3), (1, 2, 5, 3), (4, 2, 1, 3), (4, 5, 3), (4, 5, 2, 3), (1, 2, 3), (4, 5, 2, 1, 3), (4, 2, 5, 3), (4, 2, 3)}
assert find_all_paths(distance_matrix,3,5)=={(1, 0, 4, 2, 5), (5,), (1, 0, 4, 5), (2, 4, 5), (2, 5), (2, 1, 0, 4, 5), (1, 2, 5), (1, 2, 4, 5)}
assert find_all_paths(distance_matrix,0,6)==set()