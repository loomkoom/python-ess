import Block
import Board
import Game


# tests for highest_score

def test_highest_score__Empty_List(score, max_score):
    """Function highest_score: empty list of blocks."""
    max_score.value += 4
    try:
        positions_to_fill = {(1, 3), (4, 7), (2, 8), (5, 5)}
        the_board = Board.make_board(10, positions_to_fill)
        assert Game.highest_score(the_board, []) == (0, [])
        assert Board.get_all_filled_positions(the_board) == positions_to_fill
        score.value += 4
    except:
        pass


def test_highest_score__Single_Block_Single_Solution(score, max_score):
    """Function highest_score: single block highest score at one position."""
    max_score.value += 8
    try:
        positions_to_fill = {(1, 1), (1, 4), (2, 2), (3, 3), (4, 4)}
        the_board = Board.make_board(4, positions_to_fill)
        block = Block.make_block({(0, 0), (1, 0), (2, 0)})
        assert Game.highest_score(the_board, [block]) == (3 + 10, [(2, 1)])
        assert Board.get_all_filled_positions(the_board) == positions_to_fill
        score.value += 8
    except:
        pass


def test_highest_score__Full_Line_Drop(score, max_score):
    """Function highest_score: full line drop."""
    max_score.value += 8
    try:
        the_board = Board.make_board(4)
        block = Block.make_block({(0, 0), (1, 0), (2, 0), (3, 0)})
        assert Game.highest_score(the_board, [block]) == (4 + 10, [(1, 1)])
        assert Board.get_all_filled_positions(the_board) == set()
        score.value += 8
    except:
        pass


def test_highest_score__Full_Board_Drop(score, max_score):
    """Function highest_score: full board drop."""
    max_score.value += 15
    try:
        the_board = Board.make_board(2)
        block = Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)})
        assert Game.highest_score(the_board, [block, block, block]) == \
               (3 * (4 + 10 * 5 * 4 // 2), [(1, 1), (1, 1), (1, 1)])
        assert Board.get_all_filled_positions(the_board) == set()
        score.value += 15
    except:
        pass


def test_highest_score__Single_Block_Several_Solutions(score, max_score):
    """Function highest_score: single block highest score at several positions."""
    max_score.value += 8
    try:
        positions_to_fill = {(1, 1), (2, 2), (3, 3), (4, 4)}
        the_board = Board.make_board(4, positions_to_fill)
        block = Block.make_block({(0, 0), (1, 0), (2, 0)})
        assert Game.highest_score(the_board, [block]) == (3 + 10, [(1, 4)])
        assert Board.get_all_filled_positions(the_board) == positions_to_fill
        score.value += 8
    except:
        pass


def test_highest_score__Single_Non_Droppable_Block(score, max_score):
    """Function highest_score: single non-droppable block."""
    max_score.value += 4
    try:
        positions_to_fill = {(1, 1), (2, 2)}
        the_board = Board.make_board(2, positions_to_fill)
        block = Block.make_block({(0, 0), (1, 0), (2, 0)})
        assert Game.highest_score(the_board, [block]) == (None, None)
        assert Board.get_all_filled_positions(the_board) == positions_to_fill
        score.value += 4
    except:
        pass


def test_highest_score__Pair_Blocks_Single_Solution(score, max_score):
    """Function highest_score: pair of blocks single best solution."""
    max_score.value += 15
    try:
        the_board = Board.make_board(3)
        blocks = \
            [Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)}),
             Block.make_block({(0, 0), (-1, 0), (-2, 0), (0, -1), (0, -2)})]
        assert Game.highest_score(the_board, blocks) == (4 + (5 + 10 * (6 * 7 // 2)), [(1, 1), (3, 3)])
        assert Board.get_all_filled_positions(the_board) == set()
        assert Game.game_move(the_board, blocks[0], (1, 1)) == 4
        assert Game.game_move(the_board, blocks[1], (3, 3)) == 5 + 10 * 6 * 7 // 2
        assert Board.get_all_filled_positions(the_board) == set()
        score.value += 15
    except:
        pass


def test_highest_score__Pair_Blocks_Several_Solutions(score, max_score):
    """Function highest_score: pair of blocks several best solutions."""
    max_score.value += 12
    try:
        the_board = Board.make_board(5)
        blocks = \
            [Block.make_block({(-1, 0), (0, 0), (0, 1)}),
             Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)})]
        # No full lines nor full columns are possible in this configuration
        assert Game.highest_score(the_board, blocks) == (7, [(2, 1), (1, 3)])
        assert Board.get_all_filled_positions(the_board) == set()
        score.value += 12
    except:
        pass


