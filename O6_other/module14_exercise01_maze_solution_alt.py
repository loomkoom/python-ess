def print_maze_path(maze, path, number=9):
    """
    A function that prints a maze and represents the given
    path by the given number.
    """
    for i in range(len(path)):
        maze[path[i][0]][path[i][1]] = number
    for row in maze:
        print(row)


def vector_add(t1, t2):
    """
    A function that implements vector addition
    """
    return t1[0] + t2[0], t1[1] + t2[1]


def in_maze(maze, position):
    x = position[0]
    y = position[1]
    return x >= 0 and y >= 0 and x < len(maze) and y < len(maze[0])


def is_free(maze, position):
    x = position[0]
    y = position[1]
    return maze[x][y] == 0


def find_path_backtrack(maze, current, target, path):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    if current == target:
        return path

    for direction in directions:
        position = vector_add(current, direction)
        if in_maze(maze, position) and is_free(maze, position) and (position not in path):
            the_path = find_path_backtrack(maze, position, target, path + (position,))
            if the_path is not None:
                return the_path

    return None


# This solution will keep the current path and pass it along the recursive calls to avoid loops in the result.
def find_path(maze, current=(0, 0), target=(7, 7)):
    """
    This function returns any path through an 8x8 maze as
    a list of tuple positions starting at (0,0) and
    ending at (7,7).

    The function accepts an 8x8 array of numbers 0 or 1
    representing a maze with walls, where 0 indicates a
    free position, and 1 indicates a wall. The start and end
    positions should be free.

    The function will only use horizontal or vertical moves.
    A move into a wall is also illegal.

    The algorithm avoids retracing previously tried paths.
    """
    return find_path_backtrack(maze, current, target, (current,))


if __name__ == "__main__":
    maze = [[0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 0]]

    path = find_path(maze)
    print(path)
    if path is not None:
        print_maze_path(maze, path)
