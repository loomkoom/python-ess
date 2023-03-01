import Board
import Block


# tests for make_board

def test_Make_Board__No_Filled_Dots(score, max_score):
    """Function make_board: no filled dots."""
    max_score.value += 2
    try:
        the_board = Board.make_board(7)
        assert Board.dimension(the_board) == 7
        for column in range(1, 8):
            for row in range(1, 8):
                assert not Board.is_filled_at(the_board, (column, row))
        assert Board.get_all_filled_positions(the_board) == set()
        score.value += 2
    except:
        pass


def test_Make_Board__All_Positions_In_Boundaries(score, max_score):
    """Function make_board: all positions in boundaries."""
    max_score.value += 8
    try:
        positions_to_fill = [(1, 3), (4, 7), (6, 8), (10, 10), (1, 10), (10, 1)]
        the_board = Board.make_board(10, positions_to_fill)
        assert Board.dimension(the_board) == 10
        for column in range(1, 10):
            for row in range(1, 10):
                assert Board.is_filled_at(the_board, (column, row)) == \
                       ((column, row) in positions_to_fill)
        assert Board.get_all_filled_positions(the_board) == \
               set(positions_to_fill)
        score.value += 8
    except:
        pass


def test_Make_Board__Some_Positions_Outside_Boundaries(score, max_score):
    """Function make_board: some positions outside boundaries."""
    max_score.value += 6
    try:
        positions_to_fill = ((0, 0), (2, 3), (-3, 3), (4, -1), (5, 5), (2, 12), (16, 4))
        the_board = Board.make_board(5, positions_to_fill)
        assert Board.dimension(the_board) == 5
        for column in range(1, 10):
            for row in range(1, 10):
                assert Board.is_filled_at(the_board, (column, row)) == \
                       ((column, row) in {(2, 3), (5, 5)})
        assert Board.get_all_filled_positions(the_board) == {(2, 3), (5, 5)}
        score.value += 6
    except:
        pass


# tests for copy_board

def test_Copy_Board__Single_Case(score, max_score):
    """Function copy_board: single case"""
    max_score.value += 3
    try:
        positions_to_fill = ((1, 1), (2, 2), (3, 3))
        the_board = Board.make_board(3, positions_to_fill)
        copy_board = Board.copy_board(the_board)
        assert the_board is not copy_board
        assert Board.dimension(copy_board) == 3
        assert Board.get_all_filled_positions(copy_board) == \
               set(positions_to_fill)
        score.value += 3
    except:
        pass


# tests for is_proper_board

def test_Is_Proper_Board__True_Case(score, max_score):
    """Function is_proper_board: true case"""
    max_score.value += 3
    try:
        positions_to_fill = ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4))
        the_board = Board.make_board(3, positions_to_fill)
        assert Board.is_proper_board(the_board)
        score.value += 3
    except:
        pass


def test_Is_Proper_Board__False_Cases(score, max_score):
    """Function is_proper_board: false cases"""
    max_score.value += 2
    try:
        assert not Board.is_proper_board(None)
        assert not Board.is_proper_board("KU Leuven")
        assert not Board.is_proper_board(3.1416)
        assert not Board.is_proper_board([1, "abc", 5.67])
        score.value += 2
    except:
        pass


# tests for get_all_dot_positions

def test_Get_All_Dot_Positions__Hackers_Test1(score, max_score):
    """Function get_all_dot_positions: hacker's test 1."""
    max_score.value += 10
    try:
        positions_to_fill = {(2, 5), (1, 3), (4, 1), (5, 5)}
        the_board = Board.make_board(6, positions_to_fill)
        set.add(positions_to_fill, "hacker")
        board_filled_positions = Board.get_all_filled_positions(the_board)
        assert board_filled_positions == {(2, 5), (1, 3), (4, 1), (5, 5)}
        score.value += 10
    except:
        pass


