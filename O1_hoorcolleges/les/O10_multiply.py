"""
    functie om een vermeningvuldiging uit te rekenen met enkel addite  (mbv recursie)
"""

# stel a en b >= 0

def multiply(a,b):

    if a == 0 or b == 0:
        return 0

    # if a > 1:
    #     return  b + multiply(a-1,b)

    if a > b:
        return a + multiply(a,b-1)
    else:
        return b + multiply(a-1,b)


# geen assumpties voor a en b

def multiply(a,b):

    pass