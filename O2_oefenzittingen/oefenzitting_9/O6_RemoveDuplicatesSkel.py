def remove_duplicates(lst):
    """ Remove all duplicates from the given list.
    If an element occurs several times in the original list, all
    occurrences are removed, except for the leftmost occurrence. """
    index = 0
    lst.reverse()
    while index != len(lst):
        # INVARIANT het gegeven element komt maar 1 keer of niet voor in het behandelde deel tot nu toe
        # INVARIANT alle elementen tot nu toe zijn verschillend
        assert list.count(lst[:index],lst[index-1]) <= 1
        assert all(list.count(lst[:k],lst[k-1]) <= 1 for k in range(index))
        if lst.count(lst[index]) > 1:
            del lst[index]
        else:
            index += 1

    lst.reverse()

    print(lst)

def remove_duplicates(lst):
    """ Remove all duplicates from the given list.
    If an element occurs several times in the original list, all
    occurrences are removed, except for the leftmost occurrence. """
    index = 0
    while index != len(lst):
        # INVARIANT alle elementen tot nu toe zijn verschillend
        assert all([lst[k] != lst[j] for k in range(0,index) for j in range(k+1,index)])
        if lst.index(lst[index]) < index:
            del lst[index]
        else:
            index += 1

    print(lst)

##TESTS
# empty list
lst = []
lst_id = id(lst)
remove_duplicates(lst)
assert (lst_id == id(lst)) and (lst == [])
# list with 1 element
lst = [20]
lst_id = id(lst)
remove_duplicates(lst)
assert (lst_id == id(lst)) and (lst == [20])
# list with duplicates
lst = [2, 3, 2, 5, 2, 3, 7]
lst_id = id(lst)
remove_duplicates(lst)
assert (lst_id == id(lst)) and (lst == [2, 3, 5, 7])
# list with duplicate element at the end
lst = [2, 3, 2, 5, 2, 3, 7, 2]
lst_id = id(lst)
remove_duplicates(lst)
assert (lst_id == id(lst)) and (lst == [2, 3, 5, 7])
# list with all duplicate elements
lst = [10, 10, 10, 10, 10, 10]
lst_id = id(lst)
remove_duplicates(lst)
assert (lst_id == id(lst)) and (lst == [10])

# CORRECTNESS
# BASE CASE
# Given: ...
# To prove: ...


# INDUCTION STEP
# Given: ...
# To prove: ...

# EPILOGUE
# Given: ...
# To prove: ...



# CORRECTNESS
# The assertion no_duplicates(lst,i) denotes the fact that all elements
# in the given list up to position i are different from each other.
#BASE CASE
# Given: index == 1
# To prove: no_duplicates(lst,index)
#    The handled portion of the list consists of 1 element if the original
#    list is not empty. In that case, the assertion is satsfied in a trivial way.
#    If the given list is empty, there is no element at position 0, and the
#    assertion is satisfied again


#INDUCTION STEP: Case 1: Duplicate element at index
# Denote value of index at the start of the body as index'
# Given: no_duplicates(lst,index') and (index' < len(lst))
# To prove: no_duplicates(lst,index)
#   - Case 1: The element at index' is already in the handled portion of
#     the list. In that case that element is removed. The index remains
#     unchanged in this case, which means that the loop invariant is satisfied.
#   - Case 2: The element at index' is no in the handled portion of the
#     list. Combined with the induction hypothesis, this yields
#     no_duplicates(lst,index'+1). The index is subsequently incremented,
#     meaning that index == index'+1. This proofs the loop invariant.

#EPILOGUE
# Given: no_duplicates(lst,index)) and (index >= len(lst))
# To prove: no_duplicates(lst,len(lst)))
#   We must prove that index == len(lst) upon completing the while statement.
#   This can be done by adding an extra statement to the loop invariant. We leave
#   that part of the proof to the reader.
