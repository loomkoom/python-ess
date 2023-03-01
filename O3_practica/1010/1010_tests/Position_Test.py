import Position


# Tests for is_proper_position

def test_Is_Proper_Position__Legal_Case(score, max_score):
    """Function is_proper_position: given position is proper position."""
    max_score.value += 1
    try:
        assert Position.is_proper_position((1, 1))
        assert Position.is_proper_position((0, 0))
        assert Position.is_proper_position((-3, -7))
        score.value += 1
    except:
        pass


def test_Is_Proper_Position__Not_Tuple(score, max_score):
    """Function is_proper_position: given position is not a tuple."""
    max_score.value += 1
    try:
        assert not Position.is_proper_position([1, 2])
        score.value += 1
    except:
        pass


def test_Is_Proper_Position__Improper_Length(score, max_score):
    """Function is_proper_position: given position is a tuple of length different from 2."""
    max_score.value += 1
    try:
        assert not Position.is_proper_position((1,))
        assert not Position.is_proper_position((1, 2, 3))
        score.value += 1
    except:
        pass


def test_Is_Proper_Position__Improper_First_Element(score, max_score):
    """Function is_proper_position: given position is a tuple of length 2 with non-integer as first element."""
    max_score.value += 1
    try:
        assert not Position.is_proper_position((3.14, 3))
        assert not Position.is_proper_position(((1,), 3))
        score.value += 1
    except:
        pass


def test_Is_Proper_Position__Improper_Second_Element(score, max_score):
    """Function is_proper_position: given position is a tuple of length 2 with non-integer as second element."""
    max_score.value += 1
    try:
        assert not Position.is_proper_position((3, "abc"))
        assert not Position.is_proper_position((3, [1]))
        score.value += 1
    except:
        pass


# Tests for is_proper_position_for_board

def test_Is_Proper_Position_For_Board__Legal_Case(score, max_score):
    """Function is_proper_position_for_board: given position is a proper position for a board with given dimension."""
    max_score.value += 1
    try:
        assert Position.is_proper_position_for_board(3, (1, 1))
        assert Position.is_proper_position_for_board(5, (5, 5))
        assert Position.is_proper_position_for_board(10, (4, 7))
        score.value += 1
    except:
        pass


def test_Is_Proper_Position_For_Board__Improper_Position(score, max_score):
    """Function is_proper_position_for_board: given position is not a proper position."""
    max_score.value += 1
    try:
        assert not Position.is_proper_position_for_board(3, (1, 2, 3))
        score.value += 1
    except:
        pass


def test_Is_Proper_Position_For_Board__Improper_Dimension(score, max_score):
    """Function is_proper_position_for_board: given dimension is not a positive integer number."""
    max_score.value += 1
    try:
        assert not Position.is_proper_position_for_board(3.14, (1, 2))
        assert not Position.is_proper_position_for_board(-4, (1, 2))
        score.value += 1
    except:
        pass


def test_Is_Proper_Position_For_Board__Position_Out_Of_Bounds(score, max_score):
    """Function is_proper_position_for_board: given position is outside the boundaries of a board with the given dimension."""
    max_score.value += 1
    try:
        assert not Position.is_proper_position_for_board(3, (0, 1))
        assert not Position.is_proper_position_for_board(5, (2, 6))
        assert not Position.is_proper_position_for_board(7, (-1, 10))
        score.value += 1
    except:
        pass


# Tests for left

def test_Left__Not_Leftmost_Position(score, max_score):
    """Function left: non-leftmost position"""
    max_score.value += 1
    try:
        assert Position.left(8, (2, 4)) == (1, 4)
        score.value += 1
    except:
        pass


def test_Left__Leftmost_Position(score, max_score):
    """Function left: leftmost position"""
    max_score.value += 1
    try:
        assert Position.left(8, (1, 6)) == None
        score.value += 1
    except:
        pass


# Tests for right

def test_Right__Not_Rightmost_Position(score, max_score):
    """Function right: non-rightmost position"""
    max_score.value += 1
    try:
        assert Position.right(8, (7, 4)) == (8, 4)
        score.value += 1
    except:
        pass


def test_Right__Rightmost_Position(score, max_score):
    """Function right: rightmost position"""
    max_score.value += 1
    try:
        assert Position.right(8, (8, 6)) == None
        score.value += 1
    except:
        pass


# Tests for up

def test_Up__Not_Upmost_Position(score, max_score):
    """Function up: non-upmost position"""
    max_score.value += 1
    try:
        assert Position.up(8, (2, 7)) == (2, 8)
        score.value += 1
    except:
        pass


def test_Up__Upmost_Position(score, max_score):
    """Function up: upmost position"""
    max_score.value += 1
    try:
        assert Position.up(8, (2, 8)) == None
        score.value += 1
    except:
        pass


# Tests for down

def test_Down__Not_Bottom_Position(score, max_score):
    """Function down: not bottom position"""
    max_score.value += 1
    try:
        assert Position.down(8, (4, 2)) == (4, 1)
        score.value += 1
    except:
        pass


def test_Down__Bottom_Position(score, max_score):
    """Function down: bottom position"""
    max_score.value += 1
    try:
        assert Position.down(8, (2, 1)) == None
        score.value += 1
    except:
        pass


# Tests for next

def test_Next__Not_End_Row(score, max_score):
    """Function next: position not at end of row"""
    max_score.value += 1
    try:
        assert Position.next(4, (3, 1)) == (4, 1)
        assert Position.next(4, (1, 4)) == (2, 4)
        score.value += 1
    except:
        pass


def test_Next__End_Non_Top_Row(score, max_score):
    """Function next: position at end of row that is not top row"""
    max_score.value += 1
    try:
        assert Position.next(4, (4, 1)) == (1, 2)
        assert Position.next(4, (4, 3)) == (1, 4)
        score.value += 1
    except:
        pass


def test_Next__End_Top_Row(score, max_score):
    """Function next: position at end of top row"""
    max_score.value += 1
    try:
        assert Position.next(4, (4, 4)) == None
        score.value += 1
    except:
        pass


# Tests for translate_over

def test_Translate_Over__Single_Case(score, max_score):
    """Function translate_over: single case."""
    max_score.value += 1
    try:
        assert Position.translate_over((3, 6), 2, -3) == (5, 3)
        assert Position.translate_over((-2, -7), -1, 3) == (-3, -4)
        assert Position.translate_over((3, 6), 0, 0) == (3, 6)
        score.value += 1
    except:
        pass


# Tests for get_adjacent_positions

def test_Get_Adjacent_Positions__No_Edge_Position(score, max_score):
    """Function get_adjacent_positions: no edge position"""
    max_score.value += 2
    try:
        adjacent_positions = Position.get_adjacent_positions((2, 3), 8)
        assert isinstance(adjacent_positions, set)
        assert adjacent_positions == {(1, 3), (2, 2), (2, 4), (3, 3)}
        score.value += 2
    except:
        pass


def test_Get_Adjacent_Positions__No_Boundaries(score, max_score):
    """Function get_adjacent_positions: no boundaries"""
    max_score.value += 2
    try:
        adjacent_positions = Position.get_adjacent_positions((-2, -6))
        assert adjacent_positions == {(-3, -6), (-2, -7), (-1, -6), (-2, -5)}
        score.value += 2
    except:
        pass


def test_Get_Adjacent_Positions__Edge_Positions(score, max_score):
    """Function get_adjacent_positions: edge positions"""
    max_score.value += 2
    try:
        adjacent_positions = Position.get_adjacent_positions((1, 3), 8)
        assert adjacent_positions == {(1, 4), (1, 2), (2, 3)}
        adjacent_positions = Position.get_adjacent_positions((8, 3), 8)
        assert adjacent_positions == {(8, 4), (8, 2), (7, 3)}
        adjacent_positions = Position.get_adjacent_positions((3, 1), 8)
        assert adjacent_positions == {(2, 1), (4, 1), (3, 2)}
        adjacent_positions = Position.get_adjacent_positions((3, 8), 8)
        assert adjacent_positions == {(2, 8), (4, 8), (3, 7)}
        score.value += 2
    except:
        pass


def test_Get_Adjacent_Positions__Corner_Positions(score, max_score):
    """Function get_adjacent_positions: corner positions"""
    max_score.value += 2
    try:
        adjacent_positions = Position.get_adjacent_positions((1, 1), 8)
        assert adjacent_positions == {(1, 2), (2, 1)}
        adjacent_positions = Position.get_adjacent_positions((1, 8), 8)
        assert adjacent_positions == {(1, 7), (2, 8)}
        adjacent_positions = Position.get_adjacent_positions((8, 1), 8)
        assert adjacent_positions == {(7, 1), (8, 2)}
        adjacent_positions = Position.get_adjacent_positions((8, 8), 8)
        assert adjacent_positions == {(7, 8), (8, 7)}
        score.value += 2
    except:
        pass


# Tests for is_adjacent_to

def test_Is_Adjacent_To__True_Case(score, max_score):
    """Function is_adjacent_to: true case"""
    max_score.value += 2
    try:
        assert Position.is_adjacent_to((1, 1), [(1, 2), (2, 1), (0, 0)])
        assert Position.is_adjacent_to((1, 1), ((1, 2), (-4, 3), (6, 9)))
        score.value += 2
    except:
        pass


