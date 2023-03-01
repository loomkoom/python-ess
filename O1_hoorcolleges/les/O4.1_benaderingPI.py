"""
write a function to calculate an approcimation of pi
...

opp cirkel/opp vierkant = hits/totaal

def functie ( Backer Nauer notatie.
vierkante haakjes optioneel
"""

# def f(x=2,y,z="abc"):                                  # enkel laatste parameters van functie kunnen defaultwaarde hebben


from random import *
from math import *

def benadering_pi(gevraagd_aantal_worpen = 1000):       # neemt deze verzuimwaarde in het geval dat je geen waarde meegeeft, berekend maar 1 keer dus random bv wordt dus elke keer hetzelfde getal

    '''
      Geeft een benadering terug voor de constante PI.

        - De benadering wordt beter met een stijgend aantal worpen
        - De benadering zal niet altijd gelijk zijn voor een gelijk aantal worpen
    '''

    aantal_rake_worpen = 0
    totaal_aantal_worpen = 0

    while totaal_aantal_worpen < gevraagd_aantal_worpen:        # vierkant -1 --> +1 en afstand berekenen tot middelpunt 0 => cirkel straal 1

        x = random() * 2.0 - 1
        y = random() * 2.0 - 1

        if sqrt(x*x+y*y) <= 1:
            aantal_rake_worpen += 1

        totaal_aantal_worpen += 1

    return (4.0 * aantal_rake_worpen) / (totaal_aantal_worpen)

print(benadering_pi(10000000))


