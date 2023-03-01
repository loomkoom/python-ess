"""
A program that reads a number of seconds, and displays it as a number of
hours, a number of minutes and a number of seconds.

* Input may not be negative
* Output is of the format: hours:minutes:seconds
* Output hours will range between 0 and 23

Some example outputs for given inputs:
12457   3 : 27 : 37
0       0 : 0 : 0
86399   23 : 59 : 59
86400   0 : 0 : 0
1000000 13 : 46 : 40
"""

tijd_seconden = int(input("geef de tijd in seconden: "))


uren = tijd_seconden // 3600
minuten = (tijd_seconden - uren*3600) //60
seconden = tijd_seconden -uren*3600 - minuten*60

if tijd_seconden == 86400:
    uren = 0
    seconden = 0
    minuten = 0
elif tijd_seconden > 86400:
    uren =(tijd_seconden // 3600) % 24

print(uren,minuten,seconden,sep=':')