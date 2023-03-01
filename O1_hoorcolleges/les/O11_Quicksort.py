def partition(lst,low=0,high=None):
    """
      Return the index of an element (called pivot) in the
      slice from high to low of the given list, such that
      (1) all elements in that slice before that index are
      less than the pivot, and (2) such that all elements
      in the slice after that index are greater than or
      equal to the pivot.
      The given slice must have at least one element.
      The function is free to choose any element in the
      slice as the pivot, and accomplishes the partitioning
      by rearranging elements in the given slice.
    """

    index_pivot = low
    index_current = low + 1
    if high is None:
        high = len(lst)

    while index_current < high:

        if lst[index_current] < lst[index_pivot]:                                             # werken met pop is trager
            # lst[index_pivot],lst[index_pivot+1],lst[index_current] = lst[index_current],lst[index_pivot],lst[index_pivot+1]         FOUT
            lst[index_pivot], lst[index_current], lst[index_pivot+1] = lst[index_current], lst[index_pivot+1], lst[index_pivot]
            index_pivot += 1
        index_current += 1


    return index_pivot


# Some tests for the function partition.

lst = [1]
index_pivot = partition(lst)
assert index_pivot == 0

lst = [7,2,0,3,9,5,7,2,3,5,3]
index_pivot = partition(lst)
for i in range(0,index_pivot):
    assert lst[i] < lst[index_pivot]
for j in range(index_pivot,len(lst)):
    assert lst[j] >= lst[index_pivot]





def quicksort(lst,low=0,high=None):
    """
      Sort the elements of the given list in the slice from
      low to high in ascending order.
    """
    if high is None:
        high = len(lst)
    print(lst[low:high])
    if high - low < 2:
        return
    else:
        index_pivot = partition(lst,low,high)
        quicksort(lst,low,index_pivot)
        quicksort(lst,index_pivot+1,high)




# Some tests for the function quicksort.

lst = []
quicksort(lst)
assert lst == []

lst = [3]
quicksort(lst)
assert lst == [3]

lst = [3,-7,6,-4,-11,23,2,0]
quicksort(lst)
assert lst == [-11,-7,-4,0,2,3,6,23]
