import json

from devispora.edward_python.service.drive_interaction_service import retrieve_items_from_folder
from devispora.edward_python.service.helpers.google_item_helper import filter_to_just_files, filter_sheets_by_name_being_ready
from devispora.edward_python.service.sheets_interaction_service import retrieve_sheet_information

just_this_folder = '1RV9MSTKvS2IlGbYFVWFBMtoiUErxxsIl'


def lambda_handler(event, context):
    # non aws-devs: event/context are mandatory even if not used

    # Todo. First bit would be to grab all the details from the sheet and to convert the date.
    #   Secondarily, read out all values from the Contact Sheet.
    #   Which has multiple tabs. Hopefully we can finally fix ObsCams/Second type rep nonsense.
    #   Afterwards, I guess step by step reintroduce the basic flow which is:
    #       1: Read sheet details, if event is less than 4 hours -> share
    drive_items = retrieve_items_from_folder(just_this_folder)
    filtered_files = filter_to_just_files(drive_items)
    filtered_sheets = filter_sheets_by_name_being_ready(filtered_files)
    converted_sheets = retrieve_sheet_information(filtered_sheets)
    # todo filter sheets from here

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
