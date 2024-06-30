# MDH-Reader

In this repo, I'm (finally) building a way for Intro CS Head TAs to parse through the office hours data that can be downloaded from my digital hand. Documentation will come as the project is built.

A note for anyone using this repo. The functions are as good as the data they are provided, so note that you may need to retrieve the most recent data from MDH in order to get more accurate results. This code has been tested as far back as Spring 2023, but bugs could still be lurking. 

If you are TA looking to use the script, reach out and I can point you to the data files that you need. Currently, the Google cloud console project tied to this project is in testing mode, 
which means user emails are allowed manually. If you are unable to use the Google sheets functionality, reach out to me and I  can add you to our test users. I am trying to get the project 
approved for "production" use.

If you are TA looking to help with the codebase, see the developer_notes directory, as well as any in-code documentation and reach out for files.
[Description of Functions and their parameters](notes/functions.md)

## CAPABILITIES

- Given a list of TA names, get the feedback that they have received from students (get_instructor_feedback)
- Output TA feedback into a Google sheet or Excel workbook where each TA would have their own sheet with comments (generate_ta_feedback_sheet)
- Given a student's name or email, get information about all of their trips to office hours (get_student_oh_visits)
- Get all flagged students (get_students_in_need)
- Get a given student's feedback (get_student_feedback)
- Get a list of a TA's shifts (get_ta_shifts)
- For all of the above actions, choose the number of semesters back for which you want data, defaults to using all data

## INSTALLS

If requirements.txt is not working correctly, run the following commands in your working directory
```bash
  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
  pip install pytz
  pip install openpyxl
  pip install chardet
```

Alternatively:
```bash
  pip install -r requirements.txt
```

## TODO (order not representative)

- Allow for auto updating of the data files
- prevent users from calling functions with no student name and no email 
- give functions default return values
- make the generate google sheet return the link to the sheet