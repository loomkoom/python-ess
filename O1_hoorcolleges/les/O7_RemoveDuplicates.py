# alle dubbele voorkomens van een warde verwijden en het meest linkse voorkomen te behouden
# veronderstel dat een deel geen dubbels heeft en kijk telkens een stap verder
#
# cfr inductie bewijs   ( n-1 ==> n )

def remove_duplicates(lst):

    '''

    '''

    volgende_pos = 1

    while volgende_pos < len(lst):

        if list.index(lst,lst[volgende_pos]) == volgende_pos:        # als het eerste voorkomen de volgende positie is (getal behouden)

            volgende_pos += 1
        else:                                                       # eerste voorkomen zit ervoor ==> verwijder het voorkomen op volgende positie

            del lst[volgende_pos]
           # list.remove(lst,lst[volgende_pos])                     # alternatieven
           # list.pop(volgende_pos)
           # list.pop(lst,volgende_pos)
           # lst[volgende_pos:volgende_pos + 1] = []

def remove_duplicates(lst):                                          #van rechts naar links en met objectgerichte stijl en for statement

    for volgende_pos in range(len(lst)-1 ,0 , -1):                  # +=1 is niet meer nodig door for statement
            #del lst[volgende_pos]

        if lst.index(lst[volgende_pos]) != volgende_pos:

            lst.pop(volgende_pos)
            # list.remove(lst,lst[volgende_pos])                     # alternatieven
            # list.pop(lst,volgende_pos)
            # lst[volgende_pos:volgende_pos + 1] = []









# empty list
lst = []
remove_duplicates(lst)
assert lst == []

# list with 1 element
lst = [20]
remove_duplicates(lst)
assert lst == [20]

# list with duplicates
lst = [2,3,2,5,2,3,7]
remove_duplicates(lst)
assert lst == [2,3,5,7]

# list with duplicate element at the end
lst = [2,3,2,5,2,3,7,2]
remove_duplicates(lst)
assert lst == [2,3,5,7]

# list with duplicate element at the start
lst = [2,2,3,5,2,3,7,2]
remove_duplicates(lst)
assert lst == [2,3,5,7]

# list with all duplicate elements
lst = [10,10,10,10,10,10]
remove_duplicates(lst)
assert lst == [10]

