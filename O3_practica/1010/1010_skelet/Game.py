import itertools
import random

import Block
import Board


def highest_score(board, blocks, start = 0):
    """
        Return the highest possible score that can be obtained by dropping
        all the blocks in the given sequence of blocks starting from the given
        start index in the order from left to right on the given board.
        - If a solution is possible, the function actually returns a tuple
          consisting of the highest score followed by a list of all positions
          at which the successive blocks must be dropped.
        - If the highest score can be reached in several possible ways, the
          function will give preference to the smallest position in the sense of
          the standard tuple comparison in Python (see section 6.7 of the book).
          For example, if there are two solutions s1 and s2 and s1 < s2, s1 will
          be returned.
        - If no solution is possible, the function returns the tuple (None,None).
        - At the end of the function, the board must still be in the same
          state it was in at the start of the function.
        ASSUMPTIONS
        - The given board is a proper board.
        - Each block in the given sequence of blocks is a proper block.
        - The given start index is not negative, but may be beyond the last element
          in the sequence of blocks.
        NOTE
        - You are allowed to take a copy of the given board.
        - You are not allowed to extend the heading of the function with
          additional parameters, nor to introduce an auxiliary function
          to be able to pass additional information.
        - The function should be worked out in a recursive way.
    """

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


def play_greedy(board, blocks):
    """
    Drop the given sequence of blocks on the given board in a greedy way.
        - The function will take blocks in triplets (groups of 3) in the order from
          left to right. Within each triplet, the blocks are dropped on the given board
          in the optimal order (i.e. yielding the highest possible score),
          without taking into account blocks from subsequent triplets that
          still need to be dropped further on.
        - If the number of blocks is not a multiple of 3, the function will take the
          remaining blocks (1 or 2) in the last step.
        - In dropping the blocks in a triplet, the function will search for the best
          possible order to drop each of the 3 blocks to yield the highest possible
          score.
        - If a solution is possible, the function returns the total score obtained
          from dropping all the blocks.
        - If no solution is possible, the function returns None. All the triplets that
          could be dropped are effectively dropped on the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """

    grouped_blocks = [None for k in range(len(blocks) // 3)]
    all_moves, best_moves = [], []
    high_score, total_score = 0, 0
    ALL_TRIPLETS_DROPPED = True

    if len(blocks) == 0:
        return 0
    if len(blocks) == 1:
        score, move = highest_score(board, blocks)
        game_move(board, blocks[0], move[0])
        return score

    for n in range((len(blocks) // 3)):
        grouped_blocks[n] = tuple(blocks[n * 3:(n + 1) * 3])
    if len(blocks) % 3 > 0:
        grouped_blocks += (tuple(blocks[-(len(blocks) % 3):]),)

    for triplet_nb in range(len(grouped_blocks)):
        triplet_combinations = list(itertools.permutations(grouped_blocks[triplet_nb]))
        for combination in range(0, len(triplet_combinations)):
            score, moves = highest_score(board, triplet_combinations[combination])
            if moves is not None:
                if (score > high_score) or (high_score == score and (best_moves != [] and moves < best_moves)):
                    high_score, best_moves = score, moves
                    grouped_blocks[triplet_nb] = triplet_combinations[combination]
        total_score += high_score
        all_moves.append(best_moves)
        high_score, best_moves = 0, []

        for block in grouped_blocks[triplet_nb]:
            block_nb = grouped_blocks[triplet_nb].index(block)
            if len(all_moves[triplet_nb]) == 0:
                ALL_TRIPLETS_DROPPED = False
                break
            game_move(board, block, all_moves[triplet_nb][block_nb])

    if ALL_TRIPLETS_DROPPED:
        
        return total_score
    return None


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




def play_game():
    """
        Play the 
    """
    the_board = Board.make_board(5)
    score = 0
    current_block = Block.select_standard_block()
    print("Score: ", score)
    print()
    print("Next block to drop:")
    Block.print_block(current_block)
    print()
    Board.print_board(the_board)
    print()

    while len(Board.get_droppable_positions(the_board, current_block)) > 0:

        position = input("Enter the position to drop the block: ")
        if position == "":
            position = \
                random.choice(Board.get_droppable_positions(the_board, current_block))
            print("   Using position: ", position[0], ",", position[1])
        else:
            position = eval(position)
            if not isinstance(position, tuple):
                print("Not a valid position")
                continue

        if not Board.can_be_dropped_at(the_board, current_block, position):
            print("Block cannot be dropped at the given position")
            continue

        score += game_move(the_board, current_block, position)

        current_block = Block.select_standard_block()
        print("Score: ", score)
        print()
        print("Next block to drop:")
        Block.print_block(current_block)
        print()
        Board.print_board(the_board)
        print()

    print("End of game!")
    print("   Final score: ", score)


if __name__ == '__main__':
    play_game()
