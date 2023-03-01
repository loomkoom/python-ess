import functools
import random
import string


class GradeCard:

    def __init__(self, name):
        self.__name = name
        self.__grades = dict()

    def get_name(self):
        return self.__name

    def get_nb_courses(self):
        return len(self.__grades)

    def get_nb_grades(self, course):
        if course in self.__grades:
            return len(self.__grades[course])
        return 0

    def get_grades_for(self, course):
        # if course in self.__grades:
        #     return self.__grades[course]
        return self.__grades.get(course,())


    def add_grade_for(self, course, grade):
        # if course not in self.__grades:
        #     self.__grades[course] = (grade,)
        # else:
        #     self.__grades[course] += (grade,)
        self.__grades[course] = self.get_grades_for(course) + (grade,)

    def get_highest_grade_for(self, course):
        # if course in self.__grades:
        #     if self.__grades[course] != ("NA",):
        #         all_grades = list(self.__grades[course])
        #         if "NA" in all_grades:
        #             times = all_grades.count("NA")
        #             for n in range(times):
        #                 all_grades.remove("NA")
        #         return max(all_grades)
        #     return "NA"
        # return None

        grades = self.get_grades_for(course)
        result = "NA"
        if len(grades) > 0:
            for score in grades:
                if result == "NA" or (score != "NA" and score > result):
                    result = score
            return result
        return None

    def __str__(self):
        header = str(self.__name) + "  |  courses: " + str(self.get_nb_courses()) + "\n" + "-------------------------" + "\n"
        body = ""
        for course, grades in self.__grades.items():
            grades_txt = ""
            for grade in grades:
                grades_txt += str(grade) + ", "
            course_text = str(course) + " : " + grades_txt + "\n"
            body += course_text

        return header + body


def average_score1(gradecards, course):
    any_scores_cards = list(filter(lambda card: card.get_highest_grade_for(course) is not None, gradecards))
    valid_scores = list(map((lambda card: 0 if card.get_highest_grade_for(course) == "NA" else card.get_highest_grade_for(course)), any_scores_cards))
    return functools.reduce(lambda a, b: (a + b), valid_scores) / len(valid_scores)


def average_score2(gradecards, course):
    cards_with_score = list(filter(lambda c: c.get_highest_grade_for(course) != None, gradecards))
    valid_scores = map(lambda c: c.get_highest_grade_for(course) if c.get_highest_grade_for(course) != "NA" else 0, cards_with_score)
    return functools.reduce(lambda a, b: a + b,
                            valid_scores) \
           / len(cards_with_score)


def randomString(stringLength = 10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


gradecards = []
scores = ["NA", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for N in range(10):
    card = GradeCard(randomString())
    for n in range(random.randint(0, 11)):
        card.add_grade_for("filler_course", random.choice(scores))
    gradecards.append(card)

for card in gradecards:
    print(card)
    pass

print(average_score1(gradecards, "filler_course"))
print(average_score2(gradecards, "filler_course"))
