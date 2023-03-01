"""
Given two strings, write a recursive method that finds the list of longest common subsequence (the longest group of characters that occur in both strings, in the same order)
For example, the list of longest common subsequences of 'methodiek' and 'katholiek' is ['thoiek']
Note that two strings can have multiple common subsequences. For instance, the longest common subsequences of 'methodiek' and 'ochtendgymnastiek' are ['ediek', 'etiek', 'hdiek', 'mtiek', 'odiek', 'tdiek']
"""


def lcs(xstr, ystr):
    """
    Given two strings, this function returns the list of longest common subsequences of both strings
    """
    pass


assert lcs('aapje', 'banaan') == ['aa']
assert lcs('methodiek', 'katholiek') == ['thoiek']
assert sorted(lcs('methodiek', 'ochtendgymnastiek')) == ['ediek', 'etiek', 'hdiek', 'mtiek', 'odiek', 'tdiek']
