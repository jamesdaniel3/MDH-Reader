### Interaction data is a CSV file, each line should have the following fields, all of which are strings:

- `ticket_id` [0]
- `status` [1]
- `student_prompts` [2]
- `is_followup` [3]
- `parent_id` [4]
- `requested_at` [5] (date string)
- `called_at` [6]
- `started_At` [7]
- `completed_at` [8]
- `canceled_at` [9]
- `virtual_url` [10]
- `teacher_first_name` [11]
- `teacher_nast_name` [12]
- `teacher_email` [13]
- `teacher_group` [14]
- `teacher_identifier` [15]
- `teacher_account_id` [16]
- `teacher_user_id` [17]
- `teacher_left_feedback` [18]
- `teacher_feedback` [19]
- `student_first_name` [20]
- `student_last_name` [21]
- `student_email` [22]
- `student_group` [23]
- `student_identifier` [24]
- `student_account_id` [25]
- `student_user_id` [26]
- `student_left_feedback` [27]
- `student_feedback` [28]

### Below are examples of student_feedback with and without written feedback for UVA CS 1110:

#### Without Written Feedback:

```json
[
   {
      "answer": {
         "otherValue": "",
         "selections": [
            0
         ]
      },
      "isValid": true,
      "question": {
         "type": "select-all",
         "prompt": "How did the session go?",
         "options": [
            "good",
            "not great, the TA could have been better",
            "not great, I'm really behind",
            "other",
            "I'm leaving comments below"
         ],
         "isRequired": false,
         "hasAutocomplete": false,
         "allowCustomResponse": false
      }
   }
]
```

#### With Written Feedback:

```json
[
   {
      "answer": {
         "otherValue": "",
         "selections": [
            0
         ]
      },
      "isValid": true,
      "question": {
         "type": "select-all",
         "prompt": "How did the session go?",
         "options": [
            "good",
            "not great, the TA could have been better",
            "not great, I'm really behind",
            "other",
            "I'm leaving comments below"
         ],
         "isRequired": false,
         "hasAutocomplete": false,
         "allowCustomResponse": false
      }
   },
   {
      "answer": "THIS IS WHERE THE FEEDBACK WOULD BE ",
      "isValid": true,
      "question": {
         "type": "free-response",
         "prompt": "Additional comments:",
         "options": [
            ""
         ],
         "isRequired": false,
         "hasAutocomplete": false,
         "allowCustomResponse": false
      }
   }
]
```

### Below is an example of student_prompts for UVA CS 1110:

```json
[
   {
      "answer": "Q1",
      "isValid": false,
      "question": {
         "type": "short-answer",
         "prompt": "Where are you sitting (tables have letters, chairs have numbers)?",
         "options": [
            ""
         ],
         "isRequired": false,
         "hasAutocomplete": false,
         "allowCustomResponse": false
      }
   },
   {
      "answer": "PA09",
      "isValid": true,
      "question": {
         "type": "short-answer",
         "prompt": "What are you working on?",
         "options": [],
         "isRequired": false,
         "hasAutocomplete": false,
         "allowCustomResponse": false
      }
   },
   {
      "answer": "Yes",
      "isValid": true,
      "question": {
         "type": "free-response",
         "prompt": "What have you tried to solve the problem?",
         "options": [],
         "isRequired": false,
         "hasAutocomplete": false,
         "allowCustomResponse": false
      }
   }
]
```

### Below are examples of teacher_feedback with and without written feedback for UVA CS 1110:

#### Without Written Feedback

```json
[
   {
      "answer": {
         "otherValue": "",
         "selections": [
            0
         ]
      },
      "isValid": true,
      "question": {
         "type": "select-all",
         "prompt": "How did the session go?",
         "options": [
            "good",
            "the student was difficult to work with",
            "TA struggled with the material",
            "an instructor should contact the student, comments below",
            "other"
         ],
         "isRequired": false,
         "hasAutocomplete": false,
         "allowCustomResponse": false
      }
   }
]
```

#### With Written Feedback

```json
[
   {
      "answer": {
         "otherValue": "",
         "selections": [
            4
         ]
      },
      "isValid": true,
      "question": {
         "type": "select-all",
         "prompt": "How did the session go?",
         "options": [
            "good",
            "the student was difficult to work with",
            "TA struggled with the material",
            "an instructor should contact the student, comments below",
            "other"
         ],
         "isRequired": false,
         "hasAutocomplete": false,
         "allowCustomResponse": false
      }
   },
   {
      "answer": "Seems like this student wasn't taken off the waiting list from yesterday",
      "isValid": true,
      "question": {
         "type": "free-response",
         "prompt": "Additional comments:",
         "options": [
            ""
         ],
         "isRequired": false,
         "hasAutocomplete": false,
         "allowCustomResponse": false
      }
   }
]
```
