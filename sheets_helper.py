import os.path
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def generate_instructor_feedback_sheet(info):
    """
    This function takes in the result of get_ta_feedback() with anonymous set to true and generates a Google
    sheet containing all the information. Each TA will have their own page containing their comments.
    """
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
        token.write(creds.to_json())

    try:
        # Build the service
        service = build('sheets', 'v4', credentials=creds)

        # Create a new spreadsheet with today's date in the title
        today_date = datetime.today().strftime('%Y-%m-%d')
        spreadsheet = {
            'properties': {
                'title': f'TA Feedback {today_date}'
            }
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet, fields='spreadsheetId').execute()
        spreadsheet_id = spreadsheet.get('spreadsheetId')

        # Prepare requests to add sheets
        requests = []
        sheet_id_map = {}
        first_ta = True
        for ta_name in info.keys():
            if first_ta:
                # Rename the default sheet to the first TA's name
                requests.append({
                    'updateSheetProperties': {
                        'properties': {
                            'sheetId': 0,
                            'title': ta_name
                        },
                        'fields': 'title'
                    }
                })
                sheet_id_map[ta_name] = 0
                first_ta = False
            else:
                # Add a new sheet for each subsequent TA
                requests.append({
                    'addSheet': {
                        'properties': {
                            'title': ta_name
                        }
                    }
                })

        # Execute the batch update to create sheets and rename the first sheet
        body = {
            'requests': requests
        }
        response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()

        # Retrieve the sheet IDs for the newly created sheets
        for reply in response.get('replies', []):
            if 'addSheet' in reply:
                sheet_properties = reply['addSheet']['properties']
                sheet_id_map[sheet_properties['title']] = sheet_properties['sheetId']

        # Prepare requests to add data to the sheets
        requests = []
        for ta_name, comments in info.items():
            sheet_id = sheet_id_map[ta_name]
            values = [[comment] for comment in comments]
            requests.append({
                'updateCells': {
                    'rows': [{'values': [{'userEnteredValue': {'stringValue': comment}}]} for comment in comments],
                    'fields': 'userEnteredValue',
                    'start': {'sheetId': sheet_id, 'rowIndex': 0, 'columnIndex': 0}
                }
            })

        # Execute the batch update to add data
        body = {
            'requests': requests
        }
        service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()

        # Print the link to the spreadsheet
        spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit"
        print(f"Spreadsheet URL: {spreadsheet_url}")

    except HttpError as err:
        print(err)
