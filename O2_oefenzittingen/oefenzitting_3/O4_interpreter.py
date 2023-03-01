"""
A function that interprets simple commands.
The commands can be of following forms:
    - "add x y": add x and y with x and y both floating point values
    - "subtract x y": subtract y from x with x and y both floating point values

The function must always return a float point value.

For example: "add 5.7 6.3" should return 12.0
             "subtract -55.5 55.2" should return -110.7

Hint: The split function of strings (https://docs.python.org/3.6/library/stdtypes.html#str.split) 
splits a given string into its parts. For example:

string = "add 5.0 3.0"
string.split() == ["add", "5.0", "3.0"]
"""
def interpreter(command):

    lst = command.split()

    if lst[0] == 'add' :
        answer = float(lst[1]) + float(lst[2])
    elif lst[0] == 'subtract' :
        answer = float(lst[1]) - float(lst[2])
    return answer

    

# TESTS
assert interpreter("add 5.7 6.3") == 12.0
assert interpreter("add -5 10") == 5
assert interpreter("add 10 -5") == interpreter("add -5 10")
assert interpreter("subtract -55.5 55.2") == -110.7
assert interpreter("subtract 10 5") == 5
assert interpreter("subtract 5 10") == -interpreter("subtract 10 5")