def test_Is_Adjacent_To__False_Case(score, max_score):
    """Function is_adjacent_to: false case"""
    max_score.value += 2
    try:
        assert not Position.is_adjacent_to((1, 1), set())
        assert not Position.is_adjacent_to((1, 1), ((1, 3),))
        assert not Position.is_adjacent_to((1, 1), frozenset({(3, 2), (2, -1), (-10, 10), (-1, 1)}))
        score.value += 2
    except:
        pass


# Tests for get_surrounding_positions

def test_Get_Surrounding_Positions__No_Edge_Position(score, max_score):
    """Function get_surrounding_positions: no edge position"""
    max_score.value += 2
    try:
        surrounding_positions = Position.get_surrounding_positions((2, 3), 8)
        assert isinstance(surrounding_positions,set)
        assert surrounding_positions == \
               {(1, 3), (1, 4), (1, 2), (2, 2), (2, 4), (3, 3), (3, 2), (3, 4)}
        score.value += 2
    except:
        pass


def test_Get_Surrounding_Positions__No_Boundaries(score, max_score):
    """Function get_surrounding_positions: no boundaries"""
    max_score.value += 2
    try:
        surrounding_positions = Position.get_surrounding_positions((-2, -6))
        assert surrounding_positions == \
               {(-3, -6), (-3, -7), (-3, -5), (-2, -5), (-2, -7), (-1, -6), (-1, -7), (-1, -5)}
        score.value += 2
    except:
        pass


def test_Get_Surrounding_Positions__Edge_Positions(score, max_score):
    """Function get_surrounding_positions: edge positions"""
    max_score.value += 2
    try:
        surrounding_positions = Position.get_surrounding_positions((1, 3), 8)
        assert surrounding_positions == \
               {(1, 2), (1, 4), (2, 3), (2, 2), (2, 4)}
        surrounding_positions = Position.get_surrounding_positions((8, 3), 8)
        assert surrounding_positions == \
               {(8, 2), (8, 4), (7, 3), (7, 2), (7, 4)}
        surrounding_positions = Position.get_surrounding_positions((3, 1), 8)
        assert surrounding_positions == \
               {(2, 1), (4, 1), (2, 2), (3, 2), (4, 2)}
        surrounding_positions = Position.get_surrounding_positions((3, 8), 8)
        assert surrounding_positions == \
               {(2, 8), (4, 8), (2, 7), (3, 7), (4, 7)}
        score.value += 2
    except:
        pass


def test_Get_Surrounding_Positions__Corner_Positions(score, max_score):
    """Function get_surrounding_positions: corner positions"""
    max_score.value += 2
    try:
        surrounding_positions = Position.get_surrounding_positions((1, 1), 8)
        assert surrounding_positions == {(1, 2), (2, 2), (2, 1)}
        surrounding_positions = Position.get_surrounding_positions((1, 8), 8)
        assert surrounding_positions == {(1, 7), (2, 7), (2, 8)}
        surrounding_positions = Position.get_surrounding_positions((8, 1), 8)
        assert surrounding_positions == {(7, 1), (7, 2), (8, 2)}
        surrounding_positions = Position.get_surrounding_positions((8, 8), 8)
        assert surrounding_positions == {(7, 8), (7, 7), (8, 7)}
        score.value += 2
    except:
        pass


# Tests for are_chained (iterative version)

def test_Are_Chained__Empty_Collection(score, max_score):
    """Function are_chained: empty collection"""
    max_score.value += 1
    try:
        assert Position.are_chained([])
        score.value += 1
    except:
        pass


def test_Are_Chained__Singleton_Collection(score, max_score):
    """Function are_chained: singleton collection"""
    max_score.value += 1
    try:
        assert Position.are_chained([(1, 3)])
        score.value += 1
    except:
        pass


def test_Are_Chained__True_Case(score, max_score):
    """Function are_chained: true case"""
    max_score.value += 10
    try:
        assert Position.are_chained\
            ([(0, 3), (0, 1), (1, -1), (0, 2), (-1, 1), (0, 0), (1, 3), \
              (1, 0), (-1, 2)])
        score.value += 10
    except:
        pass


def test_Are_Chained__False_Case(score, max_score):
    """Function are_chained: false case"""
    max_score.value += 6
    try:
        assert not Position.are_chained\
            ([(0, 3), (0, 1), (1, -1), (-1, 1), (0, 0), (1, 3), (1, 0)])
        score.value += 6
    except:
        pass


def test_Are_Chained__Duplicate_Positions(score, max_score):
    """Function are_chained: duplicate positions"""
    max_score.value += 3
    try:
        assert Position.are_chained\
            (((-1,-2),(-1,-2),(0,-2),(-1,-2),(0,-2)))
        score.value += 3
    except:
        pass


