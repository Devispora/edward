from google.oauth2 import service_account
import os

current_directory = os.getcwd()
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = f'{current_directory}/resources/ovo-gdrive-277815-1df7fd0a4f85.json'


# todo consider in the future to reduce the scope once files are created by the service account
# https://developers.google.com/identity/protocols/oauth2/scopes#drive
def get_credentials():
    return service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
