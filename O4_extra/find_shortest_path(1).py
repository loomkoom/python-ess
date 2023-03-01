def find_shortest_path(matrix, start, destination, excluded_cities = set()):
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

    if start == destination:
        return (0, [])

    shortest_distance = None
    path_so_far = None

    excluded_cities.add(start)  # voor dat je de for lus in gaat !
    for neighbour in range(len(matrix) - 1):
        distance = matrix[start][neighbour]
        if distance != 0 and neighbour not in excluded_cities:  # verbonden en nog niet bezocht
            rec_sol = find_shortest_path(matrix, neighbour, destination, excluded_cities)
            if rec_sol[1] is not None:  # als er een pad(destinatie) gevonden is => geldig antwoord
                total_distance = distance + rec_sol[0]
                if shortest_distance is None or total_distance < shortest_distance:  # neem het beste antwoord en bepaal die route
                    shortest_distance = total_distance
                    path_so_far = [neighbour] + rec_sol[1]
    excluded_cities.remove(start)  # na de for loop, zodat het de andere takken niet beïnvloed

    return shortest_distance, path_so_far  # geef de kortse lengte samen met route mee


distance_matrix = [[0, 15, 0, 0, 8, 0, 0, 0], \
                   [15, 0, 10, 20, 0, 0, 0, 0], \
                   [0, 10, 0, 8, 6, 6, 0, 0], \
                   [0, 20, 8, 0, 0, 10, 0, 0], \
                   [8, 0, 6, 0, 0, 15, 0, 0], \
                   [0, 0, 6, 10, 15, 0, 0, 12], \
                   [0, 0, 0, 0, 0, 0, 0, 12], \
                   [0, 0, 0, 0, 0, 0, 12, 0]]
# matrix moet 8x8 zijn ipv 8x7
assert find_shortest_path(distance_matrix, 3, 5) == ((10, [5]))
# assert find_shortest_path(distance_matrix, 5, 4) == ((12, [2, 4]))
assert find_shortest_path(distance_matrix, 0, 3) == ((22, [4, 2, 3]))
# assert find_shortest_path(distance_matrix, 0, 6) == (None, None)

print('fct', end = '\n\n\n')


# variation on the exercise above:
def find_all_paths(matrix, start, destination, excluded_cities = set(), paths = set()):
    # Determine all possible paths from a start city to a destination city, based
    # on a given distance matrix.
    # The function should return a set containing a collection of tuples. Each tuple showing a possible path
    # from start city to destination city (excluding the start city).
    # An empty set is returned if no path exists between start and destination

    if start == destination:
        return set([()])

    result = set()

    excluded_cities.add(start)
    for neighbour in range(len(matrix)):
        distance = matrix[start][neighbour]
        if distance != 0 and neighbour not in excluded_cities:  # verbonden en nog niet bezocht
            print('n',neighbour)
            rec_sol = find_all_paths(matrix, neighbour, destination, excluded_cities)
            if len(rec_sol) != 0:
                for path in rec_sol:
                    result.add((neighbour,)+path)

    excluded_cities.remove(start)  # na de for loop, zodat het de andere takken niet beïnvloedt
    print('exit', end = '\n\n')
    print(result)
    return result  # geef de kortse lengte samen met route mee


# print(find_all_paths(distance_matrix,0,3))
print(find_all_paths(distance_matrix, 3, 5))
# print(find_all_paths(distance_matrix, 0, 6))
# assert find_all_paths(distance_matrix,0,3)=={(1, 2, 4, 5, 3), (1, 3), (1, 2, 5, 3), (4, 2, 1, 3), (4, 5, 3), (4, 5, 2, 3), (1, 2, 3), (4, 5, 2, 1, 3), (4, 2, 5, 3), (4, 2, 3)}
# assert find_all_paths(distance_matrix,3,5)=={(1, 0, 4, 2, 5), (5,), (1, 0, 4, 5), (2, 4, 5), (2, 5), (2, 1, 0, 4, 5), (1, 2, 5), (1, 2, 4, 5)}
# assert find_all_paths(distance_matrix,0,6)==set()
