import turtle


# The Koch snowflake uses a recursive construction on all three
# sides (line segments) of a given triangle. For the details of
# this construction see https://en.wikipedia.org/wiki/Koch_snowflake#Construction
# Also see the example image on Toledo or Wikipedia!
#
# We use the turtle module to draw lines. The pointer (turtle) starts in
# the center. You can draw a straight line using `forward(length)` and can
# change the direction using `right(angle)` or `left(angle)`. The  angle is
# given in degrees. For details see https://docs.python.org/3/library/turtle.html


def draw_snowflake_side(length, levels):
    """
    Draw a single side of a snowflake with a given length
    and a given number of recursive levels.
    """
    if levels == 0:
        turtle.forward(length)
    else:
        length /= 3
        levels -= 1
        draw_snowflake_side(length, levels)
        turtle.right(60)
        draw_snowflake_side(length, levels)
        turtle.left(120)
        draw_snowflake_side(length, levels)
        turtle.right(60)
        draw_snowflake_side(length, levels)


def draw_snowflake(length, levels):
    """
    Draw a snowflake consisting of three snowflake sides,
    with a given length and a given number of recursive levels.
    """
    draw_snowflake_side(length, levels)
    turtle.left(360.0 / 3.0)
    draw_snowflake_side(length, levels)
    turtle.left(360.0 / 3.0)
    draw_snowflake_side(length, levels)


if __name__ == "__main__":
    # turtle speed set to turbo
    turtle.speed(0)
    # draw a snowflake
    draw_snowflake(400, 5)
    # keep the window open after drawing
    turtle.Screen().exitonclick()
