def are_chainable(board, positions, targets = None, path = None):
    # ZIE VB MAZE

    positions = sorted(list(positions))
    new_positions = []

    if len(positions) <= 1:
        return True

    current = positions[0]

    if path is None:
        path = list((current,))
    path.append(current)
    path = sorted(list(set(path)))
    if targets is None:
        targets = list(positions[1:])
    elif len(targets) > 1:
        for pos in targets:
            if current == pos:
                targets.remove(pos)
    else:
        for pos in targets:
            if pos in path and Position.are_chained(path):
                return True

    if is_filled_at(board, targets[-1]):
        state = "Filled"
    elif not is_filled_at(board, targets[-1]):
        state = "Free"

    for neighbour in Position.get_adjacent_positions(current, dimension(board)):
        if ((((state == "Filled") and (
                neighbour in board and board[neighbour] != "Free"))
             or ((state == "Free") and (
                        (neighbour not in board) or (neighbour in board and board[neighbour] == "Free"))))) and (
                neighbour not in path):
            assert ((state == "Filled" and board[neighbour] == "Filled") or (state == "Free" and (
                    (neighbour not in board) or (neighbour in board and board[neighbour] == "Free"))))
            assert ((state == "Filled" and board[current] == "Filled") or (state == "Free" and (
                    (current not in board) or (current in board and board[current] == "Free"))))
            next_pos = neighbour
            new_positions.append(next_pos)
            new_positions.extend(targets)
            # new_positions = sorted(list(set(new_positions)))
            # print('next', next_pos)

            print('p', path)
            solution = are_chainable(board, new_positions, targets, path)
            if solution is not False:
                # print('sol', solution)
                return solution
    return False


def are_chainable(board, positions, state = None, targets = None, path = None):
    # ZIE VB MAZE

    positions = sorted(list(positions))
    board = copy_board(board)
    new_positions = []

    if len(positions) <= 1:

        return True

    current = positions[0]
    print('1 cur', current, 'tar', sorted(positions[1:]))
    if targets is None:
        targets = list(positions[1:])
    elif len(targets) > 1:
        for pos in targets:
            if current == pos:
                targets.remove(pos)
    elif [current] == targets and Position.are_chained(path):
        return True

    print('2 cur', current, 'tar', targets)

    # if target == current:
    #     print('target=current')
    #     return True

    if state is None:
        if is_filled_at(board, current):
            state = "Filled"
        elif not is_filled_at(board, current):
            state = "Free"
        print("state", state)

    for neighbour in Position.get_adjacent_positions(current, dimension(board)):
        # print('neighbour', neighbour)
        if (((state == "Filled") and (
                neighbour in board and board[neighbour] != "Free"))
                or ((state == "Free") and (
                        (neighbour not in board) or (neighbour in board and board[neighbour] == "Free")))):
            next_pos = neighbour
            new_positions.append(next_pos)
            new_positions.extend(targets)
            new_positions = sorted(list(set(new_positions)))
            print('next', new_positions)

            if path is None:
                path = list((current,))
            path.append(current)
            path = sorted(list(set(path)))

            if state == "Filled":
                free_cell(board, current)
            elif state == "Free":
                fill_cell(board, current)
            if len(new_positions) == 0:
                return False
            print('p', path)
            solution = are_chainable(board, new_positions, state, targets, path)
            if solution is not False:
                # print('sol', solution)
                return solution
            else:
                if state == "Filled":
                    fill_cell(board, current)
                elif state == "Free":
                    free_cell(board, current)

    return False


def are_chainable(board, positions, state = None, targets = None, path = None):
    # ZIE VB MAZE

    positions = sorted(list(positions))
    board = copy_board(board)
    new_positions = []

    if len(positions) <= 1:
        return True

    current = positions[0]
    # print('1 cur', current, 'tar', sorted(positions[1:]))

    if path is None:
        path = list((current,))
    if targets is None:
        targets = list(positions[1:])
    elif len(targets) > 1:
        for pos in targets:
            if current == pos:
                targets.remove(pos)
    elif [current] == targets and Position.are_chained(path):
        return True

    # print('2 cur', current, 'tar', targets)

    # if target == current:
    #     print('target=current')
    #     return True

    if state is None:
        if is_filled_at(board, targets[-1]):
            state = "Filled"
        elif not is_filled_at(board, targets[-1]):
            state = "Free"
    print("state", state)
    print('cur', current, 'tar', targets)

    for neighbour in Position.get_adjacent_positions(current, dimension(board)):
        # print('neighbour', neighbour)
        if ((((state == "Filled") and (
                neighbour in board and board[neighbour] != "Free"))
             or ((state == "Free") and (
                        (neighbour not in board) or (neighbour in board and board[neighbour] == "Free"))))) and (
                neighbour not in path):
            assert ((state == "Filled" and board[neighbour] == "Filled") or (state == "Free" and (
                    (neighbour not in board) or (neighbour in board and board[neighbour] == "Free"))))
            print(current, state)
            assert ((state == "Filled" and board[current] == "Filled") or (state == "Free" and (
                    (current not in board) or (current in board and board[current] == "Free"))))
            next_pos = neighbour
            new_positions.append(next_pos)
            new_positions.extend(targets)
            # new_positions = sorted(list(set(new_positions)))
            print('next', next_pos)

            path.append(current)
            path = sorted(list(set(path)))

            # if state == "Filled":
            #     free_cell(board, current)
            # elif state == "Free":
            #     fill_cell(board, current)
            if len(new_positions) == 0:
                return False
            print('p', path)
            solution = are_chainable(board, new_positions, state, targets, path)
            if solution is not False:
                # print('sol', solution)
                return solution
            # else:
            #     if state == "Filled":
            #         fill_cell(board, current)
            #     elif state == "Free":
            #         free_cell(board, current)


def are_chainable(board, positions, targets = None, path = None):
    # ZIE VB MAZE

    positions = sorted(list(positions))
    new_positions = []

    if len(positions) <= 1:
        return True

    current = positions[0]

    if path is None:
        path = list((current,))
    if targets is None:
        targets = list(positions[1:])
    elif len(targets) > 1:
        for pos in targets:
            if current == pos:
                targets.remove(pos)
    elif [current] == targets and Position.are_chained(path):
        return True

    if is_filled_at(board, targets[-1]):
        state = "Filled"
    elif not is_filled_at(board, targets[-1]):
        state = "Free"

    print("state", state)
    print('cur', current, 'tar', targets)

    for neighbour in Position.get_adjacent_positions(current, dimension(board)):
        # print('neighbour', neighbour)
        if ((((state == "Filled") and (
                neighbour in board and board[neighbour] != "Free"))
             or ((state == "Free") and (
                        (neighbour not in board) or (neighbour in board and board[neighbour] == "Free"))))) and (
                neighbour not in path):
            assert ((state == "Filled" and board[neighbour] == "Filled") or (state == "Free" and (
                        (neighbour not in board) or (neighbour in board and board[neighbour] == "Free"))))
            print(current, state)
            assert ((state == "Filled" and board[current] == "Filled") or (state == "Free" and (
                        (current not in board) or (current in board and board[current] == "Free"))))
            next_pos = neighbour
            new_positions.append(next_pos)
            new_positions.extend(targets)
            # new_positions = sorted(list(set(new_positions)))
            print('next', next_pos)

            path.append(current)
            path = sorted(list(set(path)))

            if len(new_positions) == 0:
                return False
            print('p', path)
            solution = are_chainable(board, new_positions, targets, path)
            if solution is not False:
                # print('sol', solution)
                return solution