def test_highest_score__Pair_Blocks_Non_Empty_Board(score, max_score):
    """Function highest_score: non-empty board."""
    max_score.value += 12
    try:
        the_board = Board.make_board(4, {(2, 1)})
        blocks = \
            [Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)}),
             Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)})]
        assert Game.highest_score(the_board, blocks) == (4 + 4 + 10 * 2 * 3 // 2, [(1, 2), (3, 2)])
        assert Board.get_all_filled_positions(the_board) == set([(2, 1)])
        assert Game.game_move(the_board, blocks[0], (1, 2)) == 4
        assert Game.game_move(the_board, blocks[1], (3, 2)) == 4 + 10 * 2 * 3 // 2
        assert Board.get_all_filled_positions(the_board) == set([(2, 1)])
        score.value += 12
    except:
        pass


def test_highest_score__4_Blocks_Possible_Solution(score, max_score):
    """Function highest_score: 4 blocks with a possible solution."""
    max_score.value += 25
    try:
        the_board = Board.make_board(4,
                                     {(3, 1), (2, 3), (4, 2)})
        blocks = \
            [Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)}),
             Block.make_block({(0, 0), (0, 1), (0, 2), (0, 3)}),
             Block.make_block({(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)}),
             Block.make_block({(0, 0), (0, 1), (0, 2)})]
        assert Game.highest_score(the_board, blocks) == \
               (4 + 34 + 36 + 13, [(3, 3), (1, 1), (1, 2), (4, 1)])
        assert Board.get_all_filled_positions(the_board) == {(3, 1), (2, 3), (4, 2)}
        assert Game.game_move(the_board, blocks[0], (3, 3)) == 4
        assert Game.game_move(the_board, blocks[1], (1, 1)) == 34
        assert Game.game_move(the_board, blocks[2], (1, 2)) == 36
        assert Game.game_move(the_board, blocks[3], (4, 1)) == 13
        assert Board.get_all_filled_positions(the_board) == {(1, 3), (2, 3)}
        score.value += 25
    except:
        pass


def test_highest_score__4_Blocks_Possible_Solution2(score, max_score):
    """Function highest_score: 4 blocks with possible solution (2nd config)."""
    max_score.value += 25
    try:
        the_board = Board.make_board(4,
                                     {(2, 2), (4, 3), (1, 4)})
        blocks = \
            [Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)}),
             Block.make_block({(0, 0), (0, 1), (1, 0)}),
             Block.make_block({(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)}),
             Block.make_block({(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)})]
        assert Game.highest_score(the_board, blocks) == \
               (4 + 13 + 66 + 39, [(2, 3), (1, 1), (2, 1), (1, 1)])
        assert Board.get_all_filled_positions(the_board) == {(2, 2), (4, 3), (1, 4)}
        assert Game.game_move(the_board, blocks[0], (2, 3)) == 4
        assert Game.game_move(the_board, blocks[1], (1, 1)) == 13
        assert Game.game_move(the_board, blocks[2], (2, 1)) == 66
        assert Game.game_move(the_board, blocks[3], (1, 1)) == 39
        assert Board.get_all_filled_positions(the_board) == {(3, 2), (3, 1), (2, 1), (2, 2)}
        score.value += 25
    except:
        pass


def test_highest_score__Several_Blocks_No_Solution(score, max_score):
    """Function highest_score: several blocks no solution."""
    max_score.value += 15
    try:
        positions_to_fill = {(2, 2), (2, 3), (4, 1), (4, 4), (5, 2)}
        the_board = Board.make_board(5, positions_to_fill)
        blocks = \
            [Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)}),
             Block.make_block({(0, 0), (1, 0), (2, 0)}),
             Block.make_block({(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)}),
             Block.make_block({(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)})]
        assert Game.highest_score(the_board, blocks) == (None, None)
        assert Board.get_all_filled_positions(the_board) == positions_to_fill
        score.value += 15
    except:
        pass


