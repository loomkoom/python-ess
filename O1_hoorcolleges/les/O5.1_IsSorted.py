# tuple getallen invoer
# gesorteerd of niet gesorteerd output
# alternatief : stijgend , dalend , gelijk of geen volgorde

#def is_sorted(sequence):
def is_sorted(*values):

    '''
        ...
    '''

    volgende_pos = 1                # of huidige pos

#    while volgende_pos < len(sequence):
    while volgende_pos < len(values):

       # if(sequence[volgende_pos-1] > sequence[volgende_pos]):
        if(values[volgende_pos-1] > values[volgende_pos]):
            return False
        volgende_pos += 1

    return True

assert is_sorted(1,6,9,23,456,789)         # gwn assert voor == true
assert not is_sorted(3,4,6,2,10)            # not ipv == false
assert not is_sorted(1,5,9,789,3)
assert not is_sorted(10, -2, 6, 20 ,36)
assert is_sorted(33,)
assert is_sorted()

# dubbelle haakjes is nodig bij sequence
# bij *value moet je enkel de sequentia van getallen geven en wordt het automatisch een tuple



''' TEST

gesorteerd
niet gesorteed
eerste 2 elementen niet gesorteerd
laatste 2 elementen niet gesorteerd
string met lengte 1
string met lengte 0

'''