def are_chainable(board, positions, state = None, targets = None, path = None, left = None):
    # ZIE VB MAZE

    positions = sorted(list(positions))
    board = copy_board(board)
    new_positions = []

    if len(positions) <= 1:
        return True
    if left is None:
        left = len(positions)

    current = positions[0]

    if path is None:
        path = list((current,))

    # print('1 cur', current, 'tar', sorted(positions[1:]))
    if targets is None:
        targets = positions.copy()
    if len(targets) >= 1:
        for pos in path:
            for target in targets:
                if pos == target:
                    targets.remove(target)
                    left -= 1
        print('l', left)
    elif left == 0 and Position.are_chained(path):
        return True
    print('1 cur', current)
    print('tar', targets)

    # if target == current:
    #     print('target=current')
    #     return True

    if state is None:
        if is_filled_at(board, current):
            state = "Filled"
        elif not is_filled_at(board, current):
            state = "Free"
        print("state", state)

    for neighbour in sorted(list(Position.get_adjacent_positions(current, dimension(board)))):
        # print('neighbour', neighbour)
        # print(sorted(list(Position.get_adjacent_positions(current,dimension(board)))))
        if (((state == "Filled") and (
                neighbour in board and board[neighbour] != "Free"))
                or ((state == "Free") and (
                        (neighbour not in board) or (neighbour in board and board[neighbour] == "Free")))):
            if neighbour not in path:

                new_positions.append(neighbour)
                new_positions.extend(targets)
                new_positions = sorted(list(set(new_positions)))
                print('2 cur', current, 'neighbour', neighbour)
                print('next', new_positions)

                path.append(neighbour)
                path = sorted(list(set(path)))

                # if state == "Filled":
                #     free_cell(board, current)
                # elif state == "Free":
                #     fill_cell(board, current)
                if len(new_positions) == 0:
                    return False
                print('next', new_positions)
                print('p', path)
                print('new cycle', end = '\n\n')
                solution = are_chainable(board, new_positions, state, targets, path, left)
                if solution is not False:
                    # print('sol', solution)
                    return solution
                # else:
                #     if state == "Filled":
                #         fill_cell(board, current)
                #     elif state == "Free":
                #         free_cell(board, current)
                # path = []

    return False


