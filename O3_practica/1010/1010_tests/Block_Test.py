import Block


# tests for make_block

def test_Make_Block__Regular_Case(score, max_score):
    """Function make_block: regular case."""
    max_score.value += 2
    try:
        given_dot_positions = {(0, 0), (1, 0), (0, 1), (1, 1)}
        the_block = Block.make_block(given_dot_positions)
        assert Block.get_all_dot_positions(the_block) == given_dot_positions
        score.value += 2
    except:
        pass


def test_Make_Block__Hackers_Test1(score, max_score):
    """Function make_block: hacker's test 1."""
    max_score.value += 10
    try:
        dot_positions = {(0, 0), (1, 0), (0, 1), (1, 1)}
        the_block = Block.make_block(dot_positions)
        set.add(dot_positions, "hacker")
        assert Block.is_proper_block(the_block)
        score.value += 10
    except:
        pass


def test_Make_Block__Hackers_Test2(score, max_score):
    """Function make_block: hacker's test 2."""
    max_score.value += 10
    try:
        given_dot_positions = {(0, 0), (1, 0), (0, 1), (1, 1)}
        the_block = Block.make_block(given_dot_positions)
        block_dot_positions = Block.get_all_dot_positions(the_block)
        set.add(block_dot_positions, "hacker")
        assert Block.is_proper_block(the_block)
        score.value += 10
    except:
        pass


# tests for is_proper_block

def test_Is_Proper_Block__True_Case(score, max_score):
    """Function is_proper_block: true case."""
    max_score.value += 4
    try:
        dot_positions = {(0, 0), (1, 0), (0, 1), (1, 1)}
        the_block = Block.make_block(dot_positions)
        assert Block.is_proper_block(the_block)
        score.value += 4
    except:
        pass


def test_Is_Proper_Block__False_Case(score, max_score):
    """Function is_proper_block: false case."""
    max_score.value += 2
    try:
        assert not Block.is_proper_block("ku leuven")
        assert not Block.is_proper_block((0, 0))
        score.value += 2
    except:
        pass


# tests for add_dot

def test_Add_Dot__Legal_Dot(score, max_score):
    """Function add_dot: legal dot."""
    max_score.value += 4
    try:
        dot_positions = {(0, 0), (1, 0), (0, 1), (1, 1)}
        the_block = Block.make_block(dot_positions)
        Block.add_dot(the_block, (2, 0))
        Block.add_dot(the_block, (3, 0))
        Block.add_dot(the_block, (0, -1))
        assert Block.get_all_dot_positions(the_block) == \
               dot_positions | {(2, 0), (3, 0), (0, -1)}
        score.value += 4
    except:
        pass


def test_Add_Dot__Existing_Dot(score, max_score):
    """Function add_dot: existing dot."""
    max_score.value += 1
    try:
        dot_positions = {(0, 0), (1, 0), (0, 1), (1, 1)}
        the_block = Block.make_block(dot_positions)
        Block.add_dot(the_block, (0, 0))
        Block.add_dot(the_block, (1, 1))
        assert Block.get_all_dot_positions(the_block) == dot_positions
        score.value += 1
    except:
        pass


def test_Add_Dot__Non_Chaining_Dot(score, max_score):
    """Function add_dot: non chaining dot."""
    max_score.value += 6
    try:
        dot_positions = {(0, 0), (1, 0), (0, 1), (1, 1)}
        the_block = Block.make_block(dot_positions)
        Block.add_dot(the_block, (3, 3))
        Block.add_dot(the_block, (-1, -1))
        assert Block.get_all_dot_positions(the_block) == dot_positions
        score.value += 6
    except:
        pass


# tests for remove_dot

def test_Remove_Dot__Legal_Dot(score, max_score):
    """Function remove_dot: legal dot."""
    max_score.value += 4
    try:
        dot_positions = {(0, 0), (1, 0), (0, 1), (1, 1)}
        the_block = Block.make_block(dot_positions)
        Block.remove_dot(the_block, (1, 0))
        Block.remove_dot(the_block, (1, 1))
        Block.remove_dot(the_block, (0, 0))
        assert Block.get_all_dot_positions(the_block) == {(0, 1)}
        score.value += 4
    except:
        pass


