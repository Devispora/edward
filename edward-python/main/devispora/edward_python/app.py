import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from devispora.edward_python.google.credentials import get_credentials


def lambda_handler(event, context):
    # non aws-devs: event/context are mandatory even if not used
    credentials = get_credentials()
    try:
        service = build('drive', 'v3', credentials=credentials)
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }


