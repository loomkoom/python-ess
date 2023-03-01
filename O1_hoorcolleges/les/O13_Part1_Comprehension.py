import random

#! Iterative definition of a function to return a set of all
# ! students that passed the exam for some course.

def get_all_passed_students(results):
    """
      Return a set of all students that have passed the
      exam for some course.
        - The given results are presented as a mutable set of
          tuples that start with the name of the student
          followed by his/her grade.
        - The grade is an integer in the range from 0 to 20.
          Students that did not take the exam have None as
          their grade.
    """

    passed_students = set()

    for result in results:

        # name, score = result
        _, score = result

        # if score != None and score >= 10:
        if score is not None and score >= 10:
            set.add(passed_students, result)
    return passed_students

assert get_all_passed_students( \
    {("Paul", 12), ("Bert", 7), ("Marie", 16), \
     ("Jan", None), ("Lieve", 4)}) \
       == {("Paul", 12), ("Marie", 16)}


# ! Recursive definition of a function to return a set of all
# ! students that passed the exam for some course.
# ! The function assumes the given set of results is mutable.

def get_all_passed_students(results):
    """
      Return a set of all students that have passed the
      exam for some course.
        - The given results are presented as a mutable set of
          tuples that start with the name of the student
          followed by his/her grade.
        - The grade is an integer in the range from 0 to 20.
          Students that did not take the exam have None as
          their grade.
    """

    if len(results) == 0:
        return set()

    name,score = set.pop(results)                                   # delete willekeurig element
    passed_students = get_all_passed_students(results)

    if score is not None and score >= 10:
        set.add(passed_students,(name,score))

    set.add(results,(name,score))                                   # !! anders blijft de set leeg op het einde

    return passed_students


results_MI = {("Paul", 12), ("Bert", 7), ("Marie", 16), \
          ("Jan", None), ("Lieve", 4)}
assert get_all_passed_students(results_MI)== { ("Paul",12), ("Marie",16) }
print(results_MI)


# ! Recursive definition of a function to return a set of all
# ! students that passed the exam for some course.
# ! The given set of results may be immutable..

def get_all_passed_students(results):
    """
      Return a set of all students that have passed the
        - The given results are presented as a set of
          tuples that start with the name of the student
      exam for some course.
          followed by his/her grade. The given set may be
          mutable or immutable.
        - The grade is an integer in the range from 0 to 20.
          Students that did not take the exam have None as
          their grade.
    """

    if len(results) == 0:
        return frozenset()

    result = random.choice(tuple(results))
    passed_students = get_all_passed_students(results - frozenset([result]))
    _,score = result

    if score is not None and score >= 10:
        return passed_students | frozenset([result])              # unie |
    else:
        return passed_students


assert get_all_passed_students(\
 frozenset( ( ("Paul",12), ("Bert", 7), ("Marie",16),\
      ("Jan", None), ("Lieve",4) ) ) )\
 == frozenset( ( ("Paul",12), ("Marie",16) ) )


# ! Definition of a function to return a set of all students
# ! that passed the exam for some course using set comprehension.

def get_all_passed_students(results):                                       # mag niet op practicum
    """
      Return a set of all students that have passed the
      exam for some course.
        - The given results are presented as a mutable set of
          tuples that start with the name of the student
          followed by his/her grade.
        - The grade is an integer in the range from 0 to 20.
          Students that did not take the exam have None as
          their grade.
    """

    return {(name,score)
            for (name,score) in results
            if score is not None
            and score >= 10}

assert get_all_passed_students(\
 { ("Paul",12), ("Bert", 7), ("Marie",16),\
      ("Jan", None), ("Lieve",4) } )\
 == { ("Paul",12), ("Marie",16) }
