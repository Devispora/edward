import json

from devispora.edward_python.service.drive_interaction_service import retrieve_items_from_folder
from devispora.edward_python.service.helpers.google_item_helper import filter_to_just_files, \
    filter_by_name_and_cooldown, filter_by_share_and_cleaning
from devispora.edward_python.service.sheets_interaction_service import retrieve_sheet_information

just_this_folder = '1RV9MSTKvS2IlGbYFVWFBMtoiUErxxsIl'


def lambda_handler(event, context):
    # non aws-devs: event/context are mandatory even if not used
    drive_items = retrieve_items_from_folder(just_this_folder)
    filtered_files = filter_to_just_files(drive_items)
    filtered_sheets = filter_by_name_and_cooldown(filtered_files)

    converted_sheets, erred_sheets = retrieve_sheet_information(filtered_sheets)

    sheets_to_share, sheets_to_clean = filter_by_share_and_cleaning(converted_sheets)

    # todo
    #   [done] Split all the sheets that need to be shared
    #   [done] Split all the sheets that can be cleaned after 2 days
    #  Share mechanism ->
    #   - Read out contact sheet info [one super sheet now]
    #   - share sheet to emails
    #   - change status to shared
    #   - inform users on discord with link/name
    #  Clean/error mechanism ->
    #   - bundle up erred sheets + link/name + error-info
    #   - bundle up cleaned sheets + link/name
    #  Bonus ->
    #   - validate email again with some room of split-character-improvement?

    # sheets_to_share = filter_sheets_that_need_shared()
    # todo filter sheets from here

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
