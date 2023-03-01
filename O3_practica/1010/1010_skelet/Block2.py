import Position


def make_block(dot_positions):
    """
       Create a new block involving the given mutable set of dot positions.
       ASSUMPTIONS
       - The given set of dot positions is not empty and each of its
         elements is a proper position.
       - The given dot positions are chained together.
    """


    range_x = (min(dot_positions)[0], max(dot_positions)[0])
    range_y = (min(dot_positions)[1], max(dot_positions)[1])

    #print(range_x, range_y)
    dimension_x = (range_x[1] - range_x[0]) + 1
    dimension_y = (range_y[1] - range_y[0]) + 1
    #print(dimension_x, dimension_y)
    block_matrix = [[0 for a in range(0, dimension_x)] for b in range(0, dimension_y)]
    #print(block_matrix)
    for pos in dot_positions:
        for j in range(len(block_matrix)):
            for k in range(len(block_matrix[0])):
                if j == pos[0] and k == pos[1]:
                    block_matrix[j][k] = 1

    return block_matrix

the_block = make_block({(0,0),(1,0),(-1,1)})
print(the_block)



def get_all_dot_positions(block):
    """
        Return a mutable set of all the dot positions of the given block.
        - Dot positions are relative towards the block's anchor.
        ASSUMPTIONS
        - The given block is a proper block.
    """

    dot_positions = set()

    for j in range(len(block)):
        for k in range(len(block[0])):
            if block[j][k] == 1:
                dot_positions.add((j, k))
    return dot_positions


def is_proper_block(block):
    """
        Check whether the given block is a proper block.
        - True if and only if the set of dot positions of the given block is not empty,
          if each of its elements is a proper position, and if the dot positions of the
          given block are chained together.
        ASSUMPTIONS:
        - None
    """


    dot_positions = get_all_dot_positions(block)

    if len(dot_positions) > 0:  # and len(block[0]) > 0 and len(block) > 0: # and Position.are_chained(block):
        for pos in dot_positions:
            if not Position.is_proper_position(pos):
                return False
        return True


def add_dot(block, dot_position):
    """
        Add the given dot position to the given block.
        - Nothing happens if the given block already has a dot at the given position, or
          if the given dot cannot be chained with existing dots of the given block.
        ASSUMPTIONS
        - The given block is a proper block.
        - The given position is a proper position.
    """


    dot_positions = get_all_dot_positions(block)
    dot_x = dot_position[0]
    dot_y = dot_position[1]

    if dot_position in block:
        return
    if not Position.is_adjacent_to(dot_position, dot_positions):
        return
    block[dot_x][dot_y] = 1


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



    dot_positions = get_all_dot_positions(block)
    temp_block = list.copy(block)
    copy_dot_positions = get_all_dot_positions(temp_block)
    dot_x = dot_position[0]
    dot_y = dot_position[1]

    if dot_position not in dot_positions:
        return
    if len(dot_positions) <= 1:
        return
    if not Position.are_chained(copy_dot_positions):
        return
    # arechained werkt nog niet
    block[dot_x][dot_y] = 0


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


    dot_positions = get_all_dot_positions(block)
    print(dot_positions)

    for pos in dot_positions:
        last_left_x = pos[0]
        last_right_x = pos[0]
        print((last_left_x, last_right_x))
        break

    if len(dot_positions) == 1:
        for pos in dot_positions:
            return pos
    for pos in dot_positions:
        x = pos[0]

        if x < last_left_x:
            last_left_x = x
        if x > last_right_x:
            last_right_x = x

    return (last_left_x, last_right_x)

#
# the_block = make_block({(-1, 0), (0, 0), (1, 0), (2, 0), (1, 1)})
# print(get_horizontal_offsets_from_anchor(the_block))  # == (-1, 2)
# the_block = make_block({(3, 0), (4, 0), (4, 1)})
# assert get_horizontal_offsets_from_anchor(the_block) == (3, 4)


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



    dot_positions = get_all_dot_positions(block)

    for pos in dot_positions:
        last_left_y = pos[1]
        last_right_y = pos[1]
        break

    if len(dot_positions) == 1:
        return block[0][0]
    for pos in dot_positions:
        y = pos[1]
        if y < last_left_y:
            last_left_y = y
        if y > last_right_y:
            last_right_y = y

    return (last_left_y, last_right_y)


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

    h_offset_block = get_horizontal_offsets_from_anchor(block)
    h_offset_other_block = get_horizontal_offsets_from_anchor(other_block)
    v_offset_block = get_vertical_offsets_from_anchor(block)
    v_offset_other_block = get_vertical_offsets_from_anchor(other_block)

    dot_positions = get_all_dot_positions(block)
    dot_positions_other_block = get_all_dot_positions(other_block)

    if len(dot_positions) != len(dot_positions_other_block):
        return False
    if (len(dot_positions) == 1) and (len(dot_positions_other_block) == 1):
        return True
    if v_offset_block[0] - v_offset_block[1] != v_offset_other_block[0] - v_offset_other_block[1]:
        print(v_offset_other_block, v_offset_block)
        return False
    if h_offset_block[0] - h_offset_block[1] != h_offset_other_block[0] - h_offset_other_block[1]:
        print(h_offset_block, h_offset_other_block)
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

    dot_positions = get_all_dot_positions(block)

    for pos in dot_positions:
        if pos == (0, 0):
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
            print(printout[row][col], end=" ")
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
