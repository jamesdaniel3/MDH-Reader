import json
from constants import interactions_data_constants as data
from datetime import datetime
import pytz

def get_student_written_feedback(row):
    student_responses = json.loads(row[data.student_feedback])
    for response in student_responses:
        if response["question"]["type"] == "free-response":
            return response["answer"]


def get_ta_written_feedback(row):
    ta_feedback = json.loads(row[data.teacher_feedback])
    for response in ta_feedback:
        if response["question"]["type"] == "free-response":
            return response["answer"]


def convert_datetime_string(iso_string):
    utc_time = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
    est = pytz.timezone('US/Eastern')
    est_time = utc_time.astimezone(est)
    date = est_time.strftime('%Y-%m-%d')  
    time = est_time.strftime('%I:%M %p')  
    return date, time