def test_Get_All_Dot_Positions__Hackers_Test2(score, max_score):
    """Function get_all_dot_positions: hacker's test 2."""
    max_score.value += 10
    try:
        positions_to_fill = {(2, 5), (1, 3), (4, 1), (5, 5)}
        the_board = Board.make_board(6, positions_to_fill)
        board_filled_positions = Board.get_all_filled_positions(the_board)
        set.add(board_filled_positions, "hacker")
        assert Board.get_all_filled_positions(the_board) == \
               {(2, 5), (1, 3), (4, 1), (5, 5)}
        score.value += 10
    except:
        pass


# tests for is_filled_at

def test_Is_Filled_At__Outside_Boundaries(score, max_score):
    """Function is_filled_at: position outside boundaries"""
    max_score.value += 3
    try:
        the_board = Board.make_board(3)
        assert not Board.is_filled_at(the_board, (0, 0))
        assert not Board.is_filled_at(the_board, (4, 4))
        assert not Board.is_filled_at(the_board, (-1, 3))
        assert not Board.is_filled_at(the_board, (1, -3))
        score.value += 3
    except:
        pass


# tests for is_filled_row

def test_Is_Filled_Row__Invalid_Row(score, max_score):
    """Function is_filled_row: invalid row"""
    max_score.value += 1
    try:
        the_board = Board.make_board(3)
        assert not Board.is_filled_row(the_board, "CW")
        assert not Board.is_filled_row(the_board, 0)
        assert not Board.is_filled_row(the_board, 4)
        score.value += 1
    except:
        pass


def test_Is_Filled_Row__Row_Not_Filled(score, max_score):
    """Function is_filled_row: row not filled"""
    max_score.value += 2
    try:
        the_board = Board.make_board(4, \
                                     {(1, 4), (2, 4), (3, 4),
                                      (2, 3), (3, 3), (3, 4),
                                      (1, 2), (3, 2)})
        assert not Board.is_filled_row(the_board, 1)
        assert not Board.is_filled_row(the_board, 2)
        assert not Board.is_filled_row(the_board, 3)
        assert not Board.is_filled_row(the_board, 4)
        score.value += 2
    except:
        pass


def test_Is_Filled_Row__Row_Filled(score, max_score):
    """Function is_filled_row: row filled"""
    max_score.value += 2
    try:
        the_board = Board.make_board(3, {(1, 2), (2, 2), (3, 2)})
        assert Board.is_filled_row(the_board, 2)
        score.value += 2
    except:
        pass


# tests for is_filled_column

def test_Is_Filled_Column__Invalid_Column(score, max_score):
    """Function is_filled_column: invalid column"""
    max_score.value += 1
    try:
        the_board = Board.make_board(3)
        assert not Board.is_filled_column(the_board, "CW")
        assert not Board.is_filled_column(the_board, 0)
        assert not Board.is_filled_column(the_board, 4)
        score.value += 1
    except:
        pass


def test_Is_Filled_Column__Column_Not_Filled(score, max_score):
    """Function is_filled_column: column not filled"""
    max_score.value += 2
    try:
        the_board = Board.make_board(4,
                                     {(1, 4), (3, 4), (4, 4),
                                      (1, 3), (2, 3),
                                      (1, 2), (2, 2), (3, 2),
                                      (2, 1), (4, 1)})
        assert not Board.is_filled_column(the_board, 2)
        assert not Board.is_filled_column(the_board, 1)
        assert not Board.is_filled_column(the_board, 3)
        score.value += 2
    except:
        pass


def test_Is_Filled_Column__Column_Filled(score, max_score):
    """Function is_filled_column: column filled"""
    max_score.value += 2
    try:
        the_board = Board.make_board(3, {(2, 1), (2, 2), (2, 3)})
        assert Board.is_filled_column(the_board, 2)
        score.value += 2
    except:
        pass


# tests for get_all_filled_rows

def test_Get_All_Filled_Rows__Single_case(score, max_score):
    """Function get_all_filled_rows: single case"""
    max_score.value += 4
    try:
        the_board = Board.make_board(3)
        assert Board.get_all_filled_rows(the_board) == []
        the_board = Board.make_board(4, \
                                     {(1, 3), (2, 3), (3, 3), (4, 3), \
                                      (2, 2), \
                                      (1, 1), (2, 1), (3, 1), (4, 1)})
        assert Board.get_all_filled_rows(the_board) == [1, 3]
        score.value += 4
    except:
        pass


