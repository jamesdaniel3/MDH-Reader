import json
from constants import interactions_data_constants as data

def get_student_written_feedback(row):
    student_responses = json.loads(row[data.student_feedback])
    for response in student_responses:
        if response["question"]["type"] == "free-response":
            return response["answer"]