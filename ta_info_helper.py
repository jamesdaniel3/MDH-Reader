from constants import interactions_data_constants as interaction_data, shifts_data_constants as shift_data
from constants import ta_roster
from sheets_helper import generate_instructor_feedback_sheet
from excel_helper import generate_instructor_feedback_workbook
from utility_functions.general import get_student_written_feedback, convert_datetime_string, cleaned_feedback, detect_encoding
from utility_functions.error_handling import check_course_prompts, check_data_export
import csv


def get_instructor_feedback(file_paths, ta_names=None, named=False, google_sheet=False, excel_workbook=False, semesters=None, course="UVA CS 1110"):
    check_course_prompts(course, ta_responses_needed=False, student_responses_needed=True)
    check_data_export(named, google_sheet, excel_workbook)

    if ta_names is None:
        ta_names = ta_roster.roster

    if semesters is None:
        semesters = len(file_paths)

    results = {}

    # inefficient but functional
    for x in range(len(ta_names)):
        ta_names[x] = ta_names[x].lower()

    for x in range(len(file_paths)):
        if x >= semesters:
            break

        file_path = file_paths[x]
        encoding = detect_encoding(file_path)
        with open(file_path, mode='r', encoding=encoding) as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')

            for row in reader:
                current_student_name = row[interaction_data.student_first_name] + " " + row[interaction_data.student_last_name]
                current_ta_name = row[interaction_data.teacher_first_name].lower().strip() + " " + row[interaction_data.teacher_last_name].lower().strip()
                if current_ta_name in ta_names:
                    if row[interaction_data.student_left_feedback] == "TRUE":
                        feedback = get_student_written_feedback(row, course)
                        if feedback is None:
                            continue
                        if not cleaned_feedback(feedback):
                            continue
                        if not named:
                            results[current_ta_name] = results.get(current_ta_name, []) + [cleaned_feedback(feedback)]
                        else:
                            # I feel like there has to be a more efficient way of handling this conditional structure
                            if current_ta_name in results:
                                if current_student_name in results[current_ta_name]:
                                    results[current_ta_name][current_student_name] += [cleaned_feedback(feedback)]
                                else:
                                    results[current_ta_name][current_student_name] = [cleaned_feedback(feedback)]
                            else:
                                results[current_ta_name] = {current_student_name: [cleaned_feedback(feedback)]}

    if google_sheet:
        generate_instructor_feedback_sheet(results)
        return

    if excel_workbook:
        generate_instructor_feedback_workbook(results)
        return

    return results


def get_ta_shifts(file_paths, ta_name, limit=None, semesters=None):
    shifts = []
    ta_name = ta_name.lower()
    count = 0

    if semesters is None:
        semesters = len(file_paths)

    for x in range(len(file_paths)):
        if x >= semesters:
            break

        file_path = file_paths[x]
        encoding = detect_encoding(file_path)
        with open(file_path, mode='r', encoding=encoding) as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            next(reader)

            for row in reader:
                if row[shift_data.first_name].lower().strip() + " " + row[shift_data.last_name].lower().strip() == ta_name:
                    count += 1
                    info = {
                        "date": convert_datetime_string(row[shift_data.start_at])[0],
                        "start_time": convert_datetime_string(row[shift_data.start_at])[1],
                        "end_time": convert_datetime_string(row[shift_data.end_at])[1],
                    }
                    shifts.append(info)
                    if limit is not None and count >= limit:
                        return shifts
    return shifts
