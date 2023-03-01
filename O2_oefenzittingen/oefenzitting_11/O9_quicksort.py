def partition(lst, low = 0, high = None):
    """
    Return the index of an element (called pivot) in the
    slice from high to low of the given list, such that
    (1) all elements in that slice before that index are
    less than the pivot, and (2) such that all elements
    in the slice after that index are greater than or
    equal to the pivot.
    –	The given slice must have at least one element.
    –	The function is free to choose any element in the
    slice as the pivot, and accomplishes the
    partitioning by rearranging elements in the given
    slice.
    """
    if high == None:
        high = len(lst)
    pivot = (low + high) // 2

    # Move the pivot to the start of the list.
    lst[pivot], lst[low] = lst[low], lst[pivot]
    pivot = low

    for index in range(low + 1, high):
        if lst[index] < lst[pivot]:
            element_at_index = lst[index]
            lst[index] = lst[pivot + 1]
            lst[pivot + 1] = lst[pivot]
            lst[pivot] = element_at_index
            pivot += 1
    return pivot


def quicksort(lst, low = 0, high = None):
    '''
    Sort the elements of the given list in the slice from
    low to high in ascending order.
    '''
    if high == None:
        high = len(lst)
    if low < high - 1:
        # The slice lst[low:high] has at least 2 elements.
        index_of_pivot = partition(lst, low, high)
        quicksort(lst, low, index_of_pivot)
        quicksort(lst, index_of_pivot + 1, high)


# Some tests for the function quicksort.
lst = []
quicksort(lst)
assert lst == []

lst = [3]
quicksort(lst)
assert lst == [3]

lst = [3, -7, 6, -4, -11, 23, 2, 0]
quicksort(lst)
assert lst == [-11, -7, -4, 0, 2, 3, 6, 23]

'''
Comments:

Worst case: 

Best case: 
'''
### Measurements
import time
import random
import matplotlib.pyplot as plt

measurements_worst = []
measurements_best = []
measurements_average = []
for n in range(1, 1000, 50):
    # worst case: all the same: pivot will be at the very beginning each time
    lst = [1 for i in range(n)]
    start = time.perf_counter_ns()
    quicksort(lst)
    end = time.perf_counter_ns()
    measurements_worst.append(end - start)

    # best case
    # already (strictly) ordered list -> pivot will divide range nicely in 2 every time
    lst = [i for i in range(n)]
    start = time.perf_counter_ns()
    quicksort(lst)
    end = time.perf_counter_ns()
    measurements_best.append(end - start)

    # average
    # already (strictly) ordered list -> pivot will divide range nicely in 2 every time
    lst = [random.randint(0, n) for i in range(n)]
    start = time.perf_counter_ns()
    quicksort(lst)
    end = time.perf_counter_ns()
    measurements_average.append(end - start)

plt.title("Quicksort")

plt.plot(measurements_best, label = "best case")
plt.plot(measurements_average, label = "average case")
plt.plot(measurements_worst, label = "worst case")

plt.legend()
plt.show()
