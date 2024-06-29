# MDH-Reader

In this repo, I'm (finally) building a way for Intro CS Head TAs to parse through the office hours data that can be downloaded from my digital hand. Documentation will come as the project is built.

If you are TA looking to use the script, reach out and I can point you to the data files that you need. Currently, the Google cloud console project tied to this project is in testing mode, 
which means user emails are allowed manually. If you are unable to use the Google sheets functionality, reach out to me and I  can add you to our test users. I am trying to get the project 
approved for "production" use.

If you are TA looking to help with the codebase, see the notes directory, as well as any in-code documentation.

## CAPABILITIES

- Given a list of TA names, get the feedback that they have received from students (get_instructor_feedback)
- Output TA feedback into a Google sheet or Excel workbook where each TA would have their own sheet with comments (generate_ta_feedback_sheet)
- Given a student's name or email, get information about all of their trips to office hours (get_student_oh_visits)
- Get all flagged students (get_students_in_need)
- Get a given student's feedback (get_student_feedback)
- Get a list of a TA's shifts (get_ta_shifts)

## INSTALLS

If requirements.txt is not working correctly, run the following commands in your working directory
```bash
  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
  pip install pytz
  pip install openpyxl
  pip install chardet
```

## TODO (order not representative)

- Create a UI, probably just running from terminal for now
- Allow for auto updating of the data files
- Allow for reading through multiple semesters of data
- Allow for selecting which semesters of data you want to read through
