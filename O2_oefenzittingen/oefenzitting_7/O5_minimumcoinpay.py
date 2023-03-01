# Write a function that returns the minimum amount of coins needed to pay a certain amount of money.
# The amount and a list of possible coin values are given as arguments.
#
# ex. if the list of possible coins is [1,2,5,10,20,50] the minimum amount of coins needed to
# pay an amount of 67 cents is 4 (namely 50+10+5+2).
#
#  The function assumes a non-zero positive integer for amount and a non-empty coinList
#  The function assumes that the given amount can always be paid with the coins from coinList


def minimum_coin(amount, coinList):
    if amount == 0:
        return 0
    best = None

    for coin in coinList:
        if coin <= amount:
            current_solution = 1 + minimum_coin(amount - coin, coinList)
            if best is None or current_solution <= best:
                best = current_solution
    return best


# Tests:
assert minimum_coin(51, [1, 50]) == 2
assert minimum_coin(23, [1, 2, 5, 10]) == 4
assert minimum_coin(20, [5, 20, 50]) == 1
assert minimum_coin(60, [1, 20, 50]) == 3
