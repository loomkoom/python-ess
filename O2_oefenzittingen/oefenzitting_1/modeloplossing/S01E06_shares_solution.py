"""
A program that calculates the profit or the loss resulting from
buying and selling shares.

* The program reads the number of shares, the price at which
  a single share was bought and the price at which a single
  share was sold.

* Assume that the user enters numerical values for all three
  input data. However, if the user enters some input that
  makes no sense (negative number of shares, negative prices),
  the program prints a decent error message.

* In buying shares, you have to pay 2% extra on the total amount of
  bought shares. In selling shares, you pay 1.5% of the total price.

* The program prints the profit or loss both as a value and as a
  percentage of the total amount paid at the time of purchase
  (buy commission included). The absolute amount must be rounded
  to at most 2 digits after the decimal point; the percentage may
  not have a decimal fraction.

Some examples:
10 shares bought at 20.53 and sold at 22.64 [Profit is 13.6 or 6%]
20 shares bought at 10.07 and sold at 9.73 [Loss is 13.75 or 7%]
-4 shares [Error message]
4 shares bought at -12.45 [Error message]
4 shares bought at 12.45 and sold at -11.67 [Error message]
"""

nb_shares = int(input("Enter the number of shares: "))
buy_price = float(input("Enter the buy price: "))
sell_price = float(input("Enter the sell price: "))

BUY_COMMISSION = 0.02
SELL_COMMISSION = 0.015

if nb_shares < 0:
    print("Enter a valid number of shares")
elif buy_price <= 0:
    print("Buy price should be strict positive")
elif sell_price <= 0:
    print("Sell price should be strict positive")
else:
    paid = (nb_shares * buy_price) * (1 + BUY_COMMISSION)
    received = (nb_shares * sell_price) * (1 - SELL_COMMISSION)

    profit = received - paid
    profit_percentage = int(round(profit * 100 / paid, 0))

    if profit < 0:
        msg = "Loss"
    else:
        msg = "Profit"

    print(msg, "is", abs(round(profit,2)), "or", abs(profit_percentage),"%")

