"""
RPN (http://en.wikipedia.org/wiki/Reverse_Polish_notation) is alternative notation for mathematical formulas that
doesn't need parenthesis.

For example, instead of "10-((4+3)*2)", in RPN we write "10 4 3 + 2 * -". This formula is read from left to right, each
number is pushed onto a stack (or list), and each operation is applied to the topmost elements of the stack.

Implement a function stepRPN(stack, symbol) that processes one symbol (a number or an operation).

Implement a function solveRPN(formula) that calculates the value of a complete RPN formula by applying stepRPN on each
element as the step function. Hint: formula.split() splits a formula into a list of symbols.

(Optional) Add more operations, such as /, abs, **, %, sin, ln, ...
"""


def stepRPN(stack, symbol):
    """
    Perform one step of the RPN calculation on the given stack
    and returns the new stack.
    - If `symbol' is a number, it is pushed on top of the new stack.
    - If `symbol' is an operation, it is applied to the topmost
      elements of the stack and the result is pushed to the new stack.
    """
    if symbol == "*":
        return [stack[0] * stack[1]] + stack[2:]
    elif symbol == "+":
        return [stack[0] + stack[1]] + stack[2:]
    elif symbol == "-":
        return [stack[1] - stack[0]] + stack[2:]
    elif symbol == "/":
        return [stack[0] / stack[0]] + stack[2:]
    elif symbol == "**":
        return [stack[0] ** stack[0]] + stack[2:]
    else:
        return [int(symbol)] + stack


def solveRPN(formula):
    """
    Calculates the value of an RPN formula.
    """
    stack = []
    for symbol in formula.split():
        stack = stepRPN(stack,symbol)
        print(stack)

    return stack[0]


assert solveRPN("1 1 +") == 2
print()
assert solveRPN("10 4 3 + 2 * -") == -4

# Perhaps rewrite it as + 1 * 2 + 3 * 4....
