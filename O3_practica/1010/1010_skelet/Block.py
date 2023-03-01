import Position


def make_block(dot_positions):
    """
       Create a new block involving the given mutable set of dot positions.
       ASSUMPTIONS
       - The given set of dot positions is not empty and each of its
         elements is a proper position.
       - The given dot positions are chained together.
    """
    block = set.copy(dot_positions)

    return block


def get_all_dot_positions(block):
    """
        Return a mutable set of all the dot positions of the given block.
        - Dot positions are relative towards the block's anchor.
        ASSUMPTIONS
        - The given block is a proper block.
    """

    return set(block)


def is_proper_block(block):
    """
        Check whether the given block is a proper block.
        - True if and only if the set of dot positions of the given block is not empty,
          if each of its elements is a proper position, and if the dot positions of the
          given block are chained together.
        ASSUMPTIONS:
        - None
    """

    if len(get_all_dot_positions(block)) > 0:
        for pos in block:
            if not Position.is_proper_position(pos):
                return False
        if not Position.are_chained(block):
            return False
        return True
    return False


def add_dot(block, dot_position):
    """
        Add the given dot position to the given block.
        - Nothing happens if the given block already has a dot at the given position, or
          if the given dot cannot be chained with existing dots of the given block.
        ASSUMPTIONS
        - The given block is a proper block.
        - The given position is a proper position.
    """

    if dot_position in block:
        return
    if not Position.is_adjacent_to(dot_position, block):
        return
    block.add(dot_position)


def remove_dot(block, dot_position):
    """
        Remove the given dot position from the given block.
        - Nothing happens if the given dot is not part of the given block, if the
          given block only has the dot to be removed as its single dot, or if the dots
          in the resulting block can no longer be chained.
        ASSUMPTIONS
        - The given block is a proper block.
        - The given position is a proper position.
    """

    temp_block = set.copy(block)

    if dot_position not in block:
        return
    if {dot_position} == block:
        return

    temp_block.remove(dot_position)
    if not Position.are_chained(temp_block):
        return
    block.remove(dot_position)


def get_horizontal_offsets_from_anchor(block):
    """
        Return the horizontal offsets from the anchor of this block.
        - The function returns a tuple involving the smallest horizontal offset
          to the left of the anchor, followed by the largest horizontal offset
          to the right the anchor.
          More formally, if the function returns the tuple (L,R), then for each dot
          position (x,y) of the given block, L <= x <= R
        ASSUMPTIONS
        - The given block is a proper block.
    """
    # for elem in block:
    #     last_left_x = elem[0]
    #     last_right_x = elem[0]
    #     break
    elem = next(iter(block), None)
    last_left_x = last_right_x = Position.col(elem)
    if len(block) == 1:
        return elem
    for pos in block:
        x = Position.col(pos)
        if x < last_left_x:
            last_left_x = x
        if x > last_right_x:
            last_right_x = x

    return (last_left_x, last_right_x)


def get_vertical_offsets_from_anchor(block):
    """
        Return the vertical offsets from the anchor of this block.
        - The function returns a tuple involving the smallest vertical offset
          below the anchor, followed by the largest vertical offset above the anchor.
          More formally, if the function returns the tuple (B,A), then for each dot
          position (x,y) of the given block, B <= y <= A
        ASSUMPTIONS
        - The given block is a proper block.
    """

    elem = next(iter(block), None)
    last_down_y = last_up_y = Position.row(elem)
    if len(block) == 1:
        return elem

    for pos in block:
        y = Position.row(pos)
        if y < last_down_y:
            last_down_y = y
        if y > last_up_y:
            last_up_y = y

    return (last_down_y, last_up_y)


def are_equivalent(block, other_block):
    """
       Check whether the given blocks are equivalent, i.e. cover equivalent
       chains of dots.
       - A block is equivalent with some other block , if there exists a position
         for the anchor of the one block such that the set of dots covered by that
         block relative towards that anchor position, is identical to the set of
         dots covered by the other block.
        ASSUMPTIONS
        - Both given blocks are proper blocks.
    """

    if len(block) != len(other_block):
        return False
    if (len(block) == 1) and (len(other_block) == 1):
        return True

    anchor_1 = min(block)
    anchor_2 = min(other_block)

    shift_x, shift_y = 0, 0
    new_positions = set()

    anchor_1 = list(anchor_1)
    anchor_2 = list(anchor_2)
    while anchor_1 != anchor_2:
        if Position.col(anchor_1) < Position.col(anchor_2):
            anchor_1[0] += 1
            shift_x += 1
        if Position.col(anchor_1) > Position.col(anchor_2):
            anchor_1[0] -= 1
            shift_x -= 1
        if Position.row(anchor_1) < Position.row(anchor_2):
            anchor_1[1] += 1
            shift_y += 1
        if Position.row(anchor_1) > Position.row(anchor_2):
            anchor_1[1] -= 1
            shift_y -= 1

    for pos in block:
        new_pos = (Position.col(pos) + shift_x), (Position.row(pos) + shift_y)
        new_positions.add(new_pos)
    new_block = make_block(new_positions)

    if not new_block == other_block:
        return False
    return True


