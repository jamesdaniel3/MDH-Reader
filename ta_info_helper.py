from constants import interactions_data_constants as data
from utility_functions import get_student_written_feedback
import csv

FILE_PATH = './mdh_files/S24_interaction_data.csv'  


def get_instructor_feedback(file_path, ta_names, anonymous=True):
    """
    This function will get all written feedback that each TA in ta_names has received.

    params:
        file_path: the path to the data file, should be interaction data
        ta_name: a list of tas' first and last names
        anonymous: determines whether a students name is tied to their feedback

    if anonymous:
        return
            {
                <TA NAME>: [feedback1, feedback2, ...],
                <TA NAME>: [feedback1, feedback2, ...],
                ...
            }
    if not anonymous:
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

    results = {}

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"')
        next(reader)
        
        for row in reader:
            current_student_name = row[data.student_first_name] + " " + row[data.student_last_name]
            current_ta_name = row[data.teacher_first_name] + " " + row[data.teacher_last_name]
            if current_ta_name in ta_names:
                if row[data.student_left_feedback] == "TRUE":
                    feedback = get_student_written_feedback(row)
                    if feedback == "" or feedback is None:
                        continue
                    if anonymous:
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

    return results if anonymous else results
