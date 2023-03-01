results_MI = \
    {("Paul", 12), ("Bert", 7), ("Marie", 16), \
     ("Jan", None), ("Lieve", 5)}

# STEP 6
# - Python offers the built-in function map to get the results
#   of applying a given function to each element a given collection.
#   The resulting collection is a list.
# - The higher-order function is said to map a collection of
#   elements to some other collection.
# - Higher-order functions can be applied in succession, i.e. on
#   the collection resulting from another higher-order function.


# Names of all students that were enrolled for the exam.
assert set(map( \
    lambda result: result[0], \
    results_MI)) \
       == {"Marie", "Bert", "Jan", "Paul", "Lieve"}

# Coded results of all students enrolled for the exam.
assert set(map( \
    lambda result: \
        (result[0], "NA") if result[1] is None else
        (result[0], "AAA") if result[1] >= 18 else
        (result[0], "AA") if result[1] >= 16 else
        (result[0], "A") if result[1] >= 14 else
        (result[0], "B") if result[1] >= 12 else
        (result[0], "C") if result[1] >= 10 else
        (result[0], "D") if result[1] >= 8 else
        (result[0], "E") if result[1] >= 6 else
        (result[0], "F"),
    results_MI)) \
       == {("Marie", "AA"), ("Bert", "E"), ("Jan", "NA"), ("Paul", "B"), ("Lieve", "F")}

# Names of all students that passed the exam.
assert \
    set( \
        map( \
            lambda result: result[0],
            filter( \
                lambda result: result[1] is not None and result[1] >= 10, results_MI))) \
    == {"Marie", "Paul"}


# STEP 7
# - Set comprehension and list comprehension are just syntactical
#   shorthands for expressions involving the higher-order functions
#   filter and map.

# Names of all students that passed the exam, using list comprehension.

# assert XXX\
#  == { "Marie", "Paul"}


# STEP 8
# - Self-defined higher order functions may be needed
#   in solving specific problems.

def for_some(condition, collection):
    """
      Check whether at least one of the elements in the
      given collection satisfies the given condition.
    """

    for elem in collection:
        if condition(elem):
            return True
    return False


# Check whether at least one student has a score of 20 using for_some.
assert \
    for_some(lambda result: result[1] is not None and result[1] == 20, results_MI) == False


# Check whether at least one student has a score of 20 using the built-in function
# any and comprehension.

# assert XXX


def do(action, collection):
    """
      Execute the given action on each element of
      the given collection.
      The given collection must be a mutable collection
      of mutable elements.
      The given action must be a function that takes
      a mutable element that changes its content.
    """

    for elem in collection:
        action(elem)

def incr(result):
    if result[1] is not None and result[1] < 20:
        result[1] += 1


# Add 1 to the score of all students, not exceeding a
# maximum of 20, and taking care of students that did
# not take the exam.

# Version 1: explicit function

# Results must now be a mutable list of mutable elements.
results_MI = [["Paul", 12], ["Bert", 7], ["Marie", 20], \
              ["Jan", None], ["Lieve", 5]]

do(incr,results_MI)
assert results_MI == [['Paul', 13], ['Bert', 8], ['Marie', 20], ['Jan', None], ['Lieve', 6]]


# Version 2:  lambda function [Not covered in 2018-2019]

results_MI = [["Paul", 12], ["Bert", 7], ["Marie", 20], \
              ["Jan", None], ["Lieve", 5]]

# do(XXX,results_MI)
# assert results_MI == [['Paul', 13], ['Bert', 8], ['Marie', 20], ['Jan', None], ['Lieve', 6]]