def is_normalized(block):
    """
       Check whether the given block is normalized.
       - True if and only if the anchor of the given block is one of the dot positions
         of that block.
       ASSUMPTIONS
       - The given block is a proper block.
    """
    positions = get_all_dot_positions(block)
    if (0, 0) in positions:
        return True
    return False


def normalize(block):
    """
       Return a new block that is a normalized version of the given block.
       - The resulting block must be equivalent with the given block.
       - The function is free to choose a proper anchor for the normalized
         block.
       ASSUMPTIONS
       - The given block is a proper block.
    """
    positions = get_all_dot_positions(block)
    new_positions = set()
    new_anchor = min(positions)
    delta_x = Position.col(new_anchor)
    delta_y = Position.row(new_anchor)

    for pos in positions:
        new_pos = Position.translate_over(pos, -delta_x, -delta_y)
        new_positions.add(new_pos)
    return make_block(new_positions)


def print_block(block):
    """
        Print the given block on the standard output stream.
        - The anchor of the given block will be revealed in the print-out.
        ASSUMPTIONS
        - The given block is a proper block.
    """
    horizontal_offsets = get_horizontal_offsets_from_anchor(block)
    width = max(horizontal_offsets[1], 0) - min(horizontal_offsets[0], 0) + 1
    vertical_offsets = get_vertical_offsets_from_anchor(block)
    height = max(vertical_offsets[1], 0) - min(vertical_offsets[0], 0) + 1
    printout = [[" " for column in range(1, width + 1)]
                for row in range(1, height + 1)]
    dot_positions = get_all_dot_positions(block)
    for (column, row) in dot_positions:
        printout[row - min(vertical_offsets[0], 0)] \
            [column - min(horizontal_offsets[0], 0)] = "\u25A9"
    if (0, 0) in dot_positions:
        anchor_symbol = "\u25A3"
    else:
        anchor_symbol = "\u25A2"
    printout[-min(vertical_offsets[0], 0)][-min(horizontal_offsets[0], 0)] = anchor_symbol
    for row in range(len(printout) - 1, -1, -1):
        for col in range(0, len(printout[0])):
            print(printout[row][col], end = " ")
        print()


# collection of standard blocks used to play the game.


standard_blocks = \
    (  # Single dot
            make_block({(0, 0)}),
            # Horizontal line of length 2
            make_block({(0, 0), (1, 0)}),
            # Horizontal line of length 3
            make_block({(-1, 0), (0, 0), (1, 0)}),
            # Horizontal line of length 4
            make_block({(-3, 0), (-2, 0), (-1, 0), (0, 0)}),
            # Horizontal line of length 5
            make_block({(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)}),
            # Vertical line of length 2
            make_block({(0, 0), (0, 1)}),
            # Vertical line of length 3
            make_block({(0, -1), (0, 0), (0, 1)}),
            # Vertical line of length 4
            make_block({(-2, 2), (-2, 3), (-2, 4), (-2, 5)}),
            # Vertical line of length 5
            make_block({(0, -6), (0, -5), (0, -4), (0, -3), (0, -2)}),
            # T-squares 1x1
            make_block({(-1, 0), (0, 0), (0, 1)}),
            make_block({(0, 0), (0, 1), (1, 0)}),
            make_block({(0, 0), (0, -1), (1, 0)}),
            make_block({(-1, 0), (0, 0), (0, -1)}),
            # T-squares 2x2
            make_block({(-2, 0), (-1, 0), (0, 0), (0, 1), (0, 2)}),
            make_block({(0, 2), (1, 2), (2, 2), (2, 1), (2, 0)}),
            make_block({(2, 0), (1, 0), (0, 0), (0, -1), (0, -2)}),
            make_block({(-2, -2), (-1, -2), (0, -2), (-2, -1), (-2, 0)}),
            # Square block 2x2
            make_block({(0, 0), (1, 0), (0, 1), (1, 1)}),
            # Square block 3x3
            make_block({(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)}),
            )


def select_standard_block():
    """
        Return one of the standard blocks.
        - The resulting block is selected randomly.
    """
    import random
    return random.choice(standard_blocks)
