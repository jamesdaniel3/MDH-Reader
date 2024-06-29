# MDH-Reader

In this repo, I'm (finally) building a way for Intro CS Head TAs to parse through the office hours data that can be downloaded from my digital hand. Documentation will come as the project is built.

If you are TA looking to use the script, reach out and I can point you to the data files that you need.

If you are TA looking to help with the codebase, see the notes directory, as well as any in-code documentation.

## CAPABILITIES

- Given a list of TA names, get the feedback that they have received from students (get_instructor_feedback)
- Given a student's name or email, get information about all of their trips to office hours (get_student_oh_visits)
- Get all flagged students (get_students_in_need)
- Get a given student's feedback (get_student_feedback)
- Get a list of a TA's shifts (get_ta_shifts)

## TODO (order not representative)

- Create a UI, probably just running from terminal for now
- Allow for getting all TAs feedback without having to list them all
- Allow for output in xlsx and/or sheets
- Allow for auto updating of the data files
- Allow for reading through multiple semesters of data 
- Allow for selecting which semesters of data you want to read through
