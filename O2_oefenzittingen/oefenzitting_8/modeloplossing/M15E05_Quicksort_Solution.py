def quicksort(compare, lst):
    """
    Returns a new list `result' with the same elements as 
    the given list such that 
    compare(result[i],result[i+1]) <= 0 for all i. 
    """
    if len(lst) < 2:
        return lst
    pivot = lst[0]
    rest  = lst[1:]
    left  = list(filter(lambda x: compare(x,pivot) <= 0, rest))
    right = list(filter(lambda x: compare(x,pivot) > 0,  rest))
    return quicksort(compare,left) + [pivot] + quicksort(compare,right)

def is_sorted(compare, lst):
    """
    Checks if the given list is sorted according to the given compare function.
    """
    return all(compare(lst[i],lst[i+1])<=0 for i in range(0,len(lst)-1))

def is_permutation(lst1, lst2):
    """
    Checks whether the two given lists are permutations of each other
    """
    from collections import Counter
    return Counter(lst1) == Counter(lst2)
	
compare1 = lambda x,y: abs(x) - abs(y)
list1 = range(-10,10)
sorted1 = quicksort(compare1, list1)
assert is_sorted(compare1, sorted1)
assert is_permutation(list1, sorted1)

compare2 = lambda x,y: x%10 - y%10
list2 = range(0,100,7)
sorted2 = quicksort(compare2, list2)
assert is_sorted(compare2, sorted2)
assert is_permutation(list2, sorted2)