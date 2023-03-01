# Write a function that returns the minimum amount of coins needed to pay a certain amount of money.
# The amount and a list of possible coin values are given as arguments.
#
# ex. if the list of possible coins is [1,2,5,10] the minimum amount of coins needed to
# pay an amount of 23 cents is 4 (namely 10+10+2+1).
#
# The function assumes a non-zero positive integer for amount and a non-empty coinList
# The function assumes that the given amount can always be paid with the coins from coinList


def minimum_coin(amount, coinList):
    # returns the minimum amount of coins from coinList needed to pay the given amount

    if amount in coinList:
        return 1
    else:
        min_coins = amount

        for coin in coinList:
            if coin <= amount:
                num_coins = 1 + minimum_coin(amount - coin, coinList)
                if num_coins < min_coins:
                    min_coins = num_coins

        return min_coins


# The algorithm above is extremely inefficient and will take long time to finish when using large coinLists.
# One way of reducing calculation time is to store the results for the minimum number of coins in a dictionary
# Then, before computing a new minimum, we first check the dictionary to see if a result is
# already known. See code below.
def minimum_coin_eff(amount, coinList, result_so_far=None):
    # returns the minimum amount of coins from coinList needed to pay the given amount

    if result_so_far is None:
        result_so_far = {}

    if amount in coinList:
        result_so_far[amount] = 1
        return 1
    elif amount in result_so_far:
        return result_so_far[amount]
    else:
        min_coins = amount

        for coin in coinList:
            if coin <= amount:
                numCoins = 1 + minimum_coin_eff(amount - coin, coinList, result_so_far)

                if numCoins < min_coins:
                    min_coins = numCoins
                    result_so_far[amount] = min_coins

        return min_coins


# Tests:
assert minimum_coin(51, [1, 50]) == 2
assert minimum_coin(23, [1, 2, 5, 10]) == 4
assert minimum_coin(80, [5, 20, 50]) == 4

assert minimum_coin_eff(51, [1, 50]) == 2
assert minimum_coin_eff(23, [1, 2, 5, 10]) == 4
assert minimum_coin_eff(80, [5, 20, 50]) == 4

print("minimun_coin_eff(573,[1,2,5,10,20,50,100,500]) = ", end='')
print(minimum_coin_eff(573, [1, 2, 5, 10, 20, 50, 100, 500]))
print("minimun_coin(573,[1,2,5,10,20,50,100,500]) = ... watching and waiting ...", end='', flush=True)
print(minimum_coin(573, [1, 2, 5, 10, 20, 50, 100, 500]))