# tests for get_all_filled_columns

def test_Get_All_Filled_Columns__Single_case(score, max_score):
    """Function get_all_filled_columns: single case"""
    max_score.value += 4
    try:
        the_board = Board.make_board(3)
        assert Board.get_all_filled_columns(the_board) == ()
        the_board = Board.make_board(4, \
                                     {(1, 4), (4, 4), \
                                      (1, 3), (2, 3), (3, 3), (4, 3), \
                                      (1, 2), (2, 2), (4, 2), \
                                      (1, 1), (2, 1), (3, 1), (4, 1)})
        assert Board.get_all_filled_columns(the_board) == (4, 1)
        score.value += 4
    except:
        pass


# tests for fill_cell

def test_Fill_Cell__Non_Filled_Position(score, max_score):
    """Function fill_cell: non filled position"""
    max_score.value += 1
    try:
        the_board = Board.make_board(3)
        Board.fill_cell(the_board, (2, 3))
        assert Board.is_filled_at(the_board, (2, 3))
        assert Board.get_all_filled_positions(the_board) == {(2, 3)}
        score.value += 1
    except:
        pass


def test_Fill_Cell__Filled_Position(score, max_score):
    """Function fill_cell: filled position"""
    max_score.value += 1
    try:
        positions_to_fill = \
            {(1, 3), (2, 3), (3, 3), (4, 3), \
             (2, 2), \
             (1, 1), (2, 1), (3, 1), (4, 1)}
        the_board = Board.make_board(4, positions_to_fill)
        Board.fill_cell(the_board, (2, 3))
        assert Board.is_filled_at(the_board, (2, 3))
        assert Board.get_all_filled_positions(the_board) == positions_to_fill
        score.value += 1
    except:
        pass


def test_Fill_Cell__Outside_Boundaries(score, max_score):
    """Function fill_cell: outside boundaries"""
    max_score.value += 1
    try:
        positions_to_fill = \
            {(1, 3), (2, 3), (3, 3), (4, 3), \
             (2, 2), \
             (1, 1), (2, 1), (3, 1), (4, 1)}
        the_board = Board.make_board(4, positions_to_fill)
        Board.fill_cell(the_board, (5, 1))
        assert not Board.is_filled_at(the_board, (5, 1))
        assert Board.get_all_filled_positions(the_board) == positions_to_fill
        score.value += 1
    except:
        pass


# tests for fill_all_cells

def test_Fill_All_Cells__Single_Case(score, max_score):
    """Function fill_all_cells: single case"""
    max_score.value += 3
    try:
        the_board = Board.make_board(3, {(2, 3)})
        Board.fill_all_cells(the_board, [(1, 1), (4, 4), (2, 3), (1, 1), (-1, 9), (1, 1)])
        assert Board.is_filled_at(the_board, (2, 3))
        assert Board.is_filled_at(the_board, (1, 1))
        assert not Board.is_filled_at(the_board, (4, 4))
        assert not Board.is_filled_at(the_board, (-1, 9))
        assert Board.get_all_filled_positions(the_board) == {(2, 3), (1, 1)}
        score.value += 3
    except:
        pass


# tests for free_one

def test_Free_Cell__Non_Filled_Position(score, max_score):
    """Function free_cell: non filled position"""
    max_score.value += 1
    try:
        the_board = Board.make_board(3)
        Board.free_cell(the_board, (2, 3))
        assert not Board.is_filled_at(the_board, (2, 3))
        assert Board.get_all_filled_positions(the_board) == set()
        score.value += 1
    except:
        pass


