from tkinter import (Button,
                     Canvas,
                     FLAT,
                     NW,
                     Tk,
                     Label,
                     messagebox)

import MasterMindAsked
from random import choice

ALL_COLORS = ("red", "green", "blue", "yellow", "orange", "white")
random_combination = []
NUMBER_OF_CIRCLES = 5
MAX_NUMBER_OF_MOVES = 20
current_move = 0
guess_combination = []
canvas: str = ""
ovals = []
matching_position_label = ""
correct_color_label = ""
hints_used = 0


def draw_board(root):
    """
      Create the graphical user interface.
    """

    # provide the title that will be shown in the header
    root.title("Mastermind")

    # Indicate which variables of the program will be altered
    # ! In order to manipulate variables that are part of the program
    # ! but exist outside of the function, you need to indicate that you want
    # ! to use and alter these variables by declaring them as "global"
    global canvas, ovals, matching_position_label, correct_color_label

    # canvas will be the main board used for mastermind
    # ! to create a canvas, the constructor is called
    # ! (i.e. name of the class and required parameters)
    canvas = Canvas(root, bg="white", height=MAX_NUMBER_OF_MOVES * 40 + 170, width=NUMBER_OF_CIRCLES * 50 + 170)

    # Draw the empty circles representing the guesses
    ovals = MasterMindAsked.create_empty_circles(canvas, NUMBER_OF_CIRCLES, MAX_NUMBER_OF_MOVES)

    # Draw a line to separate the circles form the buttons
    canvas.create_line(NUMBER_OF_CIRCLES * 40+20, 10, NUMBER_OF_CIRCLES * 40+20, MAX_NUMBER_OF_MOVES * 40, width=3,
                       fill="black")

    # Draw the color buttons that will be used throughout the game
    # ! Every available color (listed here as strings in the global variable
    # ! ALL_COLORS) is represented in the GUI by a button
    # ! when the user clicks the button the function color(color_name)
    # ! is called
    for i in range(len(ALL_COLORS)):
        canvas.create_window(NUMBER_OF_CIRCLES * 40 + 60, 15 + i * 40, anchor=NW,
                             window=Button(canvas, command=lambda color_name=ALL_COLORS[i]: color(color_name), width=5,
                                           text=ALL_COLORS[i]))

    # Draw the result labels
    # ! matching_position_label and correct_color_label can be used later on
    # ! to show the user the number of correct positions and colors
    # ! (e.g. matching_position_label["text"] = "2")
    canvas.create_window(NUMBER_OF_CIRCLES * 20 - 15, MAX_NUMBER_OF_MOVES * 40 + 60, anchor=NW,
                         window=Label(canvas, text="Correct position: "))
    matching_position_label = Label(canvas)
    canvas.create_window(NUMBER_OF_CIRCLES * 20 + 90, MAX_NUMBER_OF_MOVES * 40 + 60, anchor=NW,
                         window=matching_position_label)

    canvas.create_window(NUMBER_OF_CIRCLES * 20 - 15, MAX_NUMBER_OF_MOVES * 40 + 90, anchor=NW,
                         window=Label(canvas, text="Correct color: "))
    correct_color_label = Label(canvas)
    canvas.create_window(NUMBER_OF_CIRCLES * 20 + 90, MAX_NUMBER_OF_MOVES * 40 + 90, anchor=NW,
                         window=correct_color_label)

    # Draw the submit button
    # ! when the user clicks the button,
    # ! the function check_combination is called
    submit_button = Button(canvas, text="Check", command=check_combination)
    submit_button.configure(width=10)
    canvas.create_window(NUMBER_OF_CIRCLES * 20 - 15, MAX_NUMBER_OF_MOVES * 40 + 120, anchor=NW, window=submit_button)

    # Draw the quit button
    quit_button = Button(canvas, text="Quit", command=root.destroy)
    quit_button.configure(width=5)
    canvas.create_window(NUMBER_OF_CIRCLES * 43 + 130, MAX_NUMBER_OF_MOVES * 40 + 130, anchor=NW, window=quit_button)

    # draw the hint button
    hint_button = Button(canvas, text="Hint", command=hint)
    hint_button.configure(width=10)
    canvas.create_window(NUMBER_OF_CIRCLES * 43 + 110, MAX_NUMBER_OF_MOVES * 40 + 60, anchor=NW, window=hint_button)

    # draw the sublist button
    sublist_button = Button(canvas, text="sublist", command=sublist)
    sublist_button.configure(width=10)
    canvas.create_window(NUMBER_OF_CIRCLES * 43 + 110, MAX_NUMBER_OF_MOVES * 40 + 90, anchor=NW, window=sublist_button)

    # draw the canvas
    canvas.pack()


