import turtle


# A tree is a trunk with a smaller tree going to the left and a smaller tree going to the right.
# tree(branch_length) will draw a tree with a trunk of size branch_length, and will draw smaller tree s
# at 20 degrees to the left and at 20 degrees to the right. The smaller trees must have a branch_length equal
# to 60 % of the current branch_length. Trees should still be made as long as the branch_length is greater than 4.

# See Toledo for the image of the result!

# We use the turtle module to draw lines. The pointer (turtle) starts in
# the center. You can draw a straight line using `forward(length)` or `backward(length)` and can
# change the direction using `right(angle)` or `left(angle)`. The  angle is
# given in degrees. For details see https://docs.python.org/3/library/turtle.html


def tree(branch_length, depth, angle, fraction):
    if branch_length > depth:
        turtle.forward(branch_length)
        # left branch
        turtle.left(angle)
        tree(branch_length * fraction, depth, angle, fraction)
        # right branch
        turtle.right(angle * 2)
        tree(branch_length * fraction, depth, angle, fraction)
        # back
        turtle.left(angle)
        turtle.backward(branch_length)


if __name__ == "__main__":
    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.backward(100)
    turtle.down()
    turtle.color("brown")

    tree(95, 9, 30, 0.7)
    turtle.Screen().exitonclick()
