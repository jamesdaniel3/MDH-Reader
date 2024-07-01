# MDH-Reader

In this repo, I'm building a way for TAs to parse through the office hours data that can be downloaded from My Digital Hand (MDH). 

A note for anyone using this repo. The functions are as good as the data they are provided, so note that you may need to retrieve the most recent data from MDH in order to get more accurate results. This code has been tested as far back as Spring 2023, but bugs could still be lurking. 

If you are TA looking to use the script, reach out and I can point you to the data files that you need, as well as the Google console credentials and the roster file. Currently, the Google cloud console project tied to this project is in testing mode, which means user emails are allowed manually. 
If you are unable to use the Google sheets functionality, reach out to me and I  can add you to our test users. I am trying to get the project approved for "production" use.

If you are looking to help with the codebase, see the developer_notes directory, as well as any in-code documentation and reach out for files. Feel free to submit a PR if you want to help change something!

This should be useful for anyone curious about the script:
[Description of Functions and Their Parameters](notes/functions.md)

## CAPABILITIES

- Given a list of TA names, get the feedback that they have received from students (get_instructor_feedback)
- Output TA feedback into a Google sheet or Excel workbook where each TA would have their own sheet with comments (generate_ta_feedback_sheet)
- Given a student's name or email, get information about all of their trips to office hours (get_student_oh_visits)
- Get all flagged students (get_students_in_need)
- Get a given student's feedback (get_student_feedback)
- Get a list of a TA's shifts (get_ta_shifts)
- For all of the above actions, choose the number of semesters back for which you want data, defaults to using all data

## SETUP

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

Additionally, you will need to do the following:
- Get interaction data and shift data from MDH and put the files in the mdh_files directory
  - These files should follow the naming scheme <interaction/shift>_data_<f/s><last 2 digits of year>.csv
    - ex. interaction_data_f23.csv
- Update the dictionaries in prompts.py with the prompts needed 
  - These are the prompts you use when asking for the data that you want. In this case, it's expecting the prompt used for getting TA written feedback and the prompt used for getting student written feedback
  - If either of the these does not apply, you don't have to update the dictionary, the code will throw warnings but it will work
- Make sure the file paths in files.py match up with the files you have
- Get credentials.json from me and put it in root directory of project 
- Get ta_roster.py from me or make your own and put it in constants directory
  - ta_roster.py should contain a list of strings representing all the TAs in your course 
  - It is used as a default value so that if you want information for all of your TAs you don't have to list them all
- Confirm that your email has been added to the list of allowed emails 

## Dev TODO (order not representative)

- Allow for auto updating of the data files
- Give functions more descriptive default return values
- Make the generate google sheet function return the link to the sheet
