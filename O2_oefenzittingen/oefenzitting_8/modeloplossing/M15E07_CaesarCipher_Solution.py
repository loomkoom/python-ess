"""
A form of encoding that was already used by the Romans is the Caesar cipher. In this encoding, each letter was replaced
by the letter 3 places further down in the alphabet. For example, the string "coding is fun" can be encoded as
"frglqj lv ixq" in this way. You can do even more, and encode a word with any integer between 1 and 25.

In this exercise, you will implement a series of functions to encode a given string and help with deciphering a
given encoded string.

Use as much list comprehensions and filter/map as you can!
"""

# ---------------- Useful functions for this exercise ----------------
def letter(int):
    """
     Return the letter represented by the given integer (e.g. 'a' for 0, 'z' for 25).
    """
    return chr(ord('a') + int)

def integer(char):
    """
     Return the integer representation of a letter (e.g. 0 for 'a', 25 for 'z').
    """
    return ord(char) - ord('a')

def convert_to_string(iterator, separator = ''):
    """
     When using a filter or map function on a string, use this function to convert the result back to a string.
    """
    return separator.join(list(iterator))


# ---------------- Start your implementation here ----------------

"""
To encode and decode any given string, we just need a function that shifts a letter by the right amount, and a function
that encodes a string by using the shift function. To decode a string that was encoded with shift amount n, just use
encode(string, -n)
"""

def shift(char, amount):
    """
     Returns the character, shifted by the right amount. Only letters are shifted, spaces are left untouched.
     e.g. shift('z', 4) == 'd' and shift(' ', 10) == ' '
    """
    if char.isspace():
        return char
    return letter((integer(char)+amount)%26)

assert shift('z',4) == 'd'
assert shift(' ', 10) == ' '
assert shift('e', 3) == 'h'

def encode(string, amount):
    """
     Encodes the given string by shifting each character with the given amount.
     (Use the function convert_to_string on the result of your use of map(), to get a string again).
    """
    return convert_to_string(map(lambda char: shift(char, amount), string))

assert encode("coding is fun", 3) == "frglqj lv ixq"
assert encode("functional programming", 11) == "qfynetzylw aczrclxxtyr"

"""
The key to crack the Caesar cipher is the observation that some letters of the (English) alphabet appear more often 
than others. By analyzing a large volume of text, the following table of approximate (average) percentage frequencies of the
 26 letters of the alphabet can be derived:
 
[ 8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.2, 0.8, 4.0, 2.4,
  6.7, 7.5, 1.9, 0.1, 6.0, 6.3, 9.1, 2.8, 1.0, 2.4, 0.2, 2.0, 0.1 ]

e.g. the letter 'e' is most frequent, with an average frequency of 12.7%

To guess which shift amount was used, we can compare the frequency table of an encoded string with this general one.
"""

def frequencies(string):
    """
     Return a list with an entry for each letter of the alphabet, containing its frequency in the given string.
     Frequency is defined as the percentage of letters in the string that is equal to that letter.
    """
    counts = [0 for i in range(26)]
    nb_chars = 0
    for char in string:
        if not char.isspace():
            counts[integer(char)] += 1
            nb_chars += 1
    return list(map(lambda x: x/nb_chars*100, counts))

assert frequencies("abbccc dddee deee") == [6.666666666666667, 13.333333333333334, 20.0, 26.666666666666668, 33.33333333333333,
                                          0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                          0.0, 0.0, 0.0, 0.0]

"""
To compare the observed frquencies in the encoded string with the expected average frequencies, we can use the chi-square 
statistic. It is defined as follows: For each two elements Oi and Ei on the same index i of lists O (observed 
frequencies) and E (expected frequencies) we calculate the value (Oi-Ei)**2/Ei and the chi-square is then the sum of all 
these values. The lower the chi-square of two lists, the more similar they are.  
"""

def chisqr(observed, expected):
    """
     Return the chi-square of the two lists. This single number is an indication of how similar the two lists are. The
     lower this number, the more similar the two lists. The chi-square is the sum of all terms (Oi-Ei)**2/Ei for each
     index i.
    """
    return sum(list(map(lambda x,y: (x-y)**2/y, observed, expected)))

frequency_table = [ 8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.2, 0.8, 4.0, 2.4,
                    6.7, 7.5, 1.9, 0.1, 6.0, 6.3, 9.1, 2.8, 1.0, 2.4, 0.2, 2.0, 0.1 ]
assert chisqr(frequencies("kdvnhoo lv ixq"), frequency_table) == 1408.767831479038

def rotate(list, n):
    """
     Return the given list, with its elements rotated n places to the left. You can assume that n will always be smaller
     than the length of the list. e.g. the list [1,2,3] rotated 1 place becomes [2,3,1]
    """
    return list[n:] + list[:n]

assert rotate([1,2,3,4,5], 3) == [4,5,1,2,3]

def crack(encoded_string, reference_table):
    """
     Return the string that is most likely the decoded form of encoded_string. The function calculates the chi-square of
     each possible rotation of the frequency table of encoded_string. The rotation amount that yields the lowest chi-
     square is the shift amount that was most likely used to encode the string. The string is then decoded using this
     value.
    """
    freqs = frequencies(encoded_string)
    chilist = [chisqr(rotate(freqs, n), reference_table) for n in range(26)]
    shift_amount = chilist.index(min(chilist))
    return encode(encoded_string, -shift_amount)

assert crack("vscd mywzboroxcsyxc kbo ecopev", frequency_table) == "list comprehensions are useful"
assert crack("frglqj lv ixq", frequency_table) == "coding is fun"
# crack doesn't always work
assert crack(encode("boxing wizards jump quickly",3), frequency_table) == "wjsdib rduvmyn ephk lpdxfgt"