'''
            TIJD: - werkend algoritme 25  minuten

            (geschat: 60 min)

'''
"""
Definitie
Lus invariant
Complexiteit
Correctheid invariant
"""


# VERSIE 1
def split_even_odds(lst1, lst2):
    '''
        Haal oneven uit 1e lijst zet op even in 2e lijst
        Haal even uit 2e lijst zet op oneven in 1e lijst
        andere getallen behouden hun positie
        gelijk aantal even in 1 en oneven in 2
    '''
    i_1 = 0
    i_2 = 0
    i = 0
    oneven_found = False
    even_found = False

    while i_1 < len(lst1) and i_2 < len(lst2):
        if lst1[i_1] % 2 == 0:
            i_1 += 1
        else:
            oneven = lst1[i_1]
            index_oneven = lst1.index(oneven)
            oneven_found = True
        if lst2[i_2] % 2 != 0:
            i_2 += 1
        else:
            even = lst2[i_2]
            index_even = lst2.index(even)
            even_found = True
        if oneven_found and even_found:
            # print("index",index_even,index_oneven)
            # lst2.insert(index_even,oneven)
            # lst2.remove(even)
            # lst1.insert(index_oneven,even)
            # lst1.remove(oneven)

            lst1[index_oneven], lst2[index_even] = lst2[index_even], lst1[index_oneven]
            even_found = False
            oneven_found = False
            i_1 += 1
            i_2 += 1
        i += 1
        print(i)

    return None


# VERSIE 2 (oplossing)
def split_even_odds(lst1, lst2):
    '''
        Haal oneven uit 1e lijst zet op even in 2e lijst
        Haal even uit 2e lijst zet op oneven in 1e lijst
        andere getallen behouden hun positie
        gelijk aantal even in 1 en oneven in 2
    '''
    index1, index2, i = 0, 0, 0
    while index1 < len(lst1) and index2 < len(lst2):
        print("1: ",index1, index2)
        if lst1[index1] % 2 == 0:
            index1 += 1
            print("if even in 1")
        if lst2[index2] % 2 != 0:
            index2 += 1
            print("if odd in 2")
        else:
            print("2: ",index1, index2)
            print("else")
            lst1[index1], lst2[index2] = lst2[index2], lst1[index1]
            index2 += 1
            index1 += 1
#

lst1 = [2, 7, 3, 14]
lst2 = [24, 16, 1, 9]

lst1_after = [2, 24, 16, 14]
lst2_after = [7, 3, 1, 9]

split_even_odds(lst1, lst2)
assert lst1 == lst1_after
assert lst2 == lst2_after
# lus invariant:


# tijdscomplexiteit alle getallen moeten vervangen worden (en lijsten zijn evenlang)
# n keer O(1) ==> O(n)

# correctheidsbewijs
