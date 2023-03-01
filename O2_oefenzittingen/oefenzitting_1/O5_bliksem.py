"""
Calculate the distance of lightning when given the delay between 
the lightning strike and the thunder. If the storm is too close, 
within 1 km, the program should warn you to unplug all appliances.

 * The time is given in seconds, and should be a decimal number
 * The speed of sound is 343 m/s
 * Print the distance in kilometer and meter
 * Print an optional warning message if the storm is too close
 * Make sure the time is positive

Verify your program:
 t = 1          | 0 km and 343 meter + [Warning message]
 t = -1         | [Error message]
 t = 10         | 3 km and 430 meter
 t = 2.9        | 0 km and 994 meter + [Warning message]
 t = 3          | 1 km and 29 meter
"""
from math import floor

delay = float(input('tijd tussen geluid in seconden: '))

if delay < 0.0 :
    print('error message')
else:
    afstand = delay * 343.0
    kilometers = floor(afstand // 1000)
    meters = floor(afstand - kilometers*1000)
    if afstand < 1000:
        print(kilometers,'km',meters,'meter','WARNING')
    else:
        print(kilometers,'km',meters,'meter')