def are_chainable(board, positions, targets = None, path = None):
    # ZIE VB MAZE

    positions = sorted(list(positions))
    new_positions = []

    if (len(positions)) <= 1 and (path is None):
        return True

    current = positions[0]

    if path is None:
        path = list((current,))
    path.append(current)
    path = sorted(list(set(path)))
    if targets is None:
        targets = list.copy(positions)
    elif len(targets) >= 1:
        for pos in targets:
            if current == pos:
                targets.remove(pos)
                if pos not in path:
                    path.append(pos)
        print('reached', current)
        print('target', targets)
        print('p', path)
    if len(targets) == 0 and Position.are_chained(path):
        return True

    if is_filled_at(board, current):
        state = "Filled"
    elif not is_filled_at(board, current):
        state = "Free"

    for neighbour in Position.get_adjacent_positions(current, dimension(board)):
        print('nbors', Position.get_adjacent_positions(current, dimension(board)))
        if ((((state == "Filled") and (
                neighbour in board and board[neighbour] != "Free"))
             or ((state == "Free") and (
                        (neighbour not in board) or (neighbour in board and board[neighbour] == "Free"))))) and (
                neighbour not in path):
            assert ((state == "Filled" and board[neighbour] == "Filled") or (state == "Free" and (
                    (neighbour not in board) or (neighbour in board and board[neighbour] == "Free"))))
            assert ((state == "Filled" and board[current] == "Filled") or (state == "Free" and (
                    (current not in board) or (current in board and board[current] == "Free"))))
            next_pos = neighbour
            new_positions.append(next_pos)
            new_positions.extend(targets)
            # new_positions = sorted(list(set(new_positions)))
            # print('next', next_pos)
            print('current', current, 'neighbour', neighbour)

            print('p', path, end = '\n\n')
            solution = are_chainable(board, new_positions, targets, path)
            if solution is not False:
                print(solution)
                return solution
    print('False')
    return False

    # if start > 0:
    #     last_high_score,last_dropped_positions = high_score(board, blocks)
    #     print(last_high_score,last_dropped_positions)
    #     print(blocks, start-1)
    #     high_score = last_high_score
    #     dropped_positions = last_dropped_positions

    # board_copy = Board.copy_board(board)
    # dropped_positions = list()
    # high_score = 0
    #
    # if start == len(blocks):
    #     # print('end', high_score, dropped_positions)
    #     # print('board', Board.get_all_filled_positions(board))
    #     return high_score, dropped_positions
    #
    # current_block = blocks[start]
    # droppable_positions = Board.get_droppable_positions(board_copy, current_block)
    #
    # for pos in droppable_positions:
    #     # print('pos',pos,'DROPPABLE',droppable_positions)
    #     last_score = game_move(board_copy, current_block, pos)
    #     dropped_positions.append(pos)
    #     filled_positions = list()
    #     for position in current_block:
    #         filled_pos = Position.translate_over((pos[0], pos[1]), position[0], position[1])
    #         filled_positions.append(filled_pos)
    #     if last_score > 0:
    #         solution = high_score(board_copy, blocks, start+1)
    #     else:
    #         solution = high_score(board_copy, blocks, start )
    #     # print('score',last_score)
    #     # print('dropped_pos', dropped_positions)
    #     # print('filled pos', filled_positions)
    #     # print('solution', solution)
    #         if solution is not (None, None):
    #             high_score = solution[0] + last_score
    #             # print('high score', high_score)
    #             dropped_positions += solution[1]
    #             solution = high_score, dropped_positions
    #             # print('solution', solution)
    #             return solution[0], solution[1]
    #         else:
    #             Board.free_all_cells(board_copy, filled_positions)
    #             dropped_positions = []
    #             start = 0
    #
    # return None,None

    # sol_positions = list()
    # board = Board.copy_board(board)
    # if len(blocks) == 0:
    #     return 0, []
    # if len(blocks) == start:
    #     print('base')
    #     return 0, (0, 0)
    # best = (None, None)
    # current_block = blocks[start]
    # for pos in Board.get_droppable_positions(board, current_block):
    #     # pos = min(Board.get_droppable_positions(board, current_block))
    #     score = game_move(board, current_block, pos)
    #     print('pos', pos)
    #     #print('score', score)
    #     solution = high_score(board, blocks, start - 1)
    #     print('solution', solution)
    #     high_score = score + solution[0]
    #     new_pos = (pos[0] + solution[1][0], pos[1] + solution[1][1])
    #     print('new pos',new_pos)
    #     sol_positions += (pos[0] + solution[1][0], pos[1] + solution[1][1])
    #     #sol_positions.append(new_pos)
    #     solution = high_score, sol_positions
    #     # print('solutions', sol_positions)
    #     # print('best', best)
    #     # print('high score', high_score)
    #     if (best is (None, None)) or (solution[0] > best[0]) or (solution[1] < best[1]):
    #         best = solution
    #         #print('best', best, sep = '\n\n')
    #         if len(best[1]) == len(blocks):
    #             return best
    #
    # #print('best', best,sep='\n\n')
    # return best

    high_score = None
    dropped_positions = None
    # print('start', start, 'len', len(blocks))

    if len(blocks) == 0 or start == len(blocks):
        # print('base', high_score, dropped_positions)
        # print('board', Board.get_all_filled_positions(board))
        return (0, [])

    current_block = blocks[start]
    droppable_positions = sorted(Board.get_droppable_positions(board, current_block))
    print('droppable', droppable_positions)

    for pos in droppable_positions:
        board_copy = Board.copy_board(board)
        # print("-for loop",end="\n\n")
        # print('pos', pos)
        # print("COPY")
        # Board.print_board(board_copy)
        # print("ORIGINAL")
        # Board.print_board(board)

        last_score = game_move(board_copy, current_block, pos)
        # print(last_score,end="\n\n")
        # print("COPY")
        # Board.print_board(board_copy)
        # print("ORIGINAL")
        # Board.print_board(board)

        filled_positions = Board.get_all_filled_positions(board_copy) - Board.get_all_filled_positions(board)

        rec_sol = rec_score, rec_positions = highest_score(board_copy, blocks, start + 1)
        Board.free_all_cells(board_copy, filled_positions)
        # print("COPY")
        # Board.print_board(board_copy)
        # print("ORIGINAL")
        # Board.print_board(board)

        # print('sol', rec_sol)
        # print('score', last_score)

        if rec_sol[0] is not None and (last_score is not None):
            score = last_score + rec_score
            if (high_score is None) or (score > high_score):
                high_score = score
                dropped_positions = [pos] + rec_positions

    print('high score', high_score, 'dropped pos', dropped_positions)
    return (high_score, dropped_positions)

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
        # print("triplet moves", triplet_combinations)
        for combination in range(0, len(triplet_combinations)):
            score, moves = highest_score(board, triplet_combinations[combination])
            print("score: ", score, "moves: ", moves)
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
                continue
            print("triplet:", triplet_nb, "block:", block_nb)
            print("position:", all_moves[triplet_nb][block_nb])
            print("posities", all_moves[triplet_nb])
            Block.print_block(block)
            game_move(board, block, all_moves[triplet_nb][block_nb])
            print("\n")
            Board.print_board(board)

        print("total score", total_score, "all moves", all_moves)

    Board.print_board(board)
    print(total_score)
    if ALL_TRIPLETS_DROPPED:
        return total_score
    return None
