# The definition of ALL_COLORS is repeated here. That repetition can
# be avoided, but it would lead us to far at this point.
from random import choice

ALL_COLORS = ("red", "green", "blue", "yellow", "orange", "white")


def get_nb_black_white_matches(given, guess):
    """ Return the number of black and white matches of the guessed
    combination with respect to the given combination. The first
    element in the resulting tuple reflects the number of correct colors
    on their positions (black matches). The second element reflects
    the number of correct colors not on their position (white matches)."""

    black, white = 0, 0
    index = 0
    given = list(given)
    guess = list(guess)
    while index in range(0, len(guess)):
        if guess[index] == given[index]:
            black += 1
            del given[index], guess[index]
            index -= 1

        index += 1

    for index in range(len(guess)):
        if (guess[index] in given[index + 1:]) or (guess[index] in given[:index]):
            white += 1

    return black, white


def create_combination(nb_elements):
    """ Return a random combination involving the number of elements."""

    combination = []
    for index in range(nb_elements):
        combination[index:index] = [choice(ALL_COLORS)]

    return combination


# ! on the board, each row will consist of 4 circles representing 1 guess
# ! in total 10 rows should be drawn (as the user is given 10 guesses)
# ! You can create a circle by using the function:
# !     canvas.create_oval(x0, y0, x1, y1)
# ! It takes two pairs of coordinates: the top left and bottom right
# ! corners of the bounding rectangle. The (0,0) point is located in the
# ! top left corner of the canvas. We assume that each bounding square has
# ! a size of 30x30 and that all the circles are separated by 10 pixels
# ! from each other, and from the border (see picture in assignment).
# ! For example, the method call (with actual parameters) that generates
# ! the second circle of the third guess will look like:
# !         canvas.create_oval(50, 90, 80, 120)
# ! Later on in the program we modify the ovals to change color depending on
# ! the color that is selected by the person playing.
# ! In order to easily retrieve the correct oval, we expect that the function
# ! you implement here returns a nested list (i.e. a matrix) of
# ! the following form:
# !         [[circle1_guess1, circle2_guess1, ...],
# !          [circle1_guess2, ...],
# !          ...,
# !          [circle4_guess10]]
# ! The second circle of the third guess would for example be stored at:
# !          ovals[2][1] = canvas.create_oval(50, 90, 80, 120)
# ! Instead of approaching the nested list as a matrix, you can also
# ! treat it as a list of lists
# !          e.g. ovals[2].append(...)
# ! Note that the method create_oval has an implementation that
# ! takes 5 parameters. The fifth parameter has name 'fill' and allows
# ! you to assign a color (as a string) to it.
# ! Make sure that all the circles you draw get the fill color "grey".


def create_empty_circles(canvas, number_of_circles, max_number_of_moves):
    """ Return a matrix containing grey ovals that are correctly initialized
        at their required location.
    """

    ovals = []
    x = list(range(10, number_of_circles * 40, 40))
    y = list(range(10, max_number_of_moves * 40, 40))

    oval_list = [canvas.create_oval(x[a], y[b], x[a] + 30, y[b] + 30, fill='grey')
                 for b in range(max_number_of_moves)
                 for a in range(number_of_circles)]

    for n in range((len(oval_list) // number_of_circles)):
        ovals.append(oval_list[n * number_of_circles:(n + 1) * number_of_circles])

    return ovals


###############################################################################
# EXTRA

def any_color_in_combination(colors, given):
    """ Returns true if at least one color in colors is part of the
    given combination. False otherwise."""

    for index in range(len(colors)):
        if colors[index] in given:
            return True

    return False


def all_colors_in_combination(colors, given):
    """ Returns true if all the colors in colors are part of the
    given combination. False otherwise."""

    count = 0

    for index in range(len(colors)):
        if colors[index] in given:
            count += 1
        else:
            return False

    if count == len(colors):
        return True


def is_sublist_of(sublist, given):
    """ Returns whether the sublist is part of the given combination.
    The order of the sublist must also correspond to the order of the
    corresponding part in the given combination."""

    for index in range(0, len(given) - len(sublist) + 1):
        if sublist == given[index: index + len(sublist)]:
            return True

    return False
