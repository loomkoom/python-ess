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

from math import *

amount = int(input('aantal gekochte aandelen: '))
price_bought = float(input('prijs van 1 aangekochte aandeel: '))
price_sold = float(input('prijs van 1 verkocht aandeel: '))

if amount < 0 or price_bought < 0 or price_sold < 0:
    print('ERROR ingevoerde data is onmogelijk')
else:
    Saldo = abs(round(-amount*price_bought - 0.02 *(amount*price_bought) + amount*price_sold - 0.015*(amount*price_sold),1))
    Percent = abs(floor(100*(Saldo / (amount*price_bought - 0.02 *(amount*price_bought)))))
    if Saldo < 0:
        print('verlies is: ',Saldo,'or',Percent,'%')
    else:
        print('winst is: ',Saldo,'or',Percent,'%')

