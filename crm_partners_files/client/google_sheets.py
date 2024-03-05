from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
# SAMPLE_SPREADSHEET_ID = "1-hjm3XzyhKh4104N-68-ICamGIuRNm0UUBhVX7NK8UU"

SAMPLE_RANGE_NAME = "Class Data!A2:E"


def send_data_to_googlesheets(spreadsheet_id, values):
    """

    """

    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=spreadsheet_id, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

    except HttpError as err:
        print(err)