def test_Free_Cell__Filled_Position(score, max_score):
    """Function free_cell: filled position"""
    max_score.value += 1
    try:
        positions_to_fill = \
            {(1, 3), (2, 3), (3, 3), (4, 3), \
             (2, 2), \
             (1, 1), (2, 1), (3, 1), (4, 1)}
        the_board = Board.make_board(4, positions_to_fill)
        Board.free_cell(the_board, (2, 3))
        assert not Board.is_filled_at(the_board, (2, 3))
        assert Board.get_all_filled_positions(the_board) == positions_to_fill - {(2, 3)}
        score.value += 1
    except:
        pass


def test_Free_One__Outside_Boundaries(score, max_score):
    """Function free_cell: outside boundaries"""
    max_score.value += 1
    try:
        positions_to_fill = \
            {(1, 3), (2, 3), (3, 3), (4, 3), \
             (2, 2), \
             (1, 1), (2, 1), (3, 1), (4, 1)}
        the_board = Board.make_board(4, positions_to_fill)
        Board.free_cell(the_board, (5, 1))
        assert not Board.is_filled_at(the_board, (5, 1))
        assert Board.get_all_filled_positions(the_board) == positions_to_fill
        score.value += 1
    except:
        pass


# tests for free_all_cells

def test_Free_All_Cells__Single_Case(score, max_score):
    """Function free_all_cells: single case"""
    max_score.value += 5
    try:
        the_board = Board.make_board(3, {(2, 3), (1, 1)})
        Board.free_all_cells(the_board, \
                             [(1, 1), (4, 4), (1, 1), (-1, 9), (1, 1)])
        assert Board.is_filled_at(the_board, (2, 3))
        assert not Board.is_filled_at(the_board, (1, 1))
        assert not Board.is_filled_at(the_board, (4, 4))
        assert not Board.is_filled_at(the_board, (-1, 9))
        assert Board.get_all_filled_positions(the_board) == {(2, 3)}
        score.value += 5
    except:
        pass


# tests for free_row

def test_Free_Row__Single_Case(score, max_score):
    """Function free_row: single case"""
    max_score.value += 2
    try:
        the_board = Board.make_board(4,
                                     {(2, 4), \
                                      (1, 2), (2, 2), (3, 2), (4, 2),
                                      (2, 1), (4, 1)})
        Board.free_row(the_board, 2)
        assert Board.get_all_filled_positions(the_board) == \
               {(2, 4), (2, 1), (4, 1)}
        Board.free_row(the_board, 3)
        assert Board.get_all_filled_positions(the_board) == \
               {(2, 4), (2, 1), (4, 1)}
        Board.free_row(the_board, 4)
        assert Board.get_all_filled_positions(the_board) == {(2, 1), (4, 1)}
        score.value += 2
    except:
        pass


# tests for free_column

def test_Free_Column__Single_Case(score, max_score):
    """Function free_column: single case"""
    max_score.value += 2
    try:
        the_board = Board.make_board(4,
                                     {(2, 4), \
                                      (2, 3),
                                      (1, 2), (2, 2), (4, 2),
                                      (2, 1), (4, 1)})
        Board.free_column(the_board, 2)
        assert Board.get_all_filled_positions(the_board) == \
               {(1, 2), (4, 2), (4, 1)}
        Board.free_column(the_board, 3)
        assert Board.get_all_filled_positions(the_board) == \
               {(1, 2), (4, 2), (4, 1)}
        Board.free_column(the_board, 4)
        assert Board.get_all_filled_positions(the_board) == {(1, 2)}
        score.value += 2
    except:
        pass


# tests for can_be_dropped_at

def test_Can_Be_Dropped_At__True_Case(score, max_score):
    """Function can_be_dropped_at: true case."""
    max_score.value += 12
    try:
        the_board = Board.make_board(4,
                                     {(2, 4), \
                                      (2, 3),
                                      (1, 2), (2, 2), (4, 2),
                                      (2, 1), (4, 1)})
        the_block = Block.make_block({(0, 0), (1, 0), (1, 1)})
        assert Board.can_be_dropped_at(the_board, the_block, (3, 3))
        the_block = Block.make_block({(0, 0), (0, 1), (1, 1)})
        assert Board.can_be_dropped_at(the_board, the_block, (3, 2))
        the_block = Block.make_block({(0, 0)})
        assert Board.can_be_dropped_at(the_board, the_block, (3, 2))
        assert Board.can_be_dropped_at(the_board, the_block, (1, 1))
        the_block = Block.make_block({(0, 0), (-1, 0), (-1, -1), (0, -1)})
        assert Board.can_be_dropped_at(the_board, the_block, (4, 4))
        score.value += 12
    except:
        pass


