# Positions are used to
#  (1) identify cells on the board
#  (2) dots on blocks relative to the block's anchor.


def is_proper_position(position):
    """
        Check whether the given position is a proper position.
        - True if and only if the given position is a tuple of length 2
          whose elements are both integer numbers.
        ASSUMPTIONS
        - None
    """

    if isinstance(position, tuple) and len(position) == 2:
        for elem in position:
            if not isinstance(elem, int):
                return False
        return True
    return False


def is_proper_position_for_board(dimension, position):
    """
        Check whether the given position is a proper position for a square
        board with the given dimension.
        - True if and only if (1) the given dimension is a positive integer
          number and (2) if the given position is a proper position within
          the boundaries of a board with the given dimension, i.e not below
          1 nor above the given dimension in both directions.
        ASSUMPTIONS
        - None
    """

    if is_proper_position(position):
        if isinstance(dimension, int) and dimension > 0:
            for elem in position:
                if not 1 <= elem <= dimension:
                    return False
            return True
    return False


def row(pos):
    """
      Return the row of the given position.
    """

    return pos[1]


def col(pos):
    """
      Return the column of the given position.
    """

    return pos[0]


def left(dimension, position):
    """
        Return the position on any board with the given dimension immediately to
        the left of the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
    """

    if col(position) != 1:
        return (col(position) - 1, row(position))
    return None


def right(dimension, position):
    """
       Return the position on any board with the given dimension immediately to
       the right of the given position.
       - None is returned if the generated position is outside the boundaries of
         a board with the given dimension.
       ASSUMPTIONS
       - The given position is a proper position for any board with the
         given dimension.
     """

    if col(position) != dimension:
        return (col(position) + 1, row(position))
    return None


def up(dimension, position):
    """
        Return the position on any board with the given dimension immediately
        above the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
     """

    if row(position) != dimension:
        return (col(position), row(position) + 1)
    return None


def down(dimension, position):
    """
        Return the position on any board with the given dimension immediately
        below the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
     """

    if row(position) != 1:
        return (col(position), row(position) - 1)
    return None


def next(dimension, position):
    """
        Return the position on any board with the given dimension next to the
        given position.
        - If the given position is not at the end of a row, the resulting position
          is immediately to the right of the given position.
        - If the given position is at the end of a row, the resulting position is
          the leftmost position of the row above. If that next row does not exist,
          None is returned.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
     """

    if col(position) < dimension:
        return right(dimension, position)
    elif row(position) == dimension:
        return None
    return (1, row(position) + 1)


def translate_over(position, delta_x, delta_y):
    """
        Return the position resulting from translating the given position horizontally
        and vertically over the given delta's.
        ASSUMPTIONS
        - The given position is a proper position.
        - The given delta's are integer numbers.
    """

    return (col(position) + delta_x, row(position) + delta_y)


def get_adjacent_positions(position, dimension = None):
    """
        Return a mutable set of all positions immediately adjacent to the
        given position and within the boundaries of a board with the given
        dimension.
        - Adjacent positions are either at a horizontal distance or at a vertical
          distance of 1 from the given position.
        - If the given dimension is None, no boundaries apply.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension, or simply a proper position if no dimension is supplied.
    """
    adjacent_positions = set()

    adjacent_positions.add((col(position) + 1, row(position)))
    adjacent_positions.add((col(position), row(position) + 1))
    adjacent_positions.add((col(position), row(position) - 1))
    adjacent_positions.add((col(position) - 1, row(position)))

    copy_adjacent_positions = set.copy(adjacent_positions)

    if dimension is None:
        return adjacent_positions

    for pos in copy_adjacent_positions:
        if not is_proper_position_for_board(dimension, pos):
            adjacent_positions.remove(pos)
    return adjacent_positions


def is_adjacent_to(position, other_positions):
    """
        Check whether the given position is adjacent to at leas t one of the positions
        in the collection of other positions.
        - True if and only if at least one of the other positions is one of the positions
          adjacent to the given position in an unbounded area.
        ASSUMPTIONS
        - The given position is a proper position
        - All positions in the collection of other positions are proper positions.
    """
    adjacent = frozenset(get_adjacent_positions(position))
    other = frozenset(other_positions)

    if not adjacent.isdisjoint(other):
        return True
    return False