def test_highest_score__Larger_Sequence_Blocks(score, max_score):
    """Function highest_score: larger sequence of blocks."""
    max_score.value += 50
    try:
        positions_to_fill = \
            {(1, 4), (2, 1), (3, 2), (3, 4), (3, 6), (4, 2), (5, 1), (5, 3), (5, 4), (5, 6), (6, 3), (6, 5)}
        the_board = Board.make_board(6, positions_to_fill)
        blocks = \
            [Block.make_block({(-3, 0), (-2, 0), (-1, 0), (0, 0)}),
             Block.make_block({(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)}),
             Block.make_block({(-2, 2), (-2, 3), (-2, 4), (-2, 5)}),
             Block.make_block({(0, 0), (0, 1), (1, 0)}),
             Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)}),
             Block.make_block({(0, 0), (1, 0), (2, 0)}),
             Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)}),
             Block.make_block({(0, 0), (1, 0), (2, 0)}),
             Block.make_block \
                 ({(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), \
                   (1, 2), (2, 2)}),
             Block.make_block({(0, 0)})]
        assert Game.highest_score(the_board, blocks) == \
               (132, [(4, 3), (1, 3), (8, 1), (5, 2), (1, 2), \
                      (1, 5), (3, 1), (3, 5), (2, 4), (1, 6)])
        Game.game_move(the_board, blocks[0], (4, 3))
        Game.game_move(the_board, blocks[1], (1, 3))
        Game.game_move(the_board, blocks[2], (8, 1))
        Game.game_move(the_board, blocks[3], (5, 2))
        Game.game_move(the_board, blocks[4], (1, 2))
        Game.game_move(the_board, blocks[5], (1, 5))
        Game.game_move(the_board, blocks[6], (3, 1))
        Game.game_move(the_board, blocks[7], (2, 4))
        Game.game_move(the_board, blocks[8], (3, 3))
        Game.game_move(the_board, blocks[9], (2, 6))
        assert Board.get_all_filled_positions(the_board) == \
               {(2, 1), (2, 6), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4), (5, 1), (5, 3), (5, 4), (5, 6), (6, 6)}
        score.value += 50
    except:
        pass


# tests for greedy_play

def test_play_greedy__Empty_List(score, max_score):
    """Function play_greedy: empty list of blocks."""
    max_score.value += 2
    try:
        positions_to_fill = {(1, 3), (4, 7), (2, 8), (5, 5)}
        the_board = Board.make_board(10, positions_to_fill)
        assert Game.play_greedy(the_board, []) == 0
        assert Board.get_all_filled_positions(the_board) == positions_to_fill
        score.value += 2
    except:
        pass


def test_play_greedy__Single_Block(score, max_score):
    """Function play_greedy: single_block."""
    max_score.value += 5
    try:
        positions_to_fill = {(1, 3), (2, 1), (2, 3), (3, 1), (3, 5)}
        the_board = Board.make_board(5, positions_to_fill)
        the_block = Block.make_block \
            ({(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), \
              (1, 2), (2, 2)})
        assert Game.play_greedy(the_board, [the_block]) == 9 + 10 * 3 * 2 // 2
        assert Board.get_all_filled_positions(the_board) == \
               {(5, 4), (4, 4), (2, 1), (4, 2), (5, 2)}
        score.value += 5
    except:
        pass


def test_play_greedy__Pair_Of_Blocks(score, max_score):
    """Function play_greedy: pair of blocks."""
    max_score.value += 8
    try:
        positions_to_fill = {(1, 1), (1, 3)}
        the_board = Board.make_board(4, positions_to_fill)
        blocks = \
            (Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1), }),
             Block.make_block({(0, 0), (-1, 0), (0, -1)}))
        assert Game.play_greedy(the_board, blocks) == 4 + 3 + 10 * 3 * 2 // 2;
        assert Board.get_all_filled_positions(the_board) == {(1, 3)}
        score.value += 8
    except:
        pass


def test_play_greedy__Triplet_Of_Blocks(score, max_score):
    """Function play_greedy: triplet of blocks."""
    max_score.value += 8
    try:
        positions_to_fill = {(1, 1), (4, 4)}
        the_board = Board.make_board(4, positions_to_fill)
        blocks = \
            (Block.make_block({(0, 0)}),
             Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1), }),
             Block.make_block({(0, 0), (-1, 0)}))
        assert Game.play_greedy(the_board, blocks) == 1 + 4 + 2 + 10 * 3 * 2 // 2;
        # assert Board.get_all_filled_positions(the_board) == {(4, 4)}
        score.value += 8
    except:
        pass


