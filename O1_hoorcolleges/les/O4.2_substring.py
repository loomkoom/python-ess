def pos_meest_linkse_voorkomen(str,substring,start=0,end=None):         # end=0 ipc len(str) omdat in de def enkel constanten kunnen voorkomen (niet symbolisch)

    '''


    '''

    volgende_positie = 0
    resultaat = None

    while (volgende_positie < end -len(substring)+1) and (resultaat == None) :
            # and statement kan weg
        if substring == str[volgende_positie : volgende_positie + len(substring)]:
            resultaat = volgende_positie                                                            # geeft meest rechtse voorkomen van de string door extra voorwaarde meest links
            # return volgende_positie
       volgende_positie += start

    return resultaat
    # return None


assert pos_meest_linkse_voorkomen("peeters","eet") == 1
assert pos_meest_linkse_voorkomen("peeters","aat") == None
assert pos_meest_linkse_voorkomen("peeters","peet") == 0
assert pos_meest_linkse_voorkomen("peeters","ers") == 4
assert pos_meest_linkse_voorkomen("peeters","") == 0

# print(pos_meest_linkse_voorkomen(substring = "abc", str = "peeters", start= 3))
# print(pos_meest_linkse_voorkomen("peeters", end = 5, substring= "eet"))



""" TESTEN via assert

1) substring helemaal vooraan
2) substring helemaal achteraan
3) substring komt niet voor
4) substring is leeg 
5) substring groter dan string
...

"""