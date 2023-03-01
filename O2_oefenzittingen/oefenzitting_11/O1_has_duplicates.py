"""
Below you find five different versions of an algorithm that checks whether a list contains duplicates.
Analyze their time complexity for both the best and worst cases, and perform measurements to check your answer.

Also, compare the worst cases of version 1 and 2; what do you expect? Do your measurements confirm this?
"""
import time


def has_duplicates_v1(lst):
    for i in range(len(lst)):  # O(n) # O(1)
        for j in range(len(lst)):  # O(n) # O(1)
            if i != j and lst[i] == lst[j]:  # O(1) # O(1)
                return True
    return False


# best case eerste 2 zijn duplicates:       O(1)
# worst case geen duplicaten                O(n^2)


###############################################################################


def has_duplicates_v2(lst):
    for i in range(len(lst)): # O(n) # O(1)
        for j in range(i + 1, len(lst)): # O(n) # O(1)
            if lst[i] == lst[j]: # O(1) # O(1)
                return True
    return False


# best case eerste 2 zijn duplicates:       O(1)
# worst case geen duplicaten                O(n^2)

###############################################################################


def has_duplicates_v3(lst):
    found_duplicate = False
    i = 0
    while i != len(lst): # O(n) # O(n)
        if lst.count(lst[i]) > 1: # O(n) # O(n)
            found_duplicate = True
        i += 1
    return found_duplicate


# best case = worst  O(n^2)

###############################################################################


def has_duplicates_v4(lst):
    for i in range(len(lst)):  # O(n) # O(1)
        if lst[i] in lst[i + 1:]:  # O(n) # O(n)
            return True
    return False


# best case: eerste 2 elementen duplicate   O(n)
# worst case: geen duplicaten               O(n^2)


###############################################################################


def has_duplicates_v5(lst):
    already_seen = {}
    for x in lst:  # O(n) O(2)
        if x in already_seen:  # O(1) O(1)
            return True
        already_seen[x] = True  # O(1) O(1)
    return False

lst1 = [1,2,3,4,5]
has_duplicates_v5(lst1)


# best case: eerste 2 elementen duplicate   O(1)
# worst case: geen duplicaten               O(n)
