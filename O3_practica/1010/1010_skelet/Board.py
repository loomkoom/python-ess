import Block
import Position


def make_board(dimension = 10, positions_to_fill = frozenset()):
    """
        Return a new board of the given dimension for which all cells at the
        given positions are already filled.
        ASSUMPTIONS
        - The given dimension is a positive integer number.
        - The filled positions is a collection of proper positions. Positions
          outside the boundaries of the new board have no impact on the content
          of the new board.
    """
    board = dict()
    max_pos = (dimension, dimension)
    board[max_pos] = 'Free'

    for position in positions_to_fill:
        if Position.is_proper_position_for_board(dimension, position):
            board[position] = 'Filled'

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
        Check whether the given board is a proper board.
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
        if board[pos] != 'Free' and board[pos] != 'Filled':
            return False
        if not Position.is_proper_position_for_board(dimension(board), pos):
            return False
    return True


def dimension(board):
    """
        Return the dimension of the given board.
        - The function returns the number of rows (== number of columns) of
          the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """

    dim = max(board)[0]

    return dim


def get_all_filled_positions(board):
    """
        Return a set of all the positions of filled cells on the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    filled_positions = set()

    for pos in board:
        if board[pos] == 'Filled':
            filled_positions.add(pos)

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
    if position in board:
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
    if not isinstance(row, int):
        return False
    if not (dimension(board) >= row > 0):
        return False
    position = (1, row)
    while Position.is_proper_position_for_board(dimension(board), position):
        if not is_filled_at(board, position):
            return False
        position = (Position.col(position) + 1, row)
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
    if not (dimension(board) >= column > 0):
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
        - The given board is proper board.
        NOTE
        - You are not allowed to use for statements in the body of this function.
    """
    filled_rows = list()
    row = 1

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
    filled_columns = tuple()

    for column in range(1, dimension(board) + 1):
        if is_filled_column(board, column):
            filled_columns += (column,)

    return filled_columns[::-1]


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
        if position not in board or board[position] == 'Free':
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
    #dim = dimension(board)
    for pos in positions:
        fill_cell(board,pos)
        # if Position.is_proper_position_for_board(dim, pos):
        #     if pos not in board or board[pos] == 'Free':
        #         board[pos] = 'Filled'


def free_cell(board, position):
    """
        Free the cell at the given position of the given board.
        - Nothing happens if the cell is already free or if the given
          position is outside the boundaries of the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given position is a proper position.
    """
    dim = dimension(board)
    if Position.is_proper_position_for_board(dim, position):
        if position == (dim, dim):
            board[position] = 'Free'
        elif position in board:
            del board[position]


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
    positions = list(positions)

    if len(positions) == 0:
        return

    if Position.is_proper_position_for_board(dimension(board), positions[0]):
        if positions[0] in board and board[positions[0]] != 'Free':
            free_cell(board, positions[0])

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
    if not 1 <= row <= dimension(board):
        return

    for pos in copy_board(board):
        if Position.row(pos) == row:
            free_cell(board, pos)


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
    if not 1 <= column <= dimension(board):
        return

    for pos in copy_board(board):
        if Position.col(pos) == column:
            free_cell(board, pos)


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

    dim = dimension(board)
    dot_positions = Block.get_all_dot_positions(block)
    new_anchor_position = min(dot_positions)
    anchor_board_position = Position.translate_over(position, Position.col(new_anchor_position), Position.row(new_anchor_position))

    normalised_block = Block.normalize(block)
    normalised_dot_positions = Block.get_all_dot_positions(normalised_block)
    new_dot_positions = set()

    for dot in normalised_dot_positions:
        new_dot = Position.translate_over(dot, Position.col(anchor_board_position), Position.row(anchor_board_position))
        new_dot_positions.add(new_dot)

    for dot in new_dot_positions:
        if not Position.is_proper_position_for_board(dim, dot):
            return False
        if is_filled_at(board, dot):
            return False
    return True


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
    dim = dimension(board)
    #dot_positions = Block.get_all_dot_positions(block)
    hor_left, hor_right = Block.get_horizontal_offsets_from_anchor(block)
    ver_down, ver_up = Block.get_vertical_offsets_from_anchor(block)

    for col in range(1 - hor_left, dim - hor_right + 1):
        for row in range(1 - ver_down, dim - ver_up + 1):
            anchor_position = (col, row)
            # for dot in dot_positions:
            #     dot_board_position = Position.translate_over(dot, Position.col(anchor_position), Position.row(anchor_position))
            #     if Position.is_proper_position_for_board(dim, dot_board_position):
            if can_be_dropped_at(board, block, anchor_position):# and anchor_position not in droppable_positions:
                droppable_positions.append(anchor_position)

    droppable_positions = sorted(droppable_positions)
    return droppable_positions

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
    new_dot_positions = set()

    for dot in dot_positions:
        new_dot = Position.translate_over(dot, Position.col(position), Position.row(position))
        new_dot_positions.add(new_dot)
    if can_be_dropped_at(board, block, position):
        for dot in new_dot_positions:
            fill_cell(board, dot)


def clear_full_rows_and_columns(board):
    """
        Clear all full rows and all full columns on the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    filled_columns = get_all_filled_columns(board)
    filled_rows = get_all_filled_rows(board)

    for column in filled_columns:
        free_column(board, column)
    for row in filled_rows:
        free_row(board, row)


def are_chainable(board, positions, targets = None, path = None):
    positions = sorted(list(positions))
    new_positions = []

    if len(positions) <= 1:
        return True

    current = positions[0]

    if path is None:
        path = list((current,))
    path.append(current)
    path = sorted(list(set(path)))
    if targets is None:
        targets = list(positions[1:])
    elif len(targets) > 1:
        for pos in targets:
            if current == pos:
                targets.remove(pos)
    else:
        for pos in targets:
            if pos in path and Position.are_chained(path):
                return True

    if is_filled_at(board, targets[-1]):
        state = "Filled"
    elif not is_filled_at(board, targets[-1]):
        state = "Free"

    for neighbour in Position.get_adjacent_positions(current, dimension(board)):
        if ((((state == "Filled") and (neighbour in board and board[neighbour] != "Free"))
             or ((state == "Free") and ((neighbour not in board) or (neighbour in board and board[neighbour] == "Free"))))) \
                and (neighbour not in path):

            next_pos = neighbour
            new_positions.append(next_pos)
            new_positions.extend(targets)

            solution = are_chainable(board, new_positions, targets, path)
            if solution is not False:
                return solution
    return False


def print_board(board):
    """111
        Print the given board on the standard output stream.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    for row in range(dimension(board), 0, -1):
        print('{:02d}'.format(row), end = " ")
        for column in range(1, dimension(board) + 1):
            if is_filled_at(board, (column, row)):
                print(" \u25A9 ", end = " ")
            else:
                print("    ", end = " ")
        print()
    print("     ", end = " ")
    for column in range(1, dimension(board) + 1):
        print('{:02d}'.format(column), end = "  ")
    print()