def test_Can_Be_Dropped_At__Filled_Cells(score, max_score):
    """Function can_be_dropped_at: filled cells."""
    max_score.value += 8
    try:
        the_board = Board.make_board(4,
                                     {(2, 4), \
                                      (2, 3),
                                      (1, 2), (2, 2), (4, 2),
                                      (2, 1), (4, 1)})
        the_block = Block.make_block({(0, 0), (1, 0), (1, 1)})
        assert not Board.can_be_dropped_at(the_board, the_block, (2, 3))
        the_block = Block.make_block({(0, 0), (0, 1), (1, 1)})
        assert not Board.can_be_dropped_at(the_board, the_block, (3, 1))
        the_block = Block.make_block({(0, 0)})
        assert not Board.can_be_dropped_at(the_board, the_block, (2, 4))
        the_block = Block.make_block({(0, 0), (1, 0), (2, 0), (3, 0)})
        assert not Board.can_be_dropped_at(the_board, the_block, (1, 2))
        score.value += 8
    except:
        pass


def test_Can_Be_Dropped_At__Outside_Boundaries(score, max_score):
    """Function can_be_dropped_at: outside boundaries."""
    max_score.value += 3
    try:
        the_block = Block.make_block({(0, 0), (1, 0), (1, 1)})
        the_board = Board.make_board(4,
                                     {(2, 4), \
                                      (2, 3),
                                      (1, 2), (2, 2), (4, 2),
                                      (2, 1), (4, 1)})
        assert not Board.can_be_dropped_at(the_board, the_block, (4, 3))
        score.value += 3
    except:
        pass


def test_Can_Be_Dropped_At__Anchor_Outside_Boundaries(score, max_score):
    """Function can_be_dropped_at: true case with anchor outside boundaries."""
    max_score.value += 10
    try:
        the_block = Block.make_block({(-2, -2), (-2, -1), (-1, -1)})
        the_board = Board.make_board(4,
                                     {(2, 4), \
                                      (2, 3),
                                      (1, 2), (2, 2), (4, 2),
                                      (2, 1), (4, 1)})
        assert Board.can_be_dropped_at(the_board, the_block, (5, 5))
        assert not Board.can_be_dropped_at(the_board, the_block, (5, 3))
        assert not Board.can_be_dropped_at(the_board, the_block, (3, 6))
        score.value += 10
    except:
        pass


# tests for get_droppable_positions

def test_Get_Droppable_Positions__EmptyBoard_Normalized_Block(score, max_score):
    """Function get_droppable_positions: normalized block on empty board."""
    max_score.value += 4
    try:
        the_block = Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)})
        the_board = Board.make_board(4)
        assert Board.get_droppable_positions(the_board, the_block) == \
               [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        score.value += 4
    except:
        pass


def test_Get_Droppable_Positions__EmptyBoard_Non_Normalized_Block(score, max_score):
    """Function get_droppable_positions: non_normalized block on empty board."""
    max_score.value += 8
    try:
        the_block = Block.make_block({(-2, -2), (-2, -1), (-1, -1)})
        the_board = Board.make_board(4)
        assert Board.get_droppable_positions(the_board, the_block) == \
               [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
        the_block = Block.make_block({(-4, 1), (-3, 1), (-2, 1)})
        the_board = Board.make_board(4)
        assert Board.get_droppable_positions(the_board, the_block) == \
               [(5, 0), (5, 1), (5, 2), (5, 3), (6, 0), (6, 1), (6, 2), (6, 3)]
        score.value += 8
    except:
        pass


def test_Get_Droppable_Positions__EmptyBoard_Non_Fitting_Block(score, max_score):
    """Function get_droppable_positions: non fitting block on empty board."""
    max_score.value += 4
    try:
        the_block = Block.make_block({(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)})
        the_board = Board.make_board(4)
        assert Board.get_droppable_positions(the_board, the_block) == []
        score.value += 4
    except:
        pass


def test_Get_Droppable_Positions__NonEmptyBoard_Normalized_Block(score, max_score):
    """Function get_droppable_positions: normalized block on non empty board."""
    max_score.value += 6
    try:
        the_block = Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)})
        the_board = Board.make_board(4, {(1, 1), (2, 2), (3, 3), (4, 4)})
        assert Board.get_droppable_positions(the_board, the_block) == \
               [(1, 3), (3, 1)]
        score.value += 6
    except:
        pass


