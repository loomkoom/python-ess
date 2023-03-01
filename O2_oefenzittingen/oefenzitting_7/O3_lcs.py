"""
Given two strings, write a recursive method that finds the list of longest common subsequence (the longest group of characters that occur in both strings, in the same order)
For example, the list of longest common subsequences of 'methodiek' and 'katholiek' is ['thoiek']
Note that two strings can have multiple common subsequences. For instance, the longest common subsequences of 'methodiek' and 'ochtendgymnastiek' are ['ediek', 'etiek', 'hdiek', 'mtiek', 'odiek', 'tdiek']
"""


def lcs(xstr, ystr):
    """
    Given two strings, this function returns the list of longest common subsequences of both strings
    """

    substring = []

    # if len(xstr) <= 0 or len(ystr) <= 0:
    if not xstr or not ystr:
        substring.append("")
        print("if not",substring)
        return substring

    xhead, xtail, yhead, ytail = xstr[0], xstr[1:], ystr[0], ystr[1:]

    if xhead == yhead:
        for elem in lcs(xtail, ytail):
            substring.append(xhead + elem)
        print("if",substring)
        return substring

    else:
        next_results = lcs(xstr, ytail)
        next_results.extend(lcs(xtail, ystr))

        max_length = 0
        for next_result in next_results:
            if len(next_result) > max_length:
                substring = [next_result]
                max_length = len(next_result)
            elif len(next_result) == max_length and next_result not in substring:
                substring.append(next_result)
        print("else",substring)
        return substring
assert lcs('aapje', 'banaan') == ['aa']
#assert lcs('methodiek', 'katholiek') == ['thoiek']
#assert sorted(lcs('methodiek', 'ochtendgymnastiek')) == ['ediek', 'etiek', 'hdiek', 'mtiek', 'odiek', 'tdiek']
