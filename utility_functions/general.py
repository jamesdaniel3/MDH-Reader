import json
from constants import interactions_data_constants as data
from constants import prompts
from datetime import datetime
import pytz
import chardet


def get_student_written_feedback(row, course):
    prompts_of_interest = prompts.STUDENT_WRITTEN_FEEDBACK_PROMPTS[course]
    try:
        student_responses = json.loads(row[data.student_feedback])
        for response in student_responses:
            if response["question"]["prompt"] in prompts_of_interest:
                return response["answer"]
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e} - Skipping row")
        return None


def get_ta_written_feedback(row, course):
    prompts_of_interest = prompts.TA_WRITTEN_FEEDBACK_PROMPTS[course]
    ta_feedback = json.loads(row[data.teacher_feedback])
    for response in ta_feedback:
        # this should just be done with the prompt field, it's safer
        if response["question"]["prompt"] in prompts_of_interest:
            return response["answer"]


def convert_datetime_string(iso_string):
    utc_time = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
    est = pytz.timezone('US/Eastern')
    est_time = utc_time.astimezone(est)
    date = est_time.strftime('%Y-%m-%d')  
    time = est_time.strftime('%I:%M %p')  
    return date, time


def cleaned_feedback(feedback):
    if not feedback:
        return False

    cleaned = feedback.lower().strip()
    bad_feedback = ["none", "n/a", "no comments"]

    if cleaned in bad_feedback:
        return False
    return cleaned


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']
