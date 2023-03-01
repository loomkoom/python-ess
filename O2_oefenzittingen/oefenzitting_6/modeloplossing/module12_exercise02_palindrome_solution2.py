# If you want to avoid the extra memory required for
# the slice in the first solution, you can add parameters
# start and end to the function to delineate the portion
# of the word to be investigated

def is_palindrome(word,start=0,end=-1):
  """ Check whether the given word is a palindrome.
      A word is a palindrome if reads the same from left to
      right or from right to left. """
  if len(word)-start+end+1 <= 1:
    return True
  else:
    return (word[start] == word[end]) and is_palindrome(word,start+1,end-1)

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