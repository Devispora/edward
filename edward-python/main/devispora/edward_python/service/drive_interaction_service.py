from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from devispora.edward_python.exceptions.drive_exceptions import DriveException, DriveExceptionMessage
from devispora.edward_python.exceptions.sheet_share_exception import SheetShareException, SheetShareExceptionMessage
from devispora.edward_python.google.credentials import get_credentials
from devispora.edward_python.service.helpers.google_item_helper import create_email_permission

credentials = get_credentials()
drive_service = build('drive', 'v3', credentials=credentials)


def retrieve_items_from_folder(folder_id: str):
    file_operation = drive_service.files()
    items = []
    request = file_operation.list(
        q=f'"{folder_id}" in parents',
        pageSize=10,
        fields="nextPageToken, files(id, name, mimeType, createdTime)")
    try:
        while request is not None:
            results = request.execute()
            drive_files = results.get('files', [])
            request = file_operation.list_next(request, results)
            items.extend(drive_files)
        if not items:
            raise DriveException(DriveExceptionMessage.NoFilesFound)
        return items
    except HttpError as error:
        print(f'An error occurred: {error}')
        raise DriveException(DriveExceptionMessage.HTTPError)


# todo catch them exceptions
def share_sheet_to_users(spreadsheet_id: str, emails: [str]):
    prepared_batch = drive_service.new_batch_http_request(callback=callback)
    for email in emails:
        permission = drive_service.permissions().create(
            fileId=spreadsheet_id,
            body=create_email_permission(email),
            fields='id'
        )
        prepared_batch.add(permission)
    return prepared_batch.execute()


def callback(request_id, response, exception):
    if exception:
        print(exception)
        raise SheetShareException(SheetShareExceptionMessage.ShareIssue)