def test_Remove_Dot__Non_Existing_Dot(score, max_score):
    """Function remove_dot: non_existing dot."""
    max_score.value += 1
    try:
        dot_positions = {(0, 0), (1, 0), (0, 1), (1, 1)}
        the_block = Block.make_block(dot_positions)
        Block.remove_dot(the_block, (2, 0))
        Block.remove_dot(the_block, (1, 2))
        Block.remove_dot(the_block, (-1, -1))
        assert Block.get_all_dot_positions(the_block) == dot_positions
        score.value += 1
    except:
        pass


def test_Remove_Dot__Singleton_Block(score, max_score):
    """Function remove_dot: singleton block."""
    max_score.value += 2
    try:
        dot_positions = {(1, 1)}
        the_block = Block.make_block(dot_positions)
        Block.remove_dot(the_block, (1, 1))
        assert Block.get_all_dot_positions(the_block) == dot_positions
        score.value += 2
    except:
        pass


def test_Remove_Dot__Chaining_Lost(score, max_score):
    """Function remove_dot: chaining_lost."""
    max_score.value += 6
    try:
        dot_positions = {(0, 0), (1, 0), (0, 1), (1, 1)}
        the_block = Block.make_block(dot_positions)
        Block.remove_dot(the_block, (0, 0))
        Block.remove_dot(the_block, (1, 1))
        assert Block.get_all_dot_positions(the_block) == dot_positions - {(0, 0)}
        score.value += 6
    except:
        pass


# tests for get_horizontal_offsets_from_anchor

def test_Get_Horizontal_Offsets_From_Anchor__Single_Case(score, max_score):
    """Function get_horizontal_offsets_from_anchor: single case."""
    max_score.value += 3
    try:
        the_block = Block.make_block({(0, 0)})
        assert Block.get_horizontal_offsets_from_anchor(the_block) == (0, 0)
        the_block = Block.make_block({(-1, 0), (0, 0), (1, 0), (2, 0), (1, 1)})
        assert Block.get_horizontal_offsets_from_anchor(the_block) == (-1, 2)
        the_block = Block.make_block({(3, 0), (4, 0), (4, 1)})
        assert Block.get_horizontal_offsets_from_anchor(the_block) == (3, 4)
        score.value += 3
    except:
        pass


# tests for get_vertical_offsets_from_anchor

def test_Get_Vertical_Offsets_From_Anchor__Single_Case(score, max_score):
    """Function get_vertical_offsets_from_anchor: single case."""
    max_score.value += 3
    try:
        the_block = Block.make_block({(0, 0)})
        assert Block.get_vertical_offsets_from_anchor(the_block) == (0, 0)
        the_block = Block.make_block({(0, -1), (0, 0), (0, 1), (0, 2), (1, 1)})
        assert Block.get_vertical_offsets_from_anchor(the_block) == (-1, 2)
        the_block = Block.make_block({(0, 3), (0, 4), (1, 4)})
        assert Block.get_vertical_offsets_from_anchor(the_block) == (3, 4)
        score.value += 3
    except:
        pass


# tests for are_equivalent

def test_Are_Equivalent__True_Cases(score, max_score):
    """Function are_equivalent: true cases."""
    max_score.value += 6
    try:
        # single dot blocks
        the_block = Block.make_block({(0, 0)})
        other_block = Block.make_block({(1, 3)})
        assert Block.are_equivalent(the_block, other_block)
        # one-dimensional blocks
        the_block = Block.make_block({(-2, 2), (-2, 3), (-2, 4), (-2, 5)})
        other_block = Block.make_block({(0, 0), (0, 1), (0, 2), (0, 3)})
        assert Block.are_equivalent(the_block, other_block)
        #two-dimensional blocks
        the_block = Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)})
        other_block = Block.make_block({(-2, 3), (-1, 3), (-2, 4), (-1, 4)})
        assert Block.are_equivalent(the_block, other_block)
        score.value += 6
    except:
        pass


