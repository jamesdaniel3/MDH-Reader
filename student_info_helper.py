from constants import interactions_data_constants as data
from utility_functions import get_student_written_feedback, get_ta_written_feedback, convert_datetime_string
import csv
import json

FILE_PATH = './mdh_files/S24_interaction_data.csv'  


def get_student_oh_visits(file_path, student_name="", student_email=""):
    """
    This function will give information about all of a student's visits to office hours.

    params:
        file_path: the path to the data file, should be interaction data
        student_name: the student's first and last name, capitalization is irrelevant
        student_email: the student's email

    return: a list of dictionaries containing the information about the student's OH visits, see the info= {} section
    """

    student_first_name, student_last_name = student_name.lower().split()

    student_visits_info = [] 
    with (open(file_path, mode='r', encoding='utf-8') as file):
        reader = csv.reader(file, delimiter=',', quotechar='"')
        next(reader)
        
        for row in reader:
            if student_email == row[data.student_email] \
                or student_first_name == row[data.student_first_name].lower() \
                    and student_last_name == row[data.student_last_name].lower():

                student_prompts_results = json.loads(row[data.student_prompts])
                reason_for_request = "Not given" if len(student_prompts_results) < 2 else student_prompts_results[1]["answer"]
                student_written_feedback = get_student_written_feedback(row) if get_student_written_feedback(row) else "None"
                ta_written_feedback = get_ta_written_feedback(row) if get_ta_written_feedback(row) else "None"

                info = {
                    "interaction_id": row[data.ticket_id],
                    "ta_name": row[data.teacher_first_name] + " " + row[data.teacher_last_name],
                    "date": convert_datetime_string(row[data.started_at])[0],
                    "time_requested": convert_datetime_string(row[data.started_at])[1],
                    "reason_for_request": reason_for_request,
                    "student_written_feedback": student_written_feedback,
                    "ta_written_feedback":  ta_written_feedback,
                }
                student_visits_info.append(info)

    return student_visits_info


def get_students_in_need(file_path):
    """
    This function will give information about all of a students who have had a TA answer one or both of the following:
        "an instructor should comment the student, comments below"
        "other"

    Note: there is a lot of junk data due to the fact that we are taking instances where the TA answered "other", but
            it seems worth keeping as better safe than sorry, could probably be cleaned some

    params:
        file_path: the path to the data file, should be interaction data

    return: a list of dictionaries containing the information about the students, see the info= {} section
    """
    flagged_student_instances = []
    with (open(file_path, mode='r', encoding='utf-8') as file):
        reader = csv.reader(file, delimiter=',', quotechar='"')
        next(reader)

        for row in reader:
            ta_responses = json.loads(row[data.teacher_feedback])
            if len(ta_responses) == 0:
                continue

            if "3" in ta_responses[0]["answer"]["selections"] or 4 in ta_responses[0]["answer"]["selections"]:
                ta_written_feedback = get_ta_written_feedback(row) if get_ta_written_feedback(row) else "None"

                info = {
                    "interaction_id": row[data.ticket_id],
                    "ta_name": row[data.teacher_first_name] + " " + row[data.teacher_last_name],
                    "student_name": row[data.student_first_name] + " " + row[data.student_last_name],
                    "ta_comment": ta_written_feedback,
                    "date": convert_datetime_string(row[data.started_at])[0],
                }

                flagged_student_instances.append(info)

    return flagged_student_instances


result = get_students_in_need(FILE_PATH)

for each in result:
    print(each)
