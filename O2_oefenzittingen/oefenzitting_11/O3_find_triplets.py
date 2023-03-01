"""
Write a program that takes a list of integer numbers as input.
Determine the number of sets of 3 items from the list, that sum to 0.

E.g. if the list = [5, -2, 4 , -8, 3], then there is one such triplet: 5 + (-8) + 3 = 0.
For larger lists, the number of triplets probably will be much higher.

If the list would contain a value more than once, count a triplet for each item with this value.
E.g. the list [5, -2, 4, 3, -8, 3] will have two triplets:
  5 + 3 + (-8) = 0 (with value 3 from position 3) and
  5 + (-8) + 3 = 0 (with value 3 from the last position in the list)

What is the time complexity of your algorithm?

Suppose your algorithm works in time T(n) = a*n^b, then you can easily derive that T(2n)/T(n) = 2^b.
Measure T(n) and T(2n) for some value of n, and use these measurements to estimate the exponent b for your algorithm.
"""
import time
import math
import random


def find_triplets(seq):
    triplets = 0
    for i in range(len(seq)):                       # O(n)
        for j in range(i + 1, len(seq)):            # O(n)
            for k in range(j + 1, len(seq)):        # O(n)
                if seq[i] + seq[j] + seq[k] == 0:   # O(1)
                    triplets += 1                   # O(1)
    return triplets


assert find_triplets([]) == 0  # At least 3 items required
assert find_triplets([3, -3]) == 0  # At least 3 items required
assert find_triplets([1, -1, 0]) == 1  # Trivial case
assert find_triplets([2, -1, -1]) == 1  # Trivial case
assert find_triplets([5, -2, 4, -8, 3]) == 1
assert find_triplets([3, -2, 2, 0, -1, -5]) == 3
assert find_triplets([4, -2, 0, 2, -1, -2, -1, -4, 3, -6, 5, -9]) == 13

N1 = 400
N2 = 800
lst1 = [random.randint(0, N1) for k in range(0, N1)]
lst2 = [random.randint(0, N2) for k in range(0, N2)]

start1 = time.perf_counter_ns()
find_triplets(lst1)
stop1 = time.perf_counter_ns()
time_elapsed1 = stop1 - start1
print(time_elapsed1)

start2 = time.perf_counter_ns()
find_triplets(lst2)
stop2 = time.perf_counter_ns()
time_elapsed2 = stop2 - start2
print(time_elapsed2)

b = math.log2(time_elapsed2 / time_elapsed1)
print(b)
# b is 3
# T(n) = a*n^(3)
# T(n) = O(n^3)
# --> klopt met 3 for loops = O(n) * O(n) * O(n)
#                           = O(n^3)
