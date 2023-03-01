# vierkantswortel berekenen vanuit approximatie via algoritme

PRECISIE = 1.0E-15                                             # cte benoemen en verder symbolisch gebruiken ( symbolische constante)

getal = float(input("geef getal: "))
benadering = 1.0                                                # of random() willekeurig getal tussen a en b

# while abs(getal - benadering ** 2) >= PRECISIE:                 # loopt soms vast omdat de precisiefout van floating point getallen te groot kan worden (bv E.0E-100)
                                                                  # => abs vs rel nauwkeurigheid  (ben/getal) <= 1.0E-15 => 15 cijfers na komma
while (abs(getal-benadering**2)/getal) >=PRECISIE :
    benadering = (benadering + (getal / benadering)) / 2.0
    print(benadering)

print("vierkantswortel van ", getal, "=", benadering)


# extra oef bepaal de mantissa van een binait getal => algoritme deel get al groter dan 2^x => bit =1 kleiner => bit = 0
