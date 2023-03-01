def get_column(nb=1):
    """
      Return the letter standing for the given column on a
      chessboard.
    """
    return chr(nb + ord("a") - 1)


assert get_column(1) == "a"
assert get_column(5) == "e"
assert get_column(8) == "h"

def next_column(col):
    # col_nb = ord(col)-ord("a")+1
    # return chr(col_nb+ord("a"))

    col_nb = ord(col)+1
    return chr(col_nb)

assert next_column("a") =="b"
assert next_column("c") == "d"


def is_attacked_by(invest, attacker):
    """
      Check whether a queen at position invest on a
      chessboard would be attacked by another queen at
      position attacker.
      - Positions are tuples starting with the letter of
        the column followed by the digit of the row.
    """

    # Same position?
    if (attacker == invest):
        return False

    # Same column?
    if (attacker[0] == invest[0]):
        return True

    # Same row?
    if (attacker[1] == invest[1]):
        return True

    # Same diagonal?
    if abs(ord(attacker[0]) - ord(invest[0])) == \
            abs(attacker[1] - invest[1]):
        return True

    return False


# Same position
assert not is_attacked_by(("a", 3), ("a", 3))
# Same column
assert is_attacked_by(("c", 4), ("c", 7))
assert not is_attacked_by(("c", 4), ("e", 7))
# Same row
assert is_attacked_by(("c", 4), ("d", 4))
# Same diagonal
assert is_attacked_by(("b", 3), ("c", 4))
assert is_attacked_by(("b", 3), ("a", 4))
assert is_attacked_by(("b", 3), ("c", 2))
assert is_attacked_by(("b", 3), ("a", 2))


def is_under_attack_of(invest, attackers):
    """
      Check whether a queen at position invest on a
      chessboard would be attacked by at least one queen at
      a position in the given collection of positions
      attackers.
    """

    for pos in attackers:
        if is_attacked_by(invest, pos):
            return True

    return False


assert not is_under_attack_of(("c", 4), [])
assert is_under_attack_of(("c", 4), [("a", 3), ("c", 7)])
assert not is_under_attack_of(("c", 4), [("c", 4), ("h", 3), ("d", 7)])


def eight_queens(filled_positions=(),curr_col="a",curr_row=1):
    """
       Return a solution for the eight queens problem involving the given tuple of
       positions at which queens must be positioned.
       - The given positions are positions in the first columns of a chess board.
       - Queens on the given positions do not attack each other.
       - The solution reveals all eight positions in the order from left to right
         at which queens must be positioned.
       - The function returns None if no such solution exists.
    """
    if len(filled_positions) == 8:
        return filled_positions
    curr_pos = (curr_col,curr_row)
    if not is_under_attack_of(curr_pos,filled_positions):
        extended_positions = filled_positions + (curr_pos,)
        solution = eight_queens(extended_positions,next_column(curr_col),1)
        if solution != None:
            return solution
    if curr_row < 8:                                                            #backtrack
        return eight_queens(filled_positions,curr_col,curr_row+1)




print(eight_queens(()))
print(eight_queens((('a',8),),"b"))                     # print(eight_queens((('a',8),)))           is fout ( kolom meegeven )
print(eight_queens((('a',1),('b',4)),"c"))              # print(eight_queens((('a',1),('b',4))))    ook



# lijst gebruiken ipv tuple

def eight_queens(filled_positions=[],curr_col="a",curr_row=1):
    """
       Return a solution for the eight queens problem involving the given list of
       positions at which queens must be positioned.
       - The given positions are positions in the first columns of a chess board.
       - Queens on the given positions do not attack each other.
       - The solution reveals all eight positions in the order from left to right
         at which queens must be positioned.
       - The function returns None if no such solution exists.
    """
    if len(filled_positions) == 8:
        return filled_positions
    curr_pos = (curr_col, curr_row)
    if not is_under_attack_of(curr_pos, filled_positions):
        # extended_positions = filled_positions + (curr_pos,)
        list.append(filled_positions,curr_pos)
        solution = eight_queens(filled_positions, next_column(curr_col), 1)
        if solution != None:
            return solution
        list.pop(filled_positions,len(filled_positions)-1)

    if curr_row < 8:  # backtrack
        return eight_queens(filled_positions, curr_col, curr_row + 1)



print(eight_queens([]))
print(eight_queens([('a',8)],"b"))
print(eight_queens([('a',1),('b',4)],"c"))





def eight_queens(given_positions=()):

  """
    Starting from a tuple of given positions, return all
    possible positions of eight queens on a chessboard,
    such that no queen attacks another queen.
    - The given k positions are positions for the queens
      in the first k column
    - Queens at those positions do not attack each other.
  """

  solutions = set()

  if len(given_positions) == 8:
    solutions.add(given_positions)

  else:

    curr_col = get_column(len(given_positions) + 1)

    for row in range(1, 9):

      if not is_under_attack_of \
              ((curr_col, row), given_positions):
        set.update(solutions, \
                   eight_queens(given_positions + ((curr_col, row),)))

  return solutions


# Number of solutions for the eight queens problem
assert len(eight_queens()) == 92

# The solution illustrated in Figure 15 is included.
assert (('a', 8), ('b', 4), ('c', 1), ('d', 3), ('e', 6), ('f', 2), ('g', 7), ('h', 5)) in eight_queens()




#! An alternative version involving lists of positions
#! instead of tuples of positions.
def eight_queens_alt(given_positions=[]):

  """
    Starting from a tuple of given positions, return all
    possible positions of eight queens on a chessboard,
    such that no queen attacks another queen.
    - The given k positions are positions for the queens
      in the first k column
    - Queens at those positions do not attack each other.
  """

  solutions = set()

  if len(given_positions) == 8:
    solutions.add(tuple(given_positions))

  else:
    curr_col = get_column(len(given_positions)+1)

    for row in range(1,9):

      curr_pos = (curr_col,row)

      if not is_under_attack_of\
                (curr_pos,given_positions):

        list.append(given_positions,curr_pos)
        set.update(solutions,
            eight_queens_alt(given_positions))
        list.remove(given_positions,curr_pos)

  return solutions



assert len(eight_queens_alt()) == 92
print(eight_queens_alt())
# The solution illustrated in Figure 15 is included.
assert (('a', 8), ('b', 4), ('c', 1), ('d', 3),('e', 6), ('f', 2), ('g', 7), ('h', 5)) in eight_queens()

# print(len(eight_queens()))
# print(eight_queens((('a',8),)))
# print(eight_queens((('a',1),('b',4))))

