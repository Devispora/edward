from google.oauth2 import service_account
import os

current_directory = os.getcwd()
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SERVICE_ACCOUNT_FILE = f'{current_directory}/resources/ovo-gdrive-277815-1df7fd0a4f85.json'


def get_credentials():
    return service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
