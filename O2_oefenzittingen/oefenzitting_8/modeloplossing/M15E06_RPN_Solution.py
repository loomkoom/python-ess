def stepRPN(stack, symbol):
    """
    Perform one step of the RPN calculation on the given stack
    and returns the new stack.
    - If `symbol' is a number, it is pushed on top of the new stack.
    - If `symbol' is an operation, it is applied to the topmost
      elements of the stack and the result is pushed to the new stack.
    """
    if symbol == "*":
        return [stack[0]*stack[1]] + stack[2:]
    elif symbol == "+":
        return [stack[0]+stack[1]] + stack[2:]
    elif symbol == "-":
        return [stack[1]-stack[0]] + stack[2:]
    else:
        return [int(symbol)] + stack

def solveRPN(formula):
    """
    Calculates the value of an RPN formula.
    """
    stack = []

    for i in formula.split():
        stack = stepRPN(stack, i )

    return stack[0]

assert solveRPN("1 1 +") == 2
assert solveRPN("10 4 3 + 2 * -") == -4
