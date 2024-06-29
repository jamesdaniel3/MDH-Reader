from constants import interactions_data_constants as data
from utility_functions import get_student_written_feedback
import csv

FILE_PATH = './mdh_files/S24_interaction_data.csv'  


def get_instructor_feedback(file_path, ta_name, anonymous=True):
    """
    This function will get all written feedback that a given TA has received.

    params:
        file_path: the path to the data file, should be interaction data
        ta_name: the ta's first and last name, capitalization is irrelevant
        anonymous: determines whether a students name is tied to their feedback

    return: a list of student feedback if anonymous is True, a dictionary of student names tied to their feedback if anonymous is False
    """

    instructor_first_name, instructor_last_name = ta_name.lower().split()
    instructor_feedback_anonymous = []
    instructor_feedback_named = {}

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"')
        
        for row in reader:
            if row[data.teacher_first_name].lower() == instructor_first_name and row[data.teacher_last_name].lower() == instructor_last_name:
                if row[data.student_left_feedback] == "TRUE":
                    feedback = get_student_written_feedback(row)
                    if feedback == "" or feedback is None:
                        continue
                    if anonymous:
                        instructor_feedback_anonymous.append(feedback)
                    else:
                        instructor_feedback_named[row[data.student_first_name] + " " + row[data.student_last_name]] = instructor_feedback_named.get(row[data.student_first_name] + " " + row[data.student_last_name], "") + feedback

    return instructor_feedback_anonymous if anonymous else instructor_feedback_named
