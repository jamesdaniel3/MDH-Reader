from constants import prompts


def check_course_prompts(course, ta_responses_needed=True, student_responses_needed=True):
    if course in prompts.TA_WRITTEN_FEEDBACK_PROMPTS and course in prompts.STUDENT_WRITTEN_FEEDBACK_PROMPTS:
        return

    if course not in prompts.TA_WRITTEN_FEEDBACK_PROMPTS and course not in prompts.STUDENT_WRITTEN_FEEDBACK_PROMPTS:
        print("The course you provided does not have any prompts associated with it. Please be sure that the course information is in prompts.py")
        quit(1)

    if course not in prompts.TA_WRITTEN_FEEDBACK_PROMPTS or course not in prompts.STUDENT_WRITTEN_FEEDBACK_PROMPTS:
        print("WARNING: we recommend that you put your courses prompt information in for student and ta feedback.")

    if ta_responses_needed:
        if course not in prompts.TA_WRITTEN_FEEDBACK_PROMPTS:
            print("The course you provided does not have any prompts listed for TA feedback. Please add them in prompts.py if you have them. If not, this function cannot be used.")
            quit(1)

    if student_responses_needed:
        if course not in prompts.STUDENT_WRITTEN_FEEDBACK_PROMPTS:
            print("The course you provided does not have any prompts listed for student feedback. Please add them in prompts.py if you have them. If not, this function cannot be used.")
            quit(1)


def check_student_params(student_name, student_email):
    if student_name == "empty" and student_email == "empty":
        print("You must provide either a student name or their email to run this function")
        quit(1)


def check_data_export(data_is_named, create_sheet, create_workbook):
    if data_is_named:
        if create_sheet:
            print("Google sheets can only be generated for anonymous feedback at the current moment. If you would like named feedback, please removed the --google_sheet flag.")
            quit(1)
        if create_workbook:
            print("Excel workbooks can only be generated for anonymous feedback at the current moment. If you would like named feedback, please removed the --excel_workbook flag.")
            quit(1)