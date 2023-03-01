from turtle import forward, left, right, speed


def draw_snowflake_side(length, levels):
    """
    Draw a single side of a snowflake with a given length
    and a given number of recursive levels.
    """
    if levels == 0:
        forward(length)
        return
    length /= 3.0
    draw_snowflake_side(length, levels - 1)
    left(60)
    draw_snowflake_side(length, levels - 1)
    right(120)
    draw_snowflake_side(length, levels - 1)
    left(60)
    draw_snowflake_side(length, levels - 1)


def draw_snowflake(length, levels):
    """
    Draw a snowflake consisting of three snowflake sides,
    with a given length and a given number of recursive levels.
    """
    for i in range(3):
        draw_snowflake_side(length, levels)
        right(120)


if __name__ == "__main__":
    # turtle speed set to turbo
    speed(0)
    draw_snowflake(400, 4)
    input("Return to quit.")
