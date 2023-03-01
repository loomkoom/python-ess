import Board

def lowest_moves_f(board, blocks, start = 0):

    lowest_moves = None
    dropped_positions = None

    if len(board.get_droppable_positions(board, blocks[start]))==0:
        return []

    current_block = blocks[start]
    droppable_positions = sorted(Board.get_droppable_positions(board, current_block))

    for pos in droppable_positions:
        board_copy = Board.copy_board(board)

        last_score = game_move(board_copy, current_block, pos)
        filled_positions = Board.get_all_filled_positions(board_copy) - Board.get_all_filled_positions(board)
        rec_positions = lowest_moves_f(board_copy, blocks, start + 1)

        Board.free_all_cells(board_copy, filled_positions)
        if rec_positions is not None and (last_score is not None):
            moves = len(rec_positions) + 1
            if (lowest_moves is None) or (moves < lowest_moves):
                lowest_moves = moves
                dropped_positions = [pos] + rec_positions

    return dropped_positions







def game_move(board, block, position):
    """
        Drop the given block at the given position on the given board, and
        clear all full rows and columns, if any, after the drop.
        - The function returns the score obtained from the give move.
        ASSUMPTIONS
        - The given board is a proper board
        - The given block is a proper block.
        - The given position is a proper position.
        - The given block can be dropped at the given position on the given
          board.
    """

    Board.drop_at(board, block, position)
    nb_filled_seqs = \
        len(Board.get_all_filled_columns(board)) + \
        len(Board.get_all_filled_rows(board))
    Board.clear_full_rows_and_columns(board)
    return \
        len(Block.get_all_dot_positions(block)) + \
        10 * ((nb_filled_seqs + 1) * nb_filled_seqs) // 2