def check_combination():
    """
      Check the current guess combination.
      If the guess combination is complete, the method increments the
      number of moves, it displays the number of correct colors on
      their position and the number of correct colors not on their
      position in the user interface, and it cleans the guess combination.
      If the guess combination is not complete, the method displays
      an error message.
    """

    global current_move, guess_combination

    # check if a complete combination is provided
    if len(guess_combination) < NUMBER_OF_CIRCLES:
        messagebox.showerror("Error!", "Please fill in a complete combo before hitting the 'Check' button!")
    else:
        current_move = current_move + 1
        nb_black_white_matches = MasterMindAsked.get_nb_black_white_matches(random_combination, guess_combination)
        print(nb_black_white_matches)
        matching_position_label["text"] = str(nb_black_white_matches[0])
        correct_color_label["text"] = str(nb_black_white_matches[1])
        if nb_black_white_matches[0] == NUMBER_OF_CIRCLES:
            messagebox.showinfo("Congratulations", "You have won the game")
            root.destroy()
        else:
            check_game_over()
            guess_combination = []


def check_game_over():
    """
      Display a message that the game is over, if the number of moves
      has reached the maximum number of moves.
    """

    global current_move

    if current_move == MAX_NUMBER_OF_MOVES:
        game_over_message = "Game Over! You have lost the game."
        solution = ", ".join(str(x) for x in random_combination)
        solution_message = "The correct combination was:\n" + solution
        ending_message = game_over_message + "\n" + solution_message
        messagebox.showinfo("Game over", ending_message)
        root.destroy()


# color callback function
def color(color_name):
    """
      Add the given color to the guess combination. The corresponding circle
      in the display is also filled with the color. If the guess combination is
      complete, an error message is displayed.
    """

    if len(guess_combination) == NUMBER_OF_CIRCLES:
        messagebox.showerror("Colors are full",
                             "No more colors allowed, please hit the 'Check' button to check your result")
    else:
        canvas.itemconfig(ovals[current_move][len(guess_combination)],
                          fill=color_name)
        guess_combination.append(color_name)


def hint():
    """
      Gives a hint of a random color (only once per game)
    """

    global hints_used
    hints_used += 1

    if hints_used > 1:
        messagebox.showerror('Not allowed', 'hint already used')

    else:
        hint_color = choice(random_combination)
        hint_position = random_combination.index(hint_color) + 1
        hint_message = "the color at position: " + str(hint_position) + " is: " + str(hint_color)
        messagebox.showinfo('Hint', hint_message)


def sublist(guess=guess_combination):
    """
        says if the current input(guess) combination is a sublist of the answer
    """

    if len(guess) < 1:
        messagebox.showerror('Sublist', 'The guessed combination is EMPTY \n'
                                        'please fill in a color')
    elif MasterMindAsked.is_sublist_of(guess, random_combination):
        sublist_message = "the current guess IS a sublist of the combination"
        messagebox.showinfo('sublist', sublist_message)
    else:
        sublist_message = "the current guess is NOT a sublist of the combination"
        messagebox.showinfo('sublist', sublist_message)

    for index in range(0, len(guess)):
        canvas.itemconfig(ovals[current_move][index], fill='grey')
    del guess[:]


root = Tk()
draw_board(root)
random_combination = MasterMindAsked.create_combination(NUMBER_OF_CIRCLES)
root.mainloop()
