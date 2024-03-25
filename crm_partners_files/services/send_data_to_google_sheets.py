__all__ = ['send_data_to_googlesheets', ]

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from os import environ, getenv

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = environ.get('GOOGLE_SPREADSHEETS_TABLE_ID')

raw_client_private_key = getenv('PRIVATE_KEY')
client_private_key = raw_client_private_key.replace(r'\n', '\n')

credentials_dict = {
    'type': 'service_account',
    "project_id": environ.get('PROJECT_ID'),
    "private_key_id": environ.get('PRIVATE_KEY_ID'),
    "private_key": client_private_key,
    "client_email": environ.get('CLIENT_EMAIL'),
    "client_id": environ.get('CLIENT_ID'),
    "auth_uri": environ.get('AUTH_URI'),
    "token_uri": environ.get('TOKEN_URI'),
    "auth_provider_x509_cert_url": environ.get('AUTH_PROVIDER'),
    "client_x509_cert_url": environ.get('CLIENT'),
    "universe_domain": environ.get('UNIVERSE_DOMAIN')
}


def send_data_to_googlesheets(table_name: str, sending_data: []):
    """
    Add data to existing table
    """
    print(table_name, sending_data, '>>>>>>>>>>>>>>>>>>>>>>>>>>12')
    creds = None
    creds = service_account.Credentials.from_service_account_info(
        credentials_dict, )

    body = {
        "values": [
            sending_data,
        ]
    }
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()

        result = (
            sheet.values()
            .append(spreadsheetId=SPREADSHEET_ID, range=f"{table_name}!1:1",
                    valueInputOption="USER_ENTERED",
                    insertDataOption="INSERT_ROWS", body=body)
            .execute()
        )
        return result
    except HttpError:
        return None
