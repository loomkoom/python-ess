def is_palindrome(word):
  """ Check whether the given word is a palindrome.
      A word is a palindrome if reads the same from left to
      right or from right to left. """
  if len(word) <= 1:
    return True
  else:
    return (word[0] == word[-1]) and is_palindrome(word[1:-1])

assert is_palindrome("")
assert is_palindrome("a")
assert is_palindrome("aa")
assert not is_palindrome("ab")
assert is_palindrome("aba")
assert not is_palindrome("aab")
assert is_palindrome("kayak")
assert not is_palindrome("racehorse")
assert is_palindrome("racecar")
assert is_palindrome("wasitacatisaw")
