from constants import interactions_data_constants as interaction_data, shifts_data_constants as shift_data
from sheets_helper import generate_instructor_feedback_sheet
from utility_functions import get_student_written_feedback, convert_datetime_string
import csv


def get_instructor_feedback(file_path, ta_names, named=False, google_sheet=False):
    """
    This function will get all written feedback that each TA in ta_names has received.

    params:
        file_path: the path to the data file, should be interaction data
        ta_name: a list of tas' first and last names, case-insensitive
        named: determines whether a student's name is tied to their feedback

    if not named:
        return
            {
                <TA NAME>: [feedback1, feedback2, ...],
                <TA NAME>: [feedback1, feedback2, ...],
                ...
            }
    if named:
        return
            {
                <TA NAME>:
                    <STUDENT NAME>: [feedback1, feedback2, ...],
                    <STUDENT NAME>: [feedback1, feedback2, ...],
                    ...
                <TA NAME>:
                    <STUDENT NAME>: [feedback1, feedback2, ...],
                    <STUDENT NAME>: [feedback1, feedback2, ...],
                    ...
                ...
            }
    """

    if named and google_sheet:
        print("Google sheets can only be generated for anonymous feedback")
        quit(1)

    results = {}

    # inefficient but functional
    for x in range(len(ta_names)):
        ta_names[x] = ta_names[x].lower()

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"')
        next(reader)

        for row in reader:
            current_student_name = row[interaction_data.student_first_name] + " " + row[
                interaction_data.student_last_name]
            current_ta_name = row[interaction_data.teacher_first_name].lower() + " " + row[
                interaction_data.teacher_last_name].lower()
            if current_ta_name in ta_names:
                if row[interaction_data.student_left_feedback] == "TRUE":
                    feedback = get_student_written_feedback(row)
                    if feedback == "" or feedback is None:
                        continue
                    if not named:
                        results[current_ta_name] = results.get(current_ta_name, []) + [feedback]
                    else:
                        # I feel like there has to be a more efficient way of handling this conditional structure
                        if current_ta_name in results:
                            if current_student_name in results[current_ta_name]:
                                results[current_ta_name][current_student_name] += [feedback]
                            else:
                                results[current_ta_name][current_student_name] = [feedback]
                        else:
                            results[current_ta_name] = {current_student_name: [feedback]}

    if google_sheet:
        generate_instructor_feedback_sheet(results)
        return

    return results


def get_ta_shifts(file_path, ta_name, limit=None):
    """
    This function will return a list of a TA's shifts given their names

    params:
        file_path: the path to the data file, should be shift data
        ta_name: the ta's first and last name, case-insensitive
        limit: the number of shifts back you want to get info for

    return: a list of dictionaries containing the information about a TA's shift activity
    """

    shifts = []
    ta_name = ta_name.lower()
    count = 0

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"')
        next(reader)

        for row in reader:
            if row[shift_data.first_name].lower() + " " + row[shift_data.last_name].lower() == ta_name:
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