def test_Get_Droppable_Positions__NonEmptyBoard_Non_Normalized_Block(score, max_score):
    """Function get_droppable_positions: non normalized block on non empty board."""
    max_score.value += 8
    try:
        the_block = Block.make_block({(-2, -2), (-2, -1), (-1, -1)})
        the_board = Board.make_board(4, {(1, 1), (1, 4), (2, 2), (3, 3), (4, 1), (4, 4)})
        assert Board.get_droppable_positions(the_board, the_block) == \
               [(3, 4), (4, 5), (5, 3)]
        score.value += 8
    except:
        pass


def test_Get_Droppable_Positions__NonEmptyBoard_Non_Fitting_Block(score, max_score):
    """Function get_droppable_positions: non_fitting_block on non empty board."""
    max_score.value += 8
    try:
        the_block = Block.make_block({(3, 2), (4, 2), (4, 1)})
        the_board = Board.make_board(4, {(1, 1), (1, 4), (2, 2), (3, 3), (4, 1), (4, 4)})
        assert Board.get_droppable_positions(the_board, the_block) == []
        score.value += 8
    except:
        pass


# tests for drop_at

def test_Drop_at__Normalized_Block(score, max_score):
    """Function drop_at: normalized block."""
    max_score.value += 4
    try:
        the_block = Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)})
        the_board = Board.make_board(4, {(1, 1), (2, 2), (3, 3), (4, 4)})
        orig_filled_positions = Board.get_all_filled_positions(the_board)
        Board.drop_at(the_board, the_block, (1, 3))
        assert Board.get_all_filled_positions(the_board) == \
               orig_filled_positions | {(1, 3), (1, 4), (2, 3), (2, 4)}
        score.value += 4
    except:
        pass


def test_Drop_at__Non_Normalized_Block(score, max_score):
    """Function drop_at: non normalized block."""
    max_score.value += 4
    try:
        the_block = Block.make_block({(-2, -2), (-2, -1), (-1, -1)})
        the_board = Board.make_board(4, {(1, 1), (1, 4), (2, 2), (3, 3), (4, 1), (4, 4)})
        orig_filled_positions = Board.get_all_filled_positions(the_board)
        Board.drop_at(the_board, the_block, (5, 3))
        assert Board.get_all_filled_positions(the_board) == \
               orig_filled_positions | {(3, 1), (3, 2), (4, 2)}
        score.value += 4
    except:
        pass


def test_Drop_at__Non_Fitting_Block(score, max_score):
    """Function drop_at: non_fitting_block."""
    max_score.value += 4
    try:
        the_block = Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)})
        the_board = Board.make_board(3, {(1, 1), (2, 1), (3, 1), (2, 3)})
        orig_filled_positions = Board.get_all_filled_positions(the_board)
        Board.drop_at(the_board, the_block, (1, 3))
        assert Board.get_all_filled_positions(the_board) == \
               orig_filled_positions
        score.value += 4
    except:
        pass


# tests for clear_full_rows_and_columns

