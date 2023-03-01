"""
Write an iterative program that, given a number n,
generates a list of all ascending sequences of numbers from 1 up to (and including) n.

We define an ascending sequence as a (possibly empty) tuple of numbers,
where the elements in the tuple are ordered from small to large and each number occurs at most once.

For example, the ascending sequences for the number 3 are
 () (the empty tuple), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), and (1, 2, 3).


(1) Analyze the time complexity of your algorithm.
(2) Measure and plot the time it takes for n <= 20, and compare to your analysis.
(3) Predict the time your algorithm would take for n=22, n=25, n=30, and n=50, and verify your predictions.
"""


def ascending_sequences(n):
    seq = [()]

    for i in range(1, n + 1):   # O(n)
        new_elms = []
        for elem in seq:        # O(n)
            new_elms.append(elem + (i,))    # O(1)
        seq.extend(new_elms)    # O(len(new_elms))
    return seq

    # tup = ()
    # i = 1
    # while i <= n:
    #     tup += (i,)
    #     seq.append(tup)
    #     if i == n and (n,) not in seq:
    #         tup = ()
    #         i = n-1
    #     i += 1
    # print(seq)
    # return seq


# assert sorted(ascending_sequences(0)) == [()]
# assert sorted(ascending_sequences(1)) == [(), (1,)]
# assert sorted(ascending_sequences(2)) == [(), (1,), (1, 2), (2,)]
assert sorted(ascending_sequences(3)) == [(), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)]
