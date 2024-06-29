from constants import interactions_data_constants as data
import csv
import json

FILE_PATH = './mdh_files/S24_interaction_data.csv'  

def get_instructor_feedback(file_path, ta_name, anonymous=True):
    """
    This function will get all written feedback that a given TA has receieved.
    
    params:
        file_path: the path to the data file, should be interaction data
        ta_name: the ta's first and last name, capitalization is irrelevant 
        anoymous: determines whether or not a students name is tied to their feedback
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
                    student_responses = json.loads(row[data.student_feedback])
                    for response in student_responses:
                        if response["question"]["type"] == "free-response":
                            if response["answer"] == "":
                                continue
                            if anonymous:
                                instructor_feedback_anonymous.append(response["answer"])
                            else:
                                instructor_feedback_named[row[data.student_first_name] + " " + row[data.student_last_name]] = instructor_feedback_named.get(row[data.student_first_name] + " " + row[data.student_last_name], "") + response["answer"]

    return instructor_feedback_anonymous if anonymous else instructor_feedback_named


print(get_instructor_feedback(FILE_PATH, "JaMes Daniel"))