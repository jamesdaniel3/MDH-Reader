from constants import interactions_data_constants as data
from utility_functions import get_student_written_feedback, get_ta_written_feedback, convert_datetime_string
import csv
import json

FILE_PATH = './mdh_files/S24_interaction_data.csv'  

def get_student_oh_visits(file_path, student_name="", student_email=""):
    if student_name: student_first_name, student_last_name = student_name.lower().split()

    student_visits_info = [] 
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"')
        
        for row in reader:
            if student_first_name == row[data.student_first_name].lower() and student_last_name == row[data.student_last_name].lower():
                student_prompts_results = json.loads(row[data.student_prompts])
                reason_for_request = "Not given" if len(student_prompts_results) < 2 else student_prompts_results[1]["answer"]
                student_written_feedback = get_student_written_feedback(row) if get_student_written_feedback(row) else "None"
                ta_written_feedback = get_ta_written_feedback(row) if get_ta_written_feedback(row) else "None"

                print(row[data.teacher_feedback])
                info = {
                    "interaction_id": row[data.ticket_id],
                    "ta_name" : row[data.teacher_first_name] + " " + row[data.teacher_last_name], 
                    "date": convert_datetime_string(row[data.started_at])[0],
                    "time_requested": convert_datetime_string(row[data.started_at])[1],
                    "reason_for_request": reason_for_request,
                    "student_written_feedback": student_written_feedback,
                    "ta_written_feedback":  ta_written_feedback,
                }
                print("")
                student_visits_info.append(info)

    return student_visits_info