def test_Clear_Full_Rows_And_Columns__No_Fulls(score, max_score):
    """Function clear_full_rows_and_columns: no full rows or columns."""
    max_score.value += 3
    try:
        the_board = Board.make_board(4)
        Board.clear_full_rows_and_columns(the_board)
        assert Board.get_all_filled_positions(the_board) == set()
        the_board = Board.make_board(4, \
                                     {(2, 4), (3, 4), \
                                      (2, 3), (4, 3), \
                                      (1, 2), (4, 2), \
                                      (1, 1), (2, 1), (4, 1), \
                                      })
        Board.clear_full_rows_and_columns(the_board)
        assert Board.get_all_filled_positions(the_board) == \
               {(1, 1), (2, 1), (4, 1), (1, 2), (4, 2), (2, 3), (4, 3), (2, 4), (3, 4)}
        score.value += 3
    except:
        pass


def test_Clear_Full_Rows_And_Columns__Only_Full_Columns(score, max_score):
    """Function clear_full_rows_and_columns: only full columns."""
    max_score.value += 4
    try:
        the_board = Board.make_board(4, \
                                     {(2, 4), (3, 4), (4, 4), \
                                      (2, 3), (4, 3), \
                                      (1, 2), (2, 2), (4, 2), \
                                      (1, 1), (2, 1), (4, 1), \
                                      })
        Board.clear_full_rows_and_columns(the_board)
        assert Board.get_all_filled_positions(the_board) == \
               {(1, 1), (1, 2), (3, 4)}
        score.value += 4
    except:
        pass


def test_Clear_Full_Rows_And_Columns__Only_Full_Rows(score, max_score):
    """Function clear_full_rows_and_columns: only full rows."""
    max_score.value += 4
    try:
        the_board = Board.make_board(4, \
                                     {(1, 4), (2, 4), (3, 4), (4, 4), \
                                      (4, 3), \
                                      (1, 2), (2, 2), \
                                      (1, 1), (2, 1), (3, 1), (4, 1), \
                                      })
        Board.clear_full_rows_and_columns(the_board)
        assert Board.get_all_filled_positions(the_board) == \
               {(1, 2), (2, 2), (4, 3)}
        score.value += 4
    except:
        pass


def test_Clear_Full_Rows_And_Columns__Full_Rows_And_Columns(score, max_score):
    """Function clear_full_rows_and_columns: full rows and columns."""
    max_score.value += 8
    try:
        the_board = Board.make_board(4, \
                                     {(1, 4), (2, 4), (3, 4), (4, 4), \
                                      (2, 3), (4, 3), \
                                      (1, 2), (2, 2), (4, 2), \
                                      (1, 1), (2, 1), (3, 1), (4, 1), \
                                      })
        Board.clear_full_rows_and_columns(the_board)
        assert Board.get_all_filled_positions(the_board) == \
               {(1, 2)}
        score.value += 8
    except:
        pass


# tests for are_chainable

def test_Are_Chained__Trivial_Cases(score, max_score):
    """Function are_chainable: trivial cases."""
    max_score.value += 2
    try:
        the_board = Board.make_board(4)
        assert Board.are_chainable(the_board, [])
        assert Board.are_chainable(the_board, ((2, 2),))
        score.value += 2
    except:
        pass


def test_Are_Chained__Adjacent_Positions(score, max_score):
    """Function are_chainable: adjacent_positions."""
    max_score.value += 2
    try:
        the_board = Board.make_board(4, {(2, 2), (2, 1)})
        assert Board.are_chainable(the_board, [(1, 2), (1, 3), (1, 4)])
        assert Board.are_chainable(the_board, {(2, 2), (2, 1)})
        score.value += 2
    except:
        pass


def test_Are_Chained__Non_Adjacent_Chained_Positions(score, max_score):
    """Function are_chainable: non_adjacent chained positions."""
    max_score.value += 10
    try:
        the_board = Board.make_board(4, \
                                     {(2, 4), (3, 4), \
                                      (2, 3), (4, 3), \
                                      (1, 2), (2, 2), (4, 2), \
                                      (1, 1), (2, 1), (4, 1), \
                                      })
        assert Board.are_chainable(the_board, [(1, 2), (3, 4)])
        assert Board.are_chainable(the_board, [(1, 1), (2, 3), (3, 4)])
        assert Board.are_chainable(the_board, {(4, 1), (4, 3)})
        assert Board.are_chainable(the_board, {(3, 1), (3, 3)})
        score.value += 10
    except:
        pass


