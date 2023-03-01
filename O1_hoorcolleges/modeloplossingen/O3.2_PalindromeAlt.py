# Check whether a given string is a palindrome.
#   - A string is a palindrome if it reads the same
#     from left-to-right as from right-to-left.
#   - The program prompts the end user for the string
#     to investigate and displays a message whether or
#     not it is a palindrome.

string = input("Enter the string to investigate: ")

mid = len(string)//2
left_half = string[:mid]
right_half = string[-1:-mid-1:-1]

if left_half == right_half:
  print("The string \"" + string + "\" is a palindrome!")
else:
  print("The string \"" + string + \
        "\" is not a palindrome!")

