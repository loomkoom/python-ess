def nb_occurences(element,sequence):

    """
      A function that counts the number of occurrences of a given element in a given sequence.
      The function must accept the element as its first argument and the sequence as its second argument.
      The function must always return an integer value.

      Some example outputs for given inputs:
      20,()                   0
      20,(1,6,11,50)          0
      20,(20,40,20,100,20)    3
    """

    occurence = 0

    for index in range(len(sequence)):
        if element == sequence[index]:
            occurence += 1

    return occurence

def nb_occurences2(elem,seq):
    return seq.count(elem)





# TESTS
assert nb_occurences(20,()) == 0
assert nb_occurences(20,(1,6,11,50)) == 0
assert nb_occurences(20,(20,40,20,100,20)) == 3

# TESTS
assert nb_occurences2(20,()) == 0
assert nb_occurences2(20,(1,6,11,50)) == 0
assert nb_occurences2(20,(20,40,20,100,20)) == 3
