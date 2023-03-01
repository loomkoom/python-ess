"""Given two strings, write a recursive method that finds the list of longest common subsequence (the longest group
of characters that occur in both strings, in the same order).
For example, the list of longest common subsequences of 'methodiek' and 'katholiek' is ['thoiek']
Note that two strings can have multiple common subsequences. For instance, the longest common subsequences of
'methodiek' and 'ochtendgymnastiek' are ['ediek', 'etiek', 'hdiek', 'mtiek', 'odiek', 'tdiek'] """


def lcs(xstr, ystr):
    """
    Given two strings, this function returns the list of longest common subsequences of both strings
    """
    result = []

    # one of both strings is empty → return an empty string
    if not xstr or not ystr:
        result.append('')
        return result

    xhead, xtail, yhead, ytail = xstr[0], xstr[1:], ystr[0], ystr[1:]

    # current characters match → append the current character to the list of subsequences of both tails
    if xhead == yhead:
        for el in lcs(xtail, ytail):
            result.append(xhead + el)
        return result

    # current characters do not match → return the longest subsequences of (xstr, ytail) and (xtail, ystr)
    else:
        next_results = lcs(xstr, ytail)
        next_results.extend(lcs(xtail, ystr))

        max_length = 0
        for next_result in next_results:
            if len(next_result) > max_length:
                result = [next_result]
                max_length = len(next_result)
            elif len(next_result) == max_length and next_result not in result:
                result.append(next_result)
        return result


assert lcs('aapje', 'banaan') == ['aa']
assert lcs('methodiek', 'katholiek') == ['thoiek']
assert sorted(lcs('methodiek', 'ochtendgymnastiek')) == ['ediek', 'etiek', 'hdiek', 'mtiek', 'odiek', 'tdiek']
