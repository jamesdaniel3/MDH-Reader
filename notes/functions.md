### Overview

To call any function below, write the following in your terminal, assuming you are in the main directory:
```bash
python parse_mdh.py <function_name> <required_param_if_needed> <flag_for_optional_param> <value_for_optional_param>
```

Note that `file_paths` is handled for you so you shouldn't pass in a value for it. 

Examples:

```bash
  python parse_mdh.py get_instructor_feedback --ta_names "John Doe" "Jane Doe" --semesters 1 --google_sheet
  python parse_mdh.py get_instructor_feedback
  python parse_mdh.py get_student_oh_vists --student_name "John Doe"
```

### [Student Information](../student_info_helper.py)
```python
def get_student_oh_visits(file_paths, student_name="empty", student_email="empty", semesters=None):
```
#### Intention
This function gets information about all of a student's visits to office hours.

#### Params
- `file_paths`: a list of the paths to all the files that contain data 
- `student_name`: the student's full name (first and last), case-insensitive
- `student_email`: the student's email, case-sensitive
- `semesters`: the number of semesters worth of information you want to consider, starting from the current semester, when `None`, all semesters will be used
#### Return Value 
A list of dictionaries. Each dictionary has the following structure:
```json
{
    "interaction_id": "99999",
    "ta_name": "John Doe",
    "date": "YYYY-MM-DD",
    "time_requested": "HH:MM AM/PM", (EST)
    "reason_for_request": "student reason", ("None" if not found)
    "student_written_feedback": "student feedback", ("None" if no feedback)
    "ta_written_feedback":  "ta feedback", ("None" if no feedback)
}
```
------------------------------------------------------------------------------------------------------------

```python
def get_students_in_need(file_paths, semesters=None):
```
#### Intention
This function will give information about all of a students who have had a TA answer one or both of the following: 
- "an instructor should comment the student, comments below" 
- "other"
#### Params
- `file_paths`: a list of the paths to all the files that contain data 
- `semesters`: the number of semesters worth of information you want to consider, starting from the current semester, when `None`, all semesters will be used

#### Return Value
A list of dictionaries. Each dictionary has the following structure:
```json
{
  'interaction_id': '99999', 
  'ta_name': 'Jane Doe', 
  'student_name': 'Jane Doe', 
  'ta_comment': "comment",  ("None" if not found) 
  'date': 'YYYY-MM-DD'
}
```

------------------------------------------------------------------------------------------------------------

```python
def get_student_feedback(file_paths, student_name="empty", student_email="empty", semesters=None):
```
#### Intention
Get all the notes that instructors have left regarding the student. Aka if an instructor has left a note about a student after seeing them in OH it will be returned. 

#### Params
- `file_paths`: a list of the paths to all the files that contain data 
- `student_name`: the student's full name (first and last), case-insensitive
- `student_email`: the student's email, case-sensitive
- `semesters`: the number of semesters worth of information you want to consider, starting from the current semester, when `None`, all semesters will be used

#### Return Value
A dictionary where keys are TA names and values are lists of the feedback they have given about the student

------------------------------------------------------------------------------------------------------------

### [Instructor Information](../ta_info_helper.py)
```python
def get_instructor_feedback(file_paths, ta_names=None, named=False, google_sheet=False, excel_workbook=False, semesters=None):
```
#### Intention
Get all of the feedback that the desired instructors have received from students. This can be output to terminal or put in a Google sheet or Excel workbook. 

The feedback can be anonymous or named, but named feedback cannot be exported.
#### Params
- `file_paths`: a list of the paths to all the files that contain data 
- `ta_names`: a list of the names of the TAs for whom you want to find feedback, case-insensitive
- `named`: determines whether feedback will be anonymous
- `google_sheet:` determines whether a google sheet is created
- `excel_workbook` determines whether an excel sheet is created 
- `semesters`: the number of semesters worth of information you want to consider, starting from the current semester, when `None`, all semesters will be used

#### Return Value
- If data exported: None
- If anonymous: a dictionary where keys are TA names and values are lists of feedback that they have received 
- If named: a nested dictionaries with the following structure
```json
{
  "TA 1": {
    "Student 1": ["feedback 1", "feedback 2", "..."],
    "Student 2": ["feedback 1", "feedback 2", "..."]
  },
   "TA 2": {
    "Student 1": ["feedback 1", "feedback 2", "..."],
    "Student 2": ["feedback 1", "feedback 2", "..."]
  }
}
```

------------------------------------------------------------------------------------------------------------

```python
def get_ta_shifts(file_paths, ta_name, limit=None, semesters=None):
```
#### Intention
Get shift information for a TA

#### Params
- `file_paths`: a list of the paths to all the files that contain data 
- `ta_name`: the name of the TA for whom you want information, case-insensitive
- `limit`: the maximum number of shifts you want to see data for. Note that the shifts will be found chronologically from the most recent
- `semesters`: the number of semesters worth of information you want to consider, starting from the current semester, when `None`, all semesters will be used
#### Return Value 
A list of dictionaries, each of which has the following structure:
```json
{
    "date": "YYYY-MM-DD",
    "start_time": "HH:MM AM/PM", (EST)
    "end_time": "HH:MM AM/PM" (EST)
}
```
------------------------------------------------------------------------------------------------------------

### [Sheet Creation](../excel_helper.py)

```python
def generate_instructor_feedback_sheet(info):
```
#### Intention
Create a Google sheets file with the information returned by get_instructor_feedback. There will be a sheet in the file for each TA with feedback and each row of the sheet will have a piece of feedback. The feedback should be chronological from most recent.
#### Params
- `info`: a dictionary where the keys are instructor names and the values are lists of feedback that they have received 
#### Return Value 
None

------------------------------------------------------------------------------------------------------------

```python
def generate_instructor_feedback_workbook(info):
```
#### Intention
Create an Excel workbook with the information returned by get_instructor_feedback. There will be a sheet in the file for each TA with feedback and each row of the sheet will have a piece of feedback. The feedback should be chronological from most recent. The sheet will be located in the excel_files folder.
#### Params
- `info`: a dictionary where the keys are instructor names and the values are lists of feedback that they have received 
#### Return Value 
None

------------------------------------------------------------------------------------------------------------

### [Utility Functions](../utility_functions/general.py)
```python
def get_student_written_feedback(row):
```
#### Intention
Get any feedback a student has written from a given row

#### Params
- `row`: a row of information from the csv file

#### Return Value
- string containing feedback if feedback found 
- None if feedback not found 


------------------------------------------------------------------------------------------------------------

```python
def get_ta_written_feedback(row):
```
#### Intention
Get any feedback a ta has written from a given row
#### Params
- `row`: a row of information from the csv file
#### Return Value 
- string containing feedback if feedback found 
- None if feedback not found 

------------------------------------------------------------------------------------------------------------

```python
def convert_datetime_string(iso_string):
```
#### Intention
Convert a dateTime string to a date and a time in EST
#### Params
- `iso_string`: a string representing a dateTime in UTC
#### Return Value 
A list containing the date and time in the format ["YYYY-MM-DD", "HH:MM AM/PM"]

------------------------------------------------------------------------------------------------------------

```python
def cleaned_feedback(feedback):
```
#### Intention
Clean feedback. This means strip feedback and remove empty feedback as well as feedback like "None" and "N/A". Currently removes the following, case-insensitive: 
- "none"
- "n/a"
- "no comments"
#### Params
- `feedback`: a string

#### Return Value
- False if bad data
- string containing cleaned data if good data 


------------------------------------------------------------------------------------------------------------

```python
def detect_encoding(file_path):
```
#### Intention
Find the encoding of a given file
#### Params
- `file_path`: the path to the file in question
#### Return Value 
A string representing the files encoding