def test_Are_Chained__Touching_Positions(score, max_score):
    """Function are_chained: touching positions"""
    max_score.value += 6
    try:
        assert not Position.are_chained\
            ([(0, 3), (0, 1), (1, -1), (0, 0), (1, 3), (1, 0), (-1, 2)])
        score.value += 6
    except:
        pass


# Tests for are_chained (recursive version)

def test_Are_Chained_Rec__Empty_Collection(score, max_score):
    """Function are_chained_rec: empty collection"""
    max_score.value += 1
    try:
        assert Position.are_chained_rec([])
        score.value += 1
    except:
        pass


def test_Are_Chained_Rec__Singleton_Collection(score, max_score):
    """Function are_chained_rec: singleton collection"""
    max_score.value += 1
    try:
        assert Position.are_chained_rec([(1, 3)])
        score.value += 1
    except:
        pass


def test_Are_Chained_Rec__True_Case(score, max_score):
    """Function are_chained_rec: true case"""
    max_score.value += 15
    try:
        assert Position.are_chained_rec\
            ([(0, 3), (0, 1), (1, -1), (0, 2), (-1, 1), (0, 0), (1, 3), \
              (1, 0), (-1, 2)])
        score.value += 15
    except:
        pass


def test_Are_Chained_Rec__False_Case(score, max_score):
    """Function are_chained_rec: false case"""
    max_score.value += 9
    try:
        assert not Position.are_chained_rec([(0, 3), (0, 1), (1, -1), (-1, 1), (0, 0), (1, 3), (1, 0)])
        score.value += 9
    except:
        pass


def test_Are_Chained_Rec__Duplicate_Positions(score, max_score):
    """Function are_chained: duplicate positions"""
    max_score.value += 5
    try:
        assert Position.are_chained_rec\
            (((-1,-2),(-1,-2),(0,-2),(-1,-2),(0,-2)))
        score.value += 5
    except:
        pass

def test_Are_Chained_Rec__Touching_Positions(score, max_score):
    """Function are_chained_rec: touching positions"""
    max_score.value += 9
    try:
        assert not Position.are_chained_rec\
            ([(0, 3), (0, 1), (1, -1), (0, 0), (1, 3), (1, 0), (-1, 2)])
        score.value += 9
    except:
        pass


# collection of position test functions

position_test_functions = \
    {
        test_Is_Proper_Position__Legal_Case,
        test_Is_Proper_Position__Not_Tuple,
        test_Is_Proper_Position__Improper_Length,
        test_Is_Proper_Position__Improper_First_Element,
        test_Is_Proper_Position__Improper_Second_Element,
        test_Is_Proper_Position_For_Board__Legal_Case,
        test_Is_Proper_Position_For_Board__Improper_Dimension,
        test_Is_Proper_Position_For_Board__Improper_Position,
        test_Is_Proper_Position_For_Board__Position_Out_Of_Bounds,

        test_Left__Not_Leftmost_Position,
        test_Left__Leftmost_Position,

        test_Right__Rightmost_Position,
        test_Right__Not_Rightmost_Position,

        test_Up__Not_Upmost_Position,
        test_Up__Upmost_Position,

        test_Down__Not_Bottom_Position,
        test_Down__Bottom_Position,

        test_Next__Not_End_Row,
        test_Next__End_Non_Top_Row,
        test_Next__End_Top_Row,

        test_Translate_Over__Single_Case,

        test_Get_Adjacent_Positions__No_Edge_Position,
        test_Get_Adjacent_Positions__No_Boundaries,
        test_Get_Adjacent_Positions__Edge_Positions,
        test_Get_Adjacent_Positions__Corner_Positions,

        test_Is_Adjacent_To__True_Case,
        test_Is_Adjacent_To__False_Case,

        test_Get_Surrounding_Positions__No_Edge_Position,
        test_Get_Surrounding_Positions__No_Boundaries,
        test_Get_Surrounding_Positions__Edge_Positions,
        test_Get_Surrounding_Positions__Corner_Positions,

        test_Are_Chained__Empty_Collection,
        test_Are_Chained__Singleton_Collection,
        test_Are_Chained__True_Case,
        test_Are_Chained__False_Case,
        test_Are_Chained__Duplicate_Positions,
        test_Are_Chained__Touching_Positions,

        test_Are_Chained_Rec__Empty_Collection,
        test_Are_Chained_Rec__Singleton_Collection,
        test_Are_Chained_Rec__True_Case,
        test_Are_Chained_Rec__False_Case,
        test_Are_Chained_Rec__Duplicate_Positions,
        test_Are_Chained_Rec__Touching_Positions,
    }
