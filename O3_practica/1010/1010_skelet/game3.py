import Board

def highest_score(board, blocks, start = 0):

    high_score = None
    dropped_positions = None

    if len(blocks) == 0 or start == len(blocks):
        return (0, [])

    current_block = blocks[start]
    droppable_positions = sorted(Board.get_droppable_positions(board, current_block))

    for pos in droppable_positions:
        board_copy = Board.copy_board(board)

        last_score = game_move(board_copy, current_block, pos)
        filled_positions = Board.get_all_filled_positions(board_copy) - Board.get_all_filled_positions(board)
        rec_sol = rec_score, rec_positions = highest_score(board_copy, blocks, start + 1)

        Board.free_all_cells(board_copy, filled_positions)
        if rec_sol[0] is not None and (last_score is not None):
            score = last_score + rec_score
            if (high_score is None) or (score > high_score):
                high_score = score
                dropped_positions = [pos] + rec_positions

    return (high_score, dropped_positions)







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