# all equal , ascending , descending , unordered
# bekijk per element en check de mogelijkheden : schrap en neem de overblijvende tot alles gecontroleerd is

ALL_EQUAL  = 0
ASCENDING  = 1
DESCENDING = 2
UNORDERED  = 3

def get_sorting(*values):

    '''
        ...
    '''

    huidige_pos = 0
    all_equal = True            # kleine letters! onafhankelijk
    ascending = True
    descending = True

    while (huidige_pos < len(values)-1) and (all_equal or ascending or descending):     # verder gaan als er nog een mogelijkheid niet geschrapt is

        # if values[huidige_pos] != values[huidige_pos + 1]:
        #     all_equal = False
        if values[huidige_pos] < values[huidige_pos + 1]:
            descending = False
            all_equal = False
        if values[huidige_pos] > values[huidige_pos + 1]:
            ascending = False
            all_equal = False

        huidige_pos += 1

    if all_equal:
        return ALL_EQUAL
    elif ascending:
        return ASCENDING
    elif descending:
        return DESCENDING
    else:
        return UNORDERED


assert get_sorting(3,3,3) == ALL_EQUAL
assert get_sorting(1,2,3) == ASCENDING
assert get_sorting(3,2,1) == DESCENDING
assert get_sorting(1,4,3) == UNORDERED
