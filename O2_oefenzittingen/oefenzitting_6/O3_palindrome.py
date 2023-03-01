def is_palindrome(word):
    """ Check whether the given word is a palindrome.
        A word is a palindrome if reads the same from left to
        right or from right to left. """

    start = 0
    end = len(word) - 1

    if len(word) <= 1:
        return True
    if word[start] != word[end]:
        return False
    else:
        return is_palindrome(word[start + 1:end])


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
