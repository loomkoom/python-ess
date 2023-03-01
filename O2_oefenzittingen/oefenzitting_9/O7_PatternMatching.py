def matches(word,pattern):
    """ Check whether the given word matches the given pattern.
    The word matches if and only if each letter in the given word is
    (1) identical to the character at the corresponding position in the pattern, or
    (2) the corresponding character in the pattern is an equal sign and the given
        letter is identical to the preceding letter in the word, or
    (3) the corresponding character in the pattern is an exclamation mark and the
        given letter differs from the preceding letter in the word."""
    return None

##TESTS
# Matching string without special characters in the pattern.
assert matches("abc","abc")
# Non-matching string without special characters in the pattern.
assert not matches("ade","abc")
# Non-matching string because last character does not match.
assert not matches("abd","abc")
# Matching string with equality signs in the pattern.
assert matches("abbccddd", "ab=c=d==")
# Non-matching string with equality signs in the pattern.
assert not matches("abbccddd","ab=c=de=")
# Matching string with exclamation marks in the pattern.
assert matches("abccdded", "ab!c!d!!",)
# Non-matching string with exclamation marks in the pattern.
assert not matches("abccddee", "ab!c!d!!")
# Complex pattern
assert matches("abccccdeefz", "ab!c==d!=!z")
# Empty string
assert matches("", "")
