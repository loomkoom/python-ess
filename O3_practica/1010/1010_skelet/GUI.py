from tkinter import *

import Board
import Block
import Game
import Position

import math


# Python 3.6.5

def build_gui(state):
    root = Tk()

    dimension = Board.dimension(state["board"])

    rows = dimension
    cols = dimension

    # setup grid
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)
    grid = Frame(root)
    grid.grid(row=0, column=0, sticky=N + S + E + W)

    main_field = build_field(state, grid, cols, rows, handle_main_field)
    reset_colors(main_field)
    state["main_field"] = main_field

    bottom = Frame(grid, bg="black")
    bottom.grid(row=rows, sticky=N + S + E + W, columnspan=cols)

    spd = state["spawn_size"]
    spawn_field = build_field(state, bottom, spd * 2, spd * 2,
                              handle_spawn_field)
    reset_colors(spawn_field)
    state["spawn_field"] = spawn_field

    col_floor = math.floor(cols / 2)

    state["score_text"] = StringVar()
    score_lbl = Label(grid, textvariable=state["score_text"], bg="#eee",
                      fg="black")
    score_lbl.grid(row=rows + 1, column=0, sticky=N + S + E + W,
                   columnspan=col_floor)
    state["score_text"].set("Score: 0")

    state["message"] = StringVar()
    msg = Label(grid, textvariable=state["message"], bg="#ffa3a3", fg="black")
    msg.grid(row=rows + 1, column=col_floor, sticky=N + S + E + W,
             columnspan=col_floor + 1)
    state["message"].set("Good luck!")

    return root


def build_field(state, grid, cols, rows, handler):
    field = {}
    for r in range(rows):
        Grid.rowconfigure(grid, r, weight=1)
        for c in range(cols):
            Grid.columnconfigure(grid, c, weight=1)
            btn = Label(grid, state="disabled", bg="white", text="     ",
                        borderwidth=2, relief="groove")
            p = (c + 1, rows - r)
            btn.bind("<Button-1>", lambda e, p=p: handler(state, p))
            btn.grid(row=r, column=c, sticky=N + S + E + W)
            field[p] = btn
    return field


def reset_colors(field):
    for v in field.values():
        v.configure(bg="white", highlightbackground="black")


def handle_main_field(state, position):
    if not Board.can_be_dropped_at(state["board"], state["block"], position):
        state["message"].set(f"Cannot be dropped at {position}")
    else:
        drop_current_block(state, position)
        new_block(state)

    if len(Board.get_droppable_positions(state["board"], state["block"])) <= 0:
        state["score_text"].set(f"Game Over, final score: {state['score']}")


def handle_spawn_field(state, position):
    print(position, state)


def drop_current_block(state, position):
    state["score"] += Game.game_move(state["board"], state["block"], position)
    state["score_text"].set(f"Score: {state['score']}")
    draw_board(state)


def draw_board(state):
    reset_colors(state["main_field"])
    ps = Board.get_all_filled_positions(state["board"])
    for p in ps:
        state["main_field"][p].configure(bg="blue", highlightbackground="blue")


def draw_block(state):
    block = state["block"]
    spd = state["spawn_size"]
    block_poss = Block.get_all_dot_positions(block)
    for p in block_poss:
        translated = Position.translate_over(p, spd, spd)
        state["spawn_field"][translated].configure(bg="gray",
                                                   highlightbackground="gray")
    anchor = state["spawn_field"][Position.translate_over((0, 0), spd, spd)]
    anchor.configure(bg="red", highlightbackground="red")


def new_block(state):
    reset_colors(state["spawn_field"])
    state["block"] = Block.normalize(Block.select_standard_block())
    draw_block(state)


if __name__ == '__main__':
    board = Board.make_board(10)

    my_state = {"score": 0, "placing": False, "board": board, "block": None,
                "message": None, "spawn_size": 6}

    frame = build_gui(my_state)

    new_block(my_state)

    frame.mainloop()