def test_Are_Equivalent__False_Cases(score, max_score):
    """Function are_equivalent: false cases."""
    max_score.value += 6
    try:
        # blocks with different number of dots.
        the_block = Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)})
        other_block = Block.make_block({(-2, 3), (-1, 3), (-2, 4), (-1, 4), (-1, 5)})
        assert not Block.are_equivalent(the_block, other_block)
        # blocks with same number of dots
        the_block = Block.make_block({(-2, 2), (-2, 3), (-2, 4), (-2, 5)})
        other_block = Block.make_block({(0, 0), (0, 1), (0, 2), (1,2)})
        assert not Block.are_equivalent(the_block, other_block)
        score.value += 6
    except:
        pass


# tests for is_normalized

def test_Is_Normalized__True_Cases(score, max_score):
    """Function is_normalized: true cases."""
    max_score.value += 2
    try:
        the_block = Block.make_block({(0, 0)})
        assert Block.is_normalized(the_block)
        the_block = Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)})
        assert Block.is_normalized(the_block)
        score.value += 2
    except:
        pass


def test_Is_Normalized__False_Cases(score, max_score):
    """Function is_normalized: false cases."""
    max_score.value += 2
    try:
        the_block = Block.make_block({(-2, 3), (-1, 3), (-2, 4), (-1, 4), (-1, 5)})
        assert not Block.is_normalized(the_block)
        the_block = Block.make_block({(-2, 2), (-2, 3), (-2, 4), (-2, 5)})
        assert not Block.is_normalized(the_block)
        the_block = Block.make_block({(2, -2), (2, -3), (2, -4), (2, -5)})
        assert not Block.is_normalized(the_block)
        score.value += 2
    except:
        pass


# tests for normalize

def test_Normalize__Already_Normalized(score, max_score):
    """Function normalize: block already normalized."""
    max_score.value += 2
    try:
        the_block = Block.make_block({(0, 0), (1, 0), (0, 1), (1, 1)})
        normalized_block = Block.normalize(the_block)
        assert Block.is_normalized(normalized_block)
        assert Block.are_equivalent(the_block, normalized_block)
        score.value += 2
    except:
        pass


def test_Normalize__Not_Yet_Normalized(score, max_score):
    """Function normalize: block not yet normalized."""
    max_score.value += 6
    try:
        the_block = Block.make_block({(-2, -1), (-1, -1), (-2, 0), (-1, 0), (-1, 1)})
        normalized_block = Block.normalize(the_block)
        assert Block.is_normalized(normalized_block)
        assert Block.are_equivalent(the_block, normalized_block)
        the_block = Block.make_block({(-1, 3), (0, 3), (-1, 4), (0, 4), (0, 5)})
        normalized_block = Block.normalize(the_block)
        assert Block.is_normalized(normalized_block)
        assert Block.are_equivalent(the_block, normalized_block)
        the_block = Block.make_block({(-2, 3), (-1, 3), (-2, 4), (-1, 4), (-1, 5)})
        normalized_block = Block.normalize(the_block)
        assert Block.is_normalized(normalized_block)
        assert Block.are_equivalent(the_block, normalized_block)
        score.value += 6
    except:
        pass

def test_Normalize__Standard_Blocks(score, max_score):
    """Function normalize: standard blocks."""
    max_score.value += 10
    try:
        for block in Block.standard_blocks:
            assert Block.is_normalized(Block.normalize(block))
        score.value += 10
    except:
        pass

# collection of block test functions

block_test_functions = \
    {
        test_Make_Block__Regular_Case,
        test_Make_Block__Hackers_Test1,
        test_Make_Block__Hackers_Test2,

        test_Is_Proper_Block__True_Case,
        test_Is_Proper_Block__False_Case,

        test_Add_Dot__Legal_Dot,
        test_Add_Dot__Existing_Dot,
        test_Add_Dot__Non_Chaining_Dot,

        test_Remove_Dot__Legal_Dot,
        test_Remove_Dot__Non_Existing_Dot,
        test_Remove_Dot__Singleton_Block,
        test_Remove_Dot__Chaining_Lost,

        test_Get_Horizontal_Offsets_From_Anchor__Single_Case,

        test_Get_Vertical_Offsets_From_Anchor__Single_Case,

        test_Are_Equivalent__True_Cases,
        test_Are_Equivalent__False_Cases,

        test_Is_Normalized__True_Cases,
        test_Is_Normalized__False_Cases,

        test_Normalize__Already_Normalized,
        test_Normalize__Not_Yet_Normalized,
    }