def test_play_greedy__Octet_Of_Blocks(score, max_score):
    """Function play_greedy: octet of blocks."""
    max_score.value += 20
    try:
        positions_to_fill = {(3, 1), (5, 2), (4, 4)}
        the_board = Board.make_board(5, positions_to_fill)
        blocks = \
            (Block.make_block \
                 ({(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), \
                   (1, 2), (2, 2)}),
             Block.make_block({(0, 0), (1, 0)}),
             Block.make_block({(0, 0), (-1, 0)}),
             Block.make_block({(0, 0), (0, 1), (1, 1)}),
             Block.make_block({(0, 0), (-1, 0), (1, 0)}),
             Block.make_block({(1, 1), (1, 2)}),
             Block.make_block({(-1, 0), (0, 0), (0, 1)}),
             Block.make_block({(-2, 0), (-1, 0), (0, 0)}))
        assert Game.play_greedy(the_board, blocks) == 43 + 38 + 16;
        # assert Board.get_all_filled_positions(the_board) == \
        #        {(2, 3), (2, 4), (2, 5), (3, 5), (4, 4), (5, 2)}
        score.value += 20
    except:
        pass


def test_play_greedy__No_Solution(score, max_score):
    """Function play_greedy: no solution."""
    max_score.value += 20
    try:
        positions_to_fill = {(2, 1), (2, 2), (3, 1), (5, 2), (4, 4)}
        the_board = Board.make_board(5, positions_to_fill)
        blocks = \
            (Block.make_block \
                 ({(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), \
                   (1, 2), (2, 2)}),
             Block.make_block({(0, 0), (1, 0), (2, 0), (3, 0)}),
             Block.make_block({(0, 0), (-1, 0), (0, 1), (1, 1)}),
             Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)}),
             Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)}),
             Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)}))
        assert Game.play_greedy(the_board, blocks) == None;
        # assert Board.get_all_filled_positions(the_board) == \
        #        {(4, 2), (4, 4), (5, 2), (1, 4)}
        score.value += 20
    except:
        pass


def test_play_greedy__Larger_Sequence_Blocks(score, max_score):
    """Function play_greedy: larger sequence of blocks."""
    max_score.value += 37
    try:
        # This is that same game as in the last test for highest_score
        positions_to_fill = \
            {(1, 4), (2, 1), (3, 2), (3, 4), (3, 6), (4, 2), (5, 1), (5, 3), (5, 4), (5, 6), (6, 3), (6, 5)}
        the_board = Board.make_board(6, positions_to_fill)
        blocks = \
            [Block.make_block({(-3, 0), (-2, 0), (-1, 0), (0, 0)}),
             Block.make_block({(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)}),
             Block.make_block({(-2, 2), (-2, 3), (-2, 4), (-2, 5)}),
             Block.make_block({(0, 0), (0, 1), (1, 0)}),
             Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)}),
             Block.make_block({(0, 0), (1, 0), (2, 0)}),
             Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)}),
             Block.make_block({(0, 0), (1, 0), (2, 0)}),
             Block.make_block \
                 ({(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), \
                   (1, 2), (2, 2)}),
             Block.make_block({(0, 0)})]
        assert Game.play_greedy(the_board, blocks) is None
        # assert Board.get_all_filled_positions(the_board) == \
        #        {(1, 3), (5, 6), (2, 1), (6, 2), (1, 6), (5, 1), (1, 2), (3, 6), (2, 2),
        #         (6, 4), (3, 2), (5, 4), (2, 6), (1, 4), (4, 2), (6, 1), (3, 4)}
        score.value += 37
    except:
        pass


game_test_functions = \
    {
        test_highest_score__Empty_List,
        test_highest_score__Single_Block_Several_Solutions,
        test_highest_score__Single_Block_Single_Solution,
        test_highest_score__Full_Line_Drop,
        test_highest_score__Full_Board_Drop,
        test_highest_score__Single_Non_Droppable_Block,
        test_highest_score__Pair_Blocks_Single_Solution,
        test_highest_score__Pair_Blocks_Several_Solutions,
        test_highest_score__Pair_Blocks_Non_Empty_Board,
        test_highest_score__4_Blocks_Possible_Solution,
        test_highest_score__4_Blocks_Possible_Solution2,
        test_highest_score__Several_Blocks_No_Solution,
        test_highest_score__Larger_Sequence_Blocks,

        test_play_greedy__Empty_List,
        test_play_greedy__Single_Block,
        test_play_greedy__Pair_Of_Blocks,
        test_play_greedy__Triplet_Of_Blocks,
        test_play_greedy__Octet_Of_Blocks,
        test_play_greedy__No_Solution,
        test_play_greedy__Larger_Sequence_Blocks,
    }

