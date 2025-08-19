"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    rounded_scores = []
    while student_scores:
        rounded_scores.append(round(student_scores.pop()))
    return rounded_scores
        
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

 

def count_failed_students(student_scores):
    failed_students = 0
    for item in student_scores:
        if item <= 40:
            failed_students += 1 
    return failed_students
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """


def above_threshold(student_scores, threshold):
    best_scores = []
    for items in student_scores:
        if items >= threshold:
            best_scores.append(items)
    return best_scores
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """


def letter_grades(highest):
    increment = round((highest - 40)/4)
    scores = []
    for score in range(41, highest, increment):
        scores.append(score)
    return scores


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    results = []
    for index, name in enumerate(student_names):
        rank_string = str(index + 1) + ". " + name + ": " + str(student_scores[index])
        results.append(rank_string)
    return results


    pass


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    result = []
    for item in student_info:
        if item[1] == 100:
            result = item
            break
    return result
