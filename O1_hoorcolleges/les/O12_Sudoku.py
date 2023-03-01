def make_roster(*values):
    """
      Return a new roster that is filled with the given
      values.
      The value at position K in the supplied sequence
      corresponds to the value at position [K/3,K%3]
      in the resulting roster.
      Each of the given values is either a digit in the
      range 1..9 or the special value None.
    """

    roster = {}

    pos = (0, 0)

    for value in values:
        if value != None:
            set_value_at(roster, value, pos)
        pos = next_position(pos)

    return roster




def get_value_at(roster, pos):
    """
      Return the value registered at the given position
      in the given roster.
      None is returned if no value is registered at the
      given position.
    """

    return roster.get(pos, None)


def is_filled_at(roster, pos):
    """
      Check whether a value is registered at the given
      position in the given roster.
    """
    return get_value_at(roster, pos) != None


def set_value_at(roster, value, pos):
    """
      Set the given value at the given position in the
      given roster.
      The given value must be a digit in the range 1..9.
    """

    roster[pos] = value


def delete_value_at(roster, pos):
    """
      Delete the value at the given position in the given
      roster.
    """

    roster.pop(pos, None)


def row(pos):
    """
      Return the row of the given position.
    """

    return pos[0]


def col(pos):
    """
      Return the column of the given position.
    """

    return pos[1]


def group(pos):
    """
      Return the group to which the given position belongs.
    """

    return (row(pos) // 3) * 3 + (col(pos) // 3)


def next_position(pos):
    """
      Return the position next to the given position.
      If the given position is not at the end of a row, the
      position right to the given position is returned.
      Otherwise, the first position of the next row is returned.
      If that next row does not exist, None is returned.
    """

    if col(pos) < 8:
        return (row(pos), col(pos) + 1)

    elif row(pos) < 8:
        return (row(pos) + 1, 0)

    else:
        return None


def row_contains_value(roster, value, row):
    """
      Check whether the given value is registered in the
      given row of the given roster.
    """

    for col in range(0, 9):

        current_pos = (row, col)

        if value == get_value_at(roster, current_pos):
            return True

    return False


def column_contains_value(roster, value, col):
    """
      Check whether the given value is registered in the
      given column of the given roster.
    """

    for row in range(0, 9):

        current_pos = (row, col)

        if value == get_value_at(roster, current_pos):
            return True

    return False


def group_contains_value(roster, value, group):
    """
      Check whether the given value is registered in the
      given group of the given roster.
    """

    first_row = (group // 3) * 3
    first_col = (group % 3) * 3

    for row in range(first_row, first_row + 3):

        for col in range(first_col, first_col + 3):

            if value == get_value_at(roster, (row, col)):
                return True

    return False


def can_have_as_value_at(roster, value, pos):
    """
      Check whether the given roster can have the given value
      at the given position.
    """

    return (value == None) or \
           ((not row_contains_value(roster, value, row(pos))) and \
            (not column_contains_value(roster, value, col(pos))) and \
            (not group_contains_value(roster, value, group(pos))))


# Print the given roster one row per line.
def print_roster(roster):
    for row in range(0, 9):
        for col in range(0, 9):
            if is_filled_at(roster, (row, col)):
                print(str.format('{:^5}', get_value_at(roster, (row, col))), end="")
            else:
                print('     ', end="")
        print()


# TEST for make_roster
roster = make_roster(4, None, 3, None, 2, 1, None, 3, None, \
                     5, 6, None, None, 7, None, None, None, 8, \
                     9)
assert get_value_at(roster, (0, 0)) == 4
assert get_value_at(roster, (0, 2)) == 3
assert get_value_at(roster, (1, 1)) == 6
assert get_value_at(roster, (2, 0)) == 9

# TEST for is_filled_at
roster = make_roster(4, None, 3, None, 2, 1, None, 3, None, \
                     5, 6, None, None, 7, None, None, None, 8, \
                     9)
assert is_filled_at(roster, (0, 0))
assert not is_filled_at(roster, (0, 1))

# TEST for set_value_at
roster = make_roster(4, None, 3, None, 2, 1, None, 3, None, \
                     5, 6, None, None, 7, None, None, None, 8, \
                     9)
set_value_at(roster, 9, (0, 3))
assert get_value_at(roster, (0, 3)) == 9
set_value_at(roster, 7, (0, 2))
assert get_value_at(roster, (0, 2)) == 7

# TEST for delete_value_at
roster = make_roster(4, None, 3, None, 2, 1, None, 3, None, \
                     5, 6, None, None, 7, None, None, None, 8, \
                     9)
delete_value_at(roster, (1, 4))
assert not is_filled_at(roster, (1, 4))
delete_value_at(roster, (0, 1))
assert not is_filled_at(roster, (0, 1))

# TEST for group
assert group((3, 2)) == 3
assert group((4, 3)) == 4

# TEST for next_position
roster = make_roster()
pos = next_position((0, 0))
assert (pos[0] == 0) and (pos[1] == 1)
pos = next_position((0, 8))
assert (pos[0] == 1) and (pos[1] == 0)
pos = next_position((8, 8))
assert pos == None

# TEST for row_contains_value
roster = make_roster(4, None, 3, None, 2, 1, None, 3, None, \
                     5, 6, None, None, 7, None, None, None, 8, \
                     9)
assert row_contains_value(roster, 3, 0)
assert row_contains_value(roster, 4, 0)
assert row_contains_value(roster, 8, 1)
assert not row_contains_value(roster, 5, 7)

# TEST for column_contains_value
roster = make_roster(4, None, 3, None, 2, 1, None, 3, None, \
                     5, 6, None, None, 7, None, None, None, 8, \
                     9)
assert column_contains_value(roster, 5, 0)
assert column_contains_value(roster, 4, 0)
assert column_contains_value(roster, 8, 8)
assert not column_contains_value(roster, 5, 8)

# TEST for group_contains_value
roster = make_roster(4, None, 3, None, 2, 1, None, 3, None, \
                     5, 6, None, None, 7, None, None, None, 8, \
                     9, None, 1)
assert group_contains_value(roster, 5, 0)
assert group_contains_value(roster, 4, 0)
assert group_contains_value(roster, 1, 0)
assert group_contains_value(roster, 3, 2)
assert not group_contains_value(roster, 2, 0)

# TEST for can_have_as_value_at
roster = make_roster(4, None, 3, None, 2, 1, None, 3, None, \
                     5, 6, None, None, 7, None, None, None, 8, \
                     9, None, 1)
assert can_have_as_value_at(roster, 2, (2, 1))
assert can_have_as_value_at(roster, None, (0, 4))
assert not can_have_as_value_at(roster, 6, (0, 1))
assert not can_have_as_value_at(roster, 1, (0, 1))
assert not can_have_as_value_at(roster, 9, (0, 1))

print(make_roster())


def fill(roster, start_pos=(0, 0)):
    """
      Fill the given roster completely in a blind way
      starting from the given position.
      - The function returns a boolean that indicates
        whether or not a complete fill was possible.
      - All positions before the given start position are filled in
        according to the rules of Sudoku.
      - If no fill is possible, the roster has not changed. Otherwise,
        the roster is completely filled.
    """
    if start_pos == None:
        return True
    # er staat al een cijfer op de pos
    if get_value_at(roster,start_pos) != None:
        return fill(roster,next_position(start_pos))
    # er staat nog geen cijfer op de pos
    for value in range(1,10):
        if can_have_as_value_at(roster,value,start_pos):
            set_value_at(roster,value,start_pos)
            solution_found = fill(roster,next_position(start_pos))
            if solution_found:
                return True
    # geen opl gevonden ==> rooster onveranderd
    delete_value_at(roster,start_pos)
    return False




roster = make_roster()
assert fill(roster)
for r in range(0, 9):
    for c in range(0, 9):
        assert is_filled_at(roster, (r, c))
print_roster(roster)
print(fill(make_roster(1, None, 3, 4, 5, 6, 7, 8, 9, None, 2)))

roster = make_roster(1,None,3,4,None,6,7,8,None,10,None)
print_roster(roster)
print(roster)
