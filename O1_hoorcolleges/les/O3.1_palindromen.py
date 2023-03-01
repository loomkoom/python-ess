#...

tekst = input("geef de tekst: ")
volgende_positie = 0
nog_palindroom = True

while (volgende_positie <= len(tekst)/2 - 1) and nog_palindroom:
    if tekst[volgende_positie] == tekst[-volgende_positie-1]:
        nog_palindroom = True
    else:
        nog_palindroom = False

    volgende_positie +=1
    print(volgende_positie,nog_palindroom)

if nog_palindroom:
    print(tekst, 'is een palindroom')
else:
    print(tekst,'is GEEN palindroom')
