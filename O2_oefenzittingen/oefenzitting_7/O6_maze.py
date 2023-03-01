"""
A module that deals with mazes
"""


def print_maze_path(maze, path, number = 8):
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


def find_path(maze, current = (0, 0), target = (7, 7)):
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
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    if current == target:
        return [target]
    else:
        maze[current[0]][current[1]] = 1
        path = []
        for direction in directions:
            new_loc = vector_add(direction,current)

            if 0 <= new_loc[0] < len(maze) and 0 <= new_loc[1] < len(maze) and (
                    maze[new_loc[0]][new_loc[1]] == 0):
                next_path = find_path(maze,new_loc,target)

                if len(next_path) > 0:
                    path = next_path
        maze[current[0]][current[1]] = 0

        if len(path) != 0:
            return [current] + path
        else:
            return []


    return []


if __name__ == "__main__":
    maze = [[0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0]]

    path = find_path(maze)
    print(path)
    print_maze_path(maze, path)