def test_Are_Chained__Non_Adjacent_Unchained_Positions(score, max_score):
    """Function are_chainable: non_adjacent unchained positions."""
    max_score.value += 10
    try:
        the_board = Board.make_board(4, \
                                     {(3, 4), \
                                      (2, 3), (4, 3), \
                                      (1, 2), (2, 2), (4, 2), \
                                      (1, 1), (2, 1), (4, 1), \
                                      })
        assert not Board.are_chainable(the_board, [(1, 2), (2, 3), (3, 4)])
        assert not Board.are_chainable(the_board, {(1, 1), (4, 1)})
        assert not Board.are_chainable(the_board, {(1, 3), (3, 1)})
        assert not Board.are_chainable(the_board, {(4, 4), (3, 3)})
        score.value += 10
    except:
        pass


board_test_functions = \
    {
        test_Make_Board__No_Filled_Dots,
        test_Make_Board__All_Positions_In_Boundaries,
        test_Make_Board__Some_Positions_Outside_Boundaries,

        test_Copy_Board__Single_Case,

        test_Is_Proper_Board__True_Case,
        test_Is_Proper_Board__False_Cases,

        test_Get_All_Dot_Positions__Hackers_Test1,
        test_Get_All_Dot_Positions__Hackers_Test2,

        test_Is_Filled_At__Outside_Boundaries,

        test_Is_Filled_Row__Invalid_Row,
        test_Is_Filled_Row__Row_Not_Filled,
        test_Is_Filled_Row__Row_Filled,

        test_Is_Filled_Column__Invalid_Column,
        test_Is_Filled_Column__Column_Not_Filled,
        test_Is_Filled_Column__Column_Filled,

        test_Get_All_Filled_Rows__Single_case,

        test_Get_All_Filled_Columns__Single_case,

        test_Fill_Cell__Non_Filled_Position,
        test_Fill_Cell__Filled_Position,
        test_Fill_Cell__Outside_Boundaries,

        test_Fill_All_Cells__Single_Case,

        test_Free_Cell__Non_Filled_Position,
        test_Free_Cell__Filled_Position,
        test_Free_One__Outside_Boundaries,

        test_Free_All_Cells__Single_Case,

        test_Free_Row__Single_Case,

        test_Free_Column__Single_Case,

        test_Can_Be_Dropped_At__True_Case,
        test_Can_Be_Dropped_At__Filled_Cells,
        test_Can_Be_Dropped_At__Outside_Boundaries,
        test_Can_Be_Dropped_At__Anchor_Outside_Boundaries,

        test_Get_Droppable_Positions__EmptyBoard_Normalized_Block,
        test_Get_Droppable_Positions__EmptyBoard_Non_Normalized_Block,
        test_Get_Droppable_Positions__EmptyBoard_Non_Fitting_Block,
        test_Get_Droppable_Positions__NonEmptyBoard_Normalized_Block,
        test_Get_Droppable_Positions__NonEmptyBoard_Non_Normalized_Block,
        test_Get_Droppable_Positions__NonEmptyBoard_Non_Fitting_Block,

        test_Drop_at__Normalized_Block,
        test_Drop_at__Non_Normalized_Block,
        test_Drop_at__Non_Fitting_Block,

        test_Clear_Full_Rows_And_Columns__No_Fulls,
        test_Clear_Full_Rows_And_Columns__Only_Full_Columns,
        test_Clear_Full_Rows_And_Columns__Only_Full_Rows,
        test_Clear_Full_Rows_And_Columns__Full_Rows_And_Columns,

        test_Are_Chained__Trivial_Cases,
        test_Are_Chained__Adjacent_Positions,
        test_Are_Chained__Non_Adjacent_Chained_Positions,
        test_Are_Chained__Non_Adjacent_Unchained_Positions,
    }
