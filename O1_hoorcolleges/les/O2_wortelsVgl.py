'''

'''

from math import *

a = float(input('geef a: '))
b = float(input('geef b: '))
c = float(input('geef c: '))

discriminant = b*b - (4*a*c)

if discriminant > 0:
    wortel_1 = (-b + sqrt(discriminant)) / (2*a)
    wortel_2 = (-b - sqrt(discriminant)) / (2 * a)
    print('De reëele wortels zijn :',wortel_1,' en ',wortel_2)
elif discriminant == 0:
    wortel = -b / (2*a)
    print('De reëele wortel is dubbel: ',wortel)
else:
    print('er bestaan geen reëele wortels')
