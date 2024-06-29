import argparse
from constants.files import INTERACTION_DATA, SHIFT_DATA
from student_info_helper import get_student_oh_visits, get_students_in_need, get_student_feedback
from ta_info_helper import get_instructor_feedback, get_ta_shifts


def main():
    parser = argparse.ArgumentParser(description="MDH Data Parsing Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for get_student_oh_visits
    parser_oh_visits = subparsers.add_parser("get_student_oh_visits", help="Get student office hours visits")
    parser_oh_visits.add_argument("--student_name", default="empty", help="Student's first and last name")
    parser_oh_visits.add_argument("--student_email", default="empty", help="Student's email")

    # Subparser for get_students_in_need
    subparsers.add_parser("get_students_in_need", help="Get students in need")

    # Subparser for get_student_feedback
    parser_student_feedback = subparsers.add_parser("get_student_feedback", help="Get student feedback")
    parser_student_feedback.add_argument("--student_name", default="empty", help="Student's first and last name")
    parser_student_feedback.add_argument("--student_email", default="empty", help="Student's email")

    # Subparser for get_instructor_feedback
    parser_instructor_feedback = subparsers.add_parser("get_instructor_feedback", help="Get instructor feedback")
    parser_instructor_feedback.add_argument("--ta_names", nargs='+', help="List of TA names")
    parser_instructor_feedback.add_argument("--named", action="store_true", help="Named feedback")
    parser_instructor_feedback.add_argument("--google_sheet", action="store_true", help="Generate Google Sheet")
    parser_instructor_feedback.add_argument("--excel_workbook", action="store_true", help="Generate Excel Workbook")

    # Subparser for get_ta_shifts
    parser_ta_shifts = subparsers.add_parser("get_ta_shifts", help="Get TA shifts")
    parser_ta_shifts.add_argument("ta_name", help="TA's first and last name")
    parser_ta_shifts.add_argument("--limit", type=int, help="Limit the number of shifts")

    args = parser.parse_args()

    interaction_data_file = INTERACTION_DATA[0]
    shift_data_file = SHIFT_DATA[0]

    if args.command == "get_student_oh_visits":
        result = get_student_oh_visits(interaction_data_file, args.student_name, args.student_email)
        print(result)

    elif args.command == "get_students_in_need":
        result = get_students_in_need(interaction_data_file)
        print(result)

    elif args.command == "get_student_feedback":
        result = get_student_feedback(interaction_data_file, args.student_name, args.student_email)
        print(result)

    elif args.command == "get_instructor_feedback":
        result = get_instructor_feedback(interaction_data_file, args.ta_names, args.named, args.google_sheet, args.excel_workbook)
        if not args.google_sheet and not args.excel_workbook:
            print(result)

    elif args.command == "get_ta_shifts":
        result = get_ta_shifts(shift_data_file, args.ta_name, args.limit)
        print(result)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
