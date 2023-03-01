import Block
import Position


def make_board(dimension=10, positions_to_fill=frozenset()):
    """
        Return a new board of the given dimension for which all cells at the
        given positions are already filled.
        ASSUMPTIONS
        - The given dimension is a positive integer number.
        - The filled positions is a collection of proper positions. Positions
          outside the boundaries of the new board have no impact on the content
          of the new board.
    """

    board = {}

    dim_pos = (dimension, dimension)
    board[dim_pos] = 'Free'

    for pos in positions_to_fill:
        if Position.is_proper_position_for_board(dimension, pos):
            board[pos] = 'Filled'
    return board


def copy_board(board):
    """
        Return a copy of the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """

    return board.copy()


def is_proper_board(board):
    """
        Check wether the given board is a proper board.
        - ...
        ASSUMPTIONS
        - None
        NOTE
        - You need to complete the conditions
        (as they depend on the internal representation you have chosen for the board)
    """
    if not isinstance(board, dict):
        return False

    for pos in board:
        if Position.is_proper_position(pos):
            if board[pos] == 'Filled' or board[pos] == 'Free':
                return True
        return False


def dimension(board):
    """
        Return the dimension of the given board.
        - The function returns the number of rows (== number of columns) of
          the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """

    dimension = max(board)[0]

    return dimension


def get_all_filled_positions(board):
    """
        Return a set of all the positions of filled cells on the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    filled_positions = set()

    for position in board:
        if board[position] == 'Filled':
            filled_positions.add(position)

    return filled_positions


def is_filled_at(board, position):
    """
        Return a boolean indicating whether or not the cell at the given position
        on the given board is filled.
        - Returns false if the given position is outside the boundaries of the
          given board.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given position is a proper position.
    """
    if not Position.is_proper_position_for_board(dimension(board), position):
        return False
    if position not in board:
        return False

    if board[position] == 'Filled':
        return True
    return False


def is_filled_row(board, row):
    """
        Return a boolean indicating whether or not all the cells of the given
        row on the given board are filled.
        - Returns false if the given row is not an integer number or if it is
          outside the boundaries of the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        NOTE
        - You are not allowed to use for statements in the body of this function.
    """

    position = (1, row)

    if not isinstance(row, int):
        return False
    if row > dimension(board) or row <= 0:
        return False

    # while position[0] <= dimension(board):
    #     if board[tuple(position)] != 'Filled':
    #         return False
    #     position[0] += 1

    while position[0] <= dimension(board):
        if not is_filled_at(board, position):
            return False
        position = (position[0] + 1, row)
    return True


def is_filled_column(board, column):
    """
        Return a boolean indicating whether or not all the cells of the given
        column on the given board are filled.
        - Returns false if the given column is not an integer number or if it is
          outside the boundaries of the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        NOTE
        - You are not allowed to use while statements in the body of this function.
    """

    if not isinstance(column, int):
        return False
    if column > dimension(board) or column <= 0:
        return False

    position = [column, 1]

    for position[1] in range(1, dimension(board) + 1):
        if not is_filled_at(board, tuple(position)):
            return False
    return True


def get_all_filled_rows(board):
    """
        Return all the rows on the given board that are completely filled.
        - The function returns a list of the numbers in ascending order of
          all the rows that are completely filled.
        ASSUMPTIONS
        - The given board is a proper board.
        NOTE
        - You are not allowed to use for statements in the body of this function.
    """
    row = 1
    filled_rows = list()

    while row <= dimension(board):
        if is_filled_row(board, row):
            filled_rows.append(row)
        row += 1
    return filled_rows


def get_all_filled_columns(board):
    """
        Return all the columns on the given board that are completely filled.
        - The function returns a tuple of the numbers in descending order of
          all the columns that are completely filled.
        ASSUMPTIONS
        - The given board is a proper board.
        NOTE
        - You are not allowed to use while statements in the body of this function.
    """
    filled_columns = []

    for position in board:
        if is_filled_column(board, position[1]) and position[1] not in filled_columns:
            filled_columns.append(position[1])
    filled_columns = reversed(sorted(filled_columns))

    return tuple(filled_columns)


def fill_cell(board, position):
    """
        Fill the cell at the given position on the given board.
        - Nothing happens if the given position is outside the
          boundaries of the given board or if the given cell is
          already filled.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given position is a proper position.
    """

    if Position.is_proper_position_for_board(dimension(board), position):
        board[position] = 'Filled'


def fill_all_cells(board, positions):
    """
        Fill all the cells at each position in the given collection of
        positions on the given board.
        - Positions outside the boundaries of the given board are ignored.
        - Positions that are already filled are left untouched.
        ASSUMPTIONS
        - The given board is a proper board.
        - Each position in the collection of positions is a proper position.
    """

    for position in positions:
        if Position.is_proper_position_for_board(dimension(board), position):
            board[position] = 'Filled'


def free_cell(board, position):
    """
        Free the cell at the given position of the given board.
        - Nothing happens if the cell is already free or if the given
          position is outside the boundaries of the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given position is a proper position.
    """

    if position in board.copy():
        board.pop(position)


def free_all_cells(board, positions):
    """
        Free all the cells at each position in the tuple of positions on
        the given board.
        - Positions outside the boundaries of the given board are ignored.
        - Positions that are already free are left untouched.
        ASSUMPTIONS
        - The given board is a proper board.
        - Each position in the tuple of positions is a proper position.
        NOTE
        - This function must be worked out in a recursive way.
    """
    if len(positions) == 0:
        return

    if Position.is_proper_position_for_board(dimension(board), positions[0]) and positions[0] in board:
        board.pop(positions[0])
    return free_all_cells(board, positions[1:])


def free_row(board, row):
    """
        Free all the cells of the given row on the given board.
        - Nothing happens if the given row is not an integer number or if
          it is outside the boundaries of the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """

    if not isinstance(row, int):
        return
    if row > dimension(board) or row <= 0:
        return

    for position in board.copy():
        if position[1] == row:
            board.pop(position)


def free_column(board, column):
    """
        Free all the cells of the given column on the given board.
        - Nothing happens if the given column is not an integer number or if
          it is outside the boundaries of the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    if not isinstance(column, int):
        return
    if column > dimension(board) or column <= 0:
        return

    for position in board.copy():
        if position[0] == column:
            board.pop(position)


def can_be_dropped_at(board, block, position):
    """
        Check whether the given block can be dropped at the given position.
        - The given position determines the position for the anchor of the
          given block.
        - True if and only if for each of the dot positions D of the given block
          there is a FREE cell at a position within the boundaries of the given
          board and at the same horizontal- and vertical distance from the
          given position as the horizontal- and vertical distance of the dot
          position D from the anchor of the given block.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        - The given position is a proper position.
    """

    # dot_positions = Block.get_all_dot_positions(block)
    # copy_dot_positions = dot_positions.copy()
    # delta_x = position[0]
    # delta_y = position[1]
    #
    # for pos in copy_dot_positions:
    #     location = Position.translate_over(pos, delta_x, delta_y)
    #     dot_positions.remove(pos)
    #     dot_positions.add(location)
    # for dot in dot_positions:
    #     if dot not in board:
    #         return False
    #     if board[dot] == 'Filled':
    #         return False
    # return True

    dot_positions = Block.get_all_dot_positions(block)

    new_anchor_position = min(dot_positions)
    anchor = Position.translate_over((0, 0), - new_anchor_position[0], - new_anchor_position[1])
    anchor_board_position = (position[0] - anchor[0], position[1] - anchor[1])

    normalised_block = Block.normalize(block)
    normalised_dot_positions = Block.get_all_dot_positions(normalised_block)
    new_dot_positions = set()

    for dot in normalised_dot_positions:
        new_dot = Position.translate_over(dot, anchor_board_position[0], anchor_board_position[1])
        new_dot_positions.add(new_dot)

    for dot in new_dot_positions:
        if not Position.is_proper_position_for_board(dimension(board), dot):
            return False
        if is_filled_at(board, dot):
            return False
    return True


the_block = Block.make_block({(-2, -2), (-2, -1), (-1, -1)})
the_board = make_board(4,
                       {(2, 4), \
                        (2, 3),
                        (1, 2), (2, 2), (4, 2),
                        (2, 1), (4, 1)})
print(can_be_dropped_at(the_board, the_block, (6, 6)))


def get_droppable_positions(board, block):
    """
        Return a list of all positions at which the given block can be dropped
        on the given board.
        - The positions in the resulting list are in ascending order.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        NOTE
        - The function should only examine positions at which the given block
          fully fits within the boundaries of the given board.
    """

    droppable_positions = list()
    dot_positions = Block.get_all_dot_positions(block)
    old_anchor = min(dot_positions)
    h_offset = Block.get_horizontal_offsets_from_anchor(block)
    v_offset = Block.get_vertical_offsets_from_anchor(block)
    vertical = abs(v_offset[0] - v_offset[1])
    horizontal = abs(h_offset[0] - h_offset[1])

    for a in range(1, dimension(board) - horizontal + 1):
        for b in range(1, dimension(board) - vertical + 1):
            pos = (a, b)
            print("pos", pos)
            anchor_position = (pos[0] - old_anchor[0], pos[1] - old_anchor[1])
            for dot in dot_positions:
                print("dot", dot)
                dot_board_position = (dot[0] + anchor_position[0], dot[1] + anchor_position[1])
                if Position.is_proper_position_for_board(dimension(board), dot_board_position):
                    if can_be_dropped_at(board, block, anchor_position) and anchor_position not in droppable_positions:
                        droppable_positions.append(anchor_position)

    droppable_positions = sorted(droppable_positions)
    return droppable_positions


the_block = Block.make_block({(-2, -2), (-2, -1), (-1, -1)})
the_board = make_board(4, {(1, 1), (1, 4), (2, 2), (3, 3), (4, 1), (4, 4)})
print(get_droppable_positions(the_board, the_block))  # == \


# [(3, 4), (4, 5), (5, 3)]

def drop_at(board, block, position):
    """
        Drop the given block at the given position on the given board.
        - Each of the cells on the given board at a position with the same
          horizontal- and vertical distance from the given position as a dot
          position of the given block from the block's anchor, is filled.
        - Nothing happens if the given block can not be dropped at the given
          position on the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given position is a proper position.
        - The given block is a proper block.
    """
    dot_positions = Block.get_all_dot_positions(block)
    copy_dot_positions = dot_positions.copy()

    for dot in copy_dot_positions:
        new_dot = Position.translate_over(dot, position[0], position[1])
        dot_positions.remove(dot)
        dot_positions.add(new_dot)

    if can_be_dropped_at(board, block, position):
        for dot in dot_positions:
            fill_cell(board, dot)


def clear_full_rows_and_columns(board):
    """
        Clear all full rows and all full columns on the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """

    filled_rows = get_all_filled_rows(board)
    filled_columns = get_all_filled_columns(board)

    for row in filled_rows:
        free_row(board, row)
    for col in filled_columns:
        free_column(board, col)


def are_chainable(board, positions, filled_positions=None):
    """
        Check whether the given collection of positions is chained on the
        given board.
        - True if and only if at least one collection of chained positions exists
          on the given board that includes all given positions and for which all
          the cells in that collection are either all filled or all empty.
        ASSUMPTIONS
        - The given board is a proper board.
        - Each of the given positions is a proper position for the given board.
        - All the cells on the given board at the given positions all have the
          same state, i.e. they are all filled or all empty.
        NOTE
        - This function should be worked out in a recursive way
    """
    chain = set(positions)
    current_positions = set()
    positions = sorted(list(positions))
    state = ''

    if filled_positions is None:
        filled_positions = sorted(list(get_all_filled_positions(board)))
        print(filled_positions)

    if Position.are_chained(chain):
        return True
    if len(filled_positions) == 0:
        return False

    state = board[positions[0]]

    if state == "Filled":
        if board[filled_positions[0]] == state:
            chain.add(filled_positions[0])
            current_positions.add(filled_positions[0])
            print("chain", chain)
    if Position.are_chained(current_positions):
        print('filled', filled_positions)
        print('pos', positions)
        print(are_chainable(board, positions[1:], filled_positions[1:]))
        return are_chainable(board, positions[1:], filled_positions[1:])


# the_board = make_board(4, {(2, 2), (2, 1)})
# assert are_chainable(the_board, [(1, 2), (1, 3), (1, 4)])
# assert are_chainable(the_board, {(2, 2), (2, 1)})
# the_board = make_board(4)
# assert are_chainable(the_board, [])
# assert are_chainable(the_board, ((2, 2),))
# the_board = make_board(4, \
#                              {(2, 4), (3, 4), \
#                               (2, 3), (4, 3), \
#                               (1, 2), (2, 2), (4, 2), \
#                               (1, 1), (2, 1), (4, 1), \
#                               })
# assert are_chainable(the_board, [(1, 2), (3, 4)])
# assert are_chainable(the_board, [(1, 1), (2, 3), (3, 4)])
# assert are_chainable(the_board, {(4, 1), (4, 3)})
# assert are_chainable(the_board, {(3, 1), (3, 3)})


def print_board(board):
    """111
        Print the given board on the standard output stream.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    for row in range(dimension(board), 0, -1):
        print('{:02d}'.format(row), end=" ")
        for column in range(1, dimension(board) + 1):
            if is_filled_at(board, (column, row)):
                print("  \u25A9", end=" ")
            else:
                print("   ", end="  ")
        print()
    print("    ", end="")
    for column in range(1, dimension(board) + 1):
        print('{:02d}'.format(column), end="   ")
    print()

# the_board = make_board(4, \
#                        {(3, 4), \
#                         (2, 3), (4, 3), \
#                         (1, 2), (2, 2), (4, 2), \
#                         (1, 1), (2, 1), (4, 1), \
#                         })
# print(are_chainable(the_board, [(1, 2), (2, 3), (3, 4)]))
# print_board(the_board)

# assert not are_chainable(the_board, {(1, 1), (4, 1)})
# assert not are_chainable(the_board, {(1, 3), (3, 1)})
# assert not are_chainable(the_board, {(4, 4), (3, 3)})