def get_surrounding_positions(position, dimension = None):
    """
        Return a mutable set of all positions immediately surrounding the
        given position and within the boundaries of a board with the given
        dimension.
        - Surrounding positions are at a horizontal distance and/or a vertical
          distance of 1 from the given position.
        - If the given dimension is None, no boundaries apply.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension, or simply a proper position if no dimension is supplied.
    """

    adjacent_positions = set()

    adjacent_positions.update(get_adjacent_positions(position, dimension))
    adjacent_positions.add((col(position) + 1, row(position) - 1))
    adjacent_positions.add((col(position) + 1, row(position) + 1))
    adjacent_positions.add((col(position) - 1, row(position) - 1))
    adjacent_positions.add((col(position) - 1, row(position) + 1))

    copy_adjacent = set.copy(adjacent_positions)

    if dimension is None:
        return adjacent_positions
    for pos in copy_adjacent:
        if not is_proper_position_for_board(dimension, pos):
            adjacent_positions.remove(pos)

    return adjacent_positions


def are_chained(positions):
    """
        Check whether the given collection of positions make up a chain.
        - True if and only if each position in the given collection of positions
          can be reached from each other position in that collection.
          can be reached from each other position in that collection.
          A position P1 can be reached from another position P2 if
            (1) P1 and P2 are adjacent to each other, or
            (2) there exists at least one position P3 in the given collection
                of positions that can be reached from both P1 and P2.
       ASSUMPTIONS
       - Each position in the collection of positions is a proper position.
       NOTE
       - This version of the function must be worked out in an iterative way.
         The body may use while statements and/or for statements.
    """

    if len(positions) <= 1:
        return True
    positions = list(positions)
    positions_copy = sorted(list(set(positions)))
    chained = set()
    chained.add(positions_copy[0])
    counter = 0
    CHANGED = True

    while counter < len(positions):
        last_positions_list = set(positions_copy)
        for pos in positions_copy:
            if is_adjacent_to(pos, chained):
                chained.add(pos)
                positions_copy.remove(pos)
        if last_positions_list == set(positions_copy):
            CHANGED = False
        if len(positions_copy) == 0 or not CHANGED:
            break
        counter += 1

    if set(chained) == set(positions):
        return True
    return False


def are_chained_rec(positions, chained_positions = frozenset(), non_chainable_positions = frozenset()):
    """
        Check whether the given collection of positions make up a chain.
        - True if and only if each position in the given collection of positions
          can be reached from each other position in that collection.
          A position P1 can be reached from another position P2 if
            (1) P1 and P2 are adjacent to each other, or
            (2) there exists at least one position P3 in the given collection
                of positions that can be reached from both P1 and P2.
       ASSUMPTIONS
       - Each position in the collection of positions is a proper position.
       NOTE
       - This version of the function must be worked out in a recursive way. The body
         may not use while statements nor for statements.
       TIP
       - Extend the heading of the function with two additional parameters:
          - chained_positions: a frozen set of positions that already form a chain.
          - non_chainable_positions: a frozen set of positions that are not
            adjacent to any of the positions in the set of chained positions.
         Assign both extra parameters the empty frozen set as their default value.
    """

    positions = sorted(list(set(positions)))
    if non_chainable_positions == frozenset():
        non_chainable_positions = set()
    if chained_positions == frozenset() and len(positions) > 0:
        chained_positions = set((positions[0],))

    if set(positions) == chained_positions:
        return True

    if len(positions) == 0:
        if len(non_chainable_positions) == 0:
            return True
        return False

    if is_adjacent_to(positions[0], chained_positions) and is_adjacent_to(positions[0], non_chainable_positions):
        adjacent_pos = get_adjacent_positions(positions[0])
        connected_chain = list(set.intersection(adjacent_pos, non_chainable_positions))

        chained_positions.add(positions[0])
        chained_positions.update(connected_chain)
        non_chainable_positions.difference_update(connected_chain)
        return are_chained_rec(connected_chain + positions[1:], chained_positions, non_chainable_positions)

    elif is_adjacent_to(positions[0], chained_positions):
        chained_positions.add(positions[0])
        return are_chained_rec(positions[1:], chained_positions, non_chainable_positions)

    elif not is_adjacent_to(positions[0], chained_positions):
        non_chainable_positions.add(positions[0])
        return are_chained_rec(positions[1:], chained_positions, non_chainable_positions)
