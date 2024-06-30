from constants import interactions_data_constants as interaction_data
from utility_functions.general import get_student_written_feedback, get_ta_written_feedback, convert_datetime_string, detect_encoding
from utility_functions.error_handling import check_course_prompts, check_student_params
import csv
import json


def get_student_oh_visits(file_paths, student_name="empty", student_email="empty", semesters=None, course="UVA CS 1110"):
    check_student_params(student_name, student_email)
    check_course_prompts(course, ta_responses_needed=True, student_responses_needed=True)

    student_first_name, student_last_name = student_name.lower().split()
    student_visits_info = []

    if semesters is None:
        semesters = len(file_paths)

    for x in range(len(file_paths)):
        if x >= semesters:
            break

        file_path = file_paths[x]
        encoding = detect_encoding(file_path)

        with (open(file_path, mode='r', encoding=encoding) as file):
            reader = csv.reader(file, delimiter=',', quotechar='"')
            next(reader)

            for row in reader:
                if student_email == row[interaction_data.student_email] \
                    or student_first_name == row[interaction_data.student_first_name].lower() \
                        and student_last_name == row[interaction_data.student_last_name].lower():

                    student_prompts_results = json.loads(row[interaction_data.student_prompts])
                    reason_for_request = "None" if len(student_prompts_results) < 2 else student_prompts_results[1]["answer"]
                    student_written_feedback = get_student_written_feedback(row, course) if get_student_written_feedback(row, course) else "None"
                    ta_written_feedback = get_ta_written_feedback(row, course) if get_ta_written_feedback(row, course) else "None"

                    info = {
                        "interaction_id": row[interaction_data.ticket_id],
                        "ta_name": row[interaction_data.teacher_first_name] + " " + row[interaction_data.teacher_last_name],
                        "date": convert_datetime_string(row[interaction_data.started_at])[0],
                        "time_requested": convert_datetime_string(row[interaction_data.started_at])[1],
                        "reason_for_request": reason_for_request,
                        "student_written_feedback": student_written_feedback,
                        "ta_written_feedback":  ta_written_feedback,
                    }
                    student_visits_info.append(info)

    return student_visits_info


def get_students_in_need(file_paths, semesters=None, course="UVA CS 1110"):
    check_course_prompts(course, ta_responses_needed=True, student_responses_needed=False)

    flagged_student_instances = []

    if semesters is None:
        semesters = len(file_paths)

    for x in range(len(file_paths)):
        if x >= semesters:
            break

        file_path = file_paths[x]
        encoding = detect_encoding(file_path)
        with (open(file_path, mode='r', encoding=encoding) as file):
            reader = csv.reader(file, delimiter=',', quotechar='"')
            next(reader)

            for row in reader:
                ta_responses = json.loads(row[interaction_data.teacher_feedback])
                if len(ta_responses) == 0:
                    continue

                if "3" in ta_responses[0]["answer"]["selections"] or 4 in ta_responses[0]["answer"]["selections"]:
                    ta_written_feedback = get_ta_written_feedback(row, course) if get_ta_written_feedback(row, course) else "None"

                    info = {
                        "interaction_id": row[interaction_data.ticket_id],
                        "ta_name": row[interaction_data.teacher_first_name] + " " + row[interaction_data.teacher_last_name],
                        "student_name": row[interaction_data.student_first_name] + " " + row[interaction_data.student_last_name],
                        "ta_comment": ta_written_feedback,
                        "date": convert_datetime_string(row[interaction_data.started_at])[0],
                    }

                    flagged_student_instances.append(info)

    return flagged_student_instances


def get_student_feedback(file_paths, student_name="empty", student_email="empty", semesters=None, course="UVA CS 1110"):
    check_student_params(student_name, student_email)
    check_course_prompts(course, ta_responses_needed=True, student_responses_needed=False)

    student_feedback = {}
    student_first_name, student_last_name = student_name.lower().split()

    if semesters is None:
        semesters = len(file_paths)

    for x in range(len(file_paths)):
        if x >= semesters:
            break

        file_path = file_paths[x]
        encoding = detect_encoding(file_path)
        with (open(file_path, mode='r', encoding=encoding) as file):
            reader = csv.reader(file, delimiter=',', quotechar='"')
            next(reader)

            for row in reader:
                current_ta_name = row[interaction_data.teacher_first_name].lower() + " " + row[interaction_data.teacher_last_name].lower()
                if student_email == row[interaction_data.student_email] \
                        or student_first_name == row[interaction_data.student_first_name].lower() \
                        and student_last_name == row[interaction_data.student_last_name].lower():
                    ta_responses = json.loads(row[interaction_data.teacher_feedback])

                    if len(ta_responses) == 0:
                        continue
                    if "3" in ta_responses[0]["answer"]["selections"] or 4 in ta_responses[0]["answer"]["selections"]:
                        ta_written_feedback = get_ta_written_feedback(row, course) if get_ta_written_feedback(row, course) else "None"
                        student_feedback[current_ta_name] = student_feedback.get(current_ta_name, []) + [ta_written_feedback]
    return student_feedback
