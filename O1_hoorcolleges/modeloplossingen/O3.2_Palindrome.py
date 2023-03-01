# Check whether a given string is a palindrome.
#   - A string is a palindrome if it reads the same from
#     left-to-right as from right-to-left.
#   - The program prompts the end-user for the string to
#     investigate and displays a message whether or not
#     it is a palindrome.

string = input("Enter the string to investigate: ")

pos_next_char = 0
still_palindrome = True

while (pos_next_char < len(string)/2) and \
       still_palindrome:

  if string[pos_next_char] != \
         string[-(pos_next_char+1)]:
    still_palindrome = False
  else:
    pos_next_char += 1

if still_palindrome:
  print("The string \"" + string + "\" is a palindrome!")
else:
  print("The string \"" + string + \
            "\" is not a palindrome!")
