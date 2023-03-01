#! STEP 1
# ! Generalize the function into a higher-order function
# ! get_results_satisfying such that any condition can be
# ! specified that all exam results in the resulting set
# ! must satisfy.

def get_students_satisfy(condition, results):
    """
      Return the subset of the given set of results that
      satisfy the stated condition.
        - The given results are presented as a set of tuples
          that start with the name of the student followed by
          his/her grade.
        - The grade is an integer in the range from 0 to 20.
          Students that did not take the exam have None as
          their grade.
    """

    # ! The code below is a copy of the body of the
    # ! non-generalized function.

    students_satisfying = set()

    # INVARIANT
    #  The set of passed students contains all students
    #  handled so far that have a grade not below 10.
    for result in results:

        if condition(result):
            set.add(students_satisfying, result)

    return students_satisfying


# ! STEP 2
# ! Invoke the function get_results_satisfying by supplying
# ! different conditions.


results_MI = {("Paul", 12), ("Bert", 7), ("Marie", 16), ("Jan", None), ("Lieve", 4)}


# ! Calculate the set of all students that have passed
# ! the exam for MI.

def has_passed(result):
    _, score = result

    return score is not None and score >= 10


assert get_students_satisfy(has_passed, results_MI) \
       == {("Marie", 16), ("Paul", 12)}


# ! Calculate the set of all students that have not passed
# ! the exam for MI (not including students that did not take
# ! the exam.

def has_not_passed(result):
    _, score = result

    return score is not None and score < 10


assert get_students_satisfy(has_not_passed, results_MI) \
       == {("Bert", 7), ("Lieve", 4)}


# ! Calculate the set of all students whose name is at least
# ! 5 characters long, and that obtained an even score on
# ! the exam for MI.

def has_long_name_and_even_score(result):
    name, score = result

    return len(name) >= 5 and score is not None and score % 2 == 0


assert get_students_satisfy(has_long_name_and_even_score, results_MI) \
       == {("Marie", 16), ("Lieve", 4)}

# ! STEP 3
# !  Use the built-in function filter instead of the generalized
# !  function get_results_satisfying.
# !  The only difference is that filter returns an iterator whereas
# !  get_results_satisfying returns a set.


results_MI = {("Paul", 12), ("Bert", 7), ("Marie", 16), ("Jan", None), ("Lieve", 4)}

# ! Calculate the set of all students that have passed
# ! the exam for MI.


assert set(filter(has_passed, results_MI)) \
       == {("Marie", 16), ("Paul", 12)}

# ! Calculate the set of all students that have not passed
# ! the exam for MI (not including students that did not take
# ! the exam.


assert set(filter(has_not_passed, results_MI)) \
       == {("Bert", 7), ("Lieve", 4)}

# ! Calculate the set of all students whose name is at least
# ! 5 characters long, and that obtained an even score on
# ! the exam for MI.


assert set(filter(has_long_name_and_even_score, results_MI)) \
       == {("Marie", 16), ("Lieve", 4)}

# STEP 4
# - We want a more flexible instrument to pass functions as arguments
#   to higher-order functions.
# - Lambda functions are anonymous functions that can be defined and
#   used on the spot.


results_MI = {("Paul", 12), ("Bert", 7), ("Marie", 16), ("Jan", None), ("Lieve", 4)}

# All results with a score of 10 or more.
assert set(filter(lambda result: result[1] is not None and result[1] >= 10, results_MI)) \
       == {("Marie", 16), ("Paul", 12)}

# All results with a score less than 10.
assert set(filter(lambda result: result[1] is not None and result[1] < 10, results_MI)) \
       == {("Bert", 7), ("Lieve", 4)}

# All results of students with a name of at least 5 characters
# and with an even score.
assert set(filter(lambda result: len(result[0]) >= 5 and result[1] is not None and result[1] % 2 == 0, results_MI)) \
       == {("Marie", 16), ("Lieve", 4)}

# STEP 5
#   - Closures are lambda functions that use (read) variables defined
#     within their context.

results_MI = {("Paul", 12), ("Bert", 7), ("Marie", 16), ("Jan", None), ("Lieve", 4)}

# ! Print the set of all students that obtained a score on
# ! the exam for MI not below a threshold that is read from
# ! the standard input stream .

threshold = int(input("Enter the threshold: "))
print(set(filter(lambda result : result[1] is not None and result[1]>=threshold ,results_MI)))