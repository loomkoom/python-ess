'''

'''

uren     = int(input('geef uren: '))
minuten  = int(input('geef minuten: '))
seconden = int(input('geef seconden: '))

if seconden >= 59:
    seconden = 0
    minuten += 1
    if minuten >= 59:
        minuten = 0
        uren += 1
        if uren >= 24:
            uren = 0
else:
    seconden += 1

print(uren,minuten,seconden,sep=' : ')