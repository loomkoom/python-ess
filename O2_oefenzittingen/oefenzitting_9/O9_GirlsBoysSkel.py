#! Auxiliary function to inspect the sign of some number.
def sign(x):
    """  Return the sign of the given number.
    +1 is returned if the given number is positive;
    0 if it is zero and -1 if it is negative."""
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return +1

##TESTS
# Negative number
assert sign(-4) == -1
# Zero number
assert sign(0) == 0
# Positive number
assert sign(+4) == +1
                                


def arrange_in_couples(lst):
    """ Rearrange the given list of girls and boys such that each boy is
    coupled to a girl. The given list must have as many boys as girls.
    Boys are represented by negative integer numbers;
    girls by positive integer numbers. For some couples, the girl may come
    first; for others the boy. """
    pass

##TESTS
# List with 4 elements not in order
lst = [3, 4, -5, -7]
arrange_in_couples(lst)
assert (lst == [3,-5,4,-7]) or (lst == [3,-5,-7,4]) or\
   (lst == [3,-7,4,-5]) or (lst == [3,-7,-5,4]) or\
   (lst == [4,-5,3,-7]) or (lst == [4,-5,-7,3]) or\
   (lst == [4,-7,3,-5]) or (lst == [4,-7,-5,3])
# List with 2 elements
lst = [3,-4]
arrange_in_couples(lst)
assert (lst == [3,-4]) or (lst == [-4,3])
# Empty list
lst = []
arrange_in_couples(lst)
assert len(lst) == 0



## CORRECTNESS

#BASE CASE
# Given: ...
# To prove: ...


#INDUCTION STEP
# Given: ...
# To prove: ...

#EPILOGUE
# Given: ...
# To prove: ...
