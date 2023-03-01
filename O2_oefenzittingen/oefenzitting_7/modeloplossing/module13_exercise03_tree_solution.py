from turtle import forward, backward, left, right, speed, up, down, color
import turtle


# A tree is a trunk with a smaller tree going to the left and a smaller tree going to the right.
# tree(branch_length) will draw a tree with a trunk of size branch_length, and will draw smaller trees
# at 20 degrees to the left and at 20 degrees to the right. The smaller trees must have a branch_length equal
# to 60 % of the current branch_length. Trees should still be made as long as the branch_length is greater than 4.

# See Toledo for the image of the result!

# We use the turtle module to draw lines. The pointer (turtle) starts in
# the center. You can draw a straight line using `forward(length)` or `backward(length)` and can
# change the direction using `right(angle)` or `left(angle)`. The  angle is
# given in degrees. For details see https://docs.python.org/3/library/turtle.html

def tree(branch_length):
    if branch_length > 4:
        forward(branch_length)
        right(20)
        tree(branch_length * 0.6)
        left(40)
        tree(branch_length * 0.6)
        right(20)
        backward(branch_length)


if __name__ == "__main__":
    left(90)
    up()
    backward(100)
    down()
    color("green")
    tree(75.0)
    turtle.Screen().exitonclick()
