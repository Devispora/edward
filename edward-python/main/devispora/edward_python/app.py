import json

from devispora.edward_python.models.account_sheet import AccountSheetStatus
from devispora.edward_python.models.helpers.contact_sheet_helper import find_reps_on_sheet, fetch_emails_only, \
    fetch_discord_ids
from devispora.edward_python.service.discord_interaction_service import share_to_discord
from devispora.edward_python.service.drive_interaction_service import retrieve_items_from_folder, share_sheet_to_users
from devispora.edward_python.service.helpers.google_item_helper import filter_to_just_files, \
    filter_by_name_and_cooldown, filter_by_share_and_cleaning
from devispora.edward_python.service.rep_interaction_service import retrieve_contacts
from devispora.edward_python.service.sheets_interaction_service import retrieve_sheet_information, update_shared_status

just_this_folder = '1RV9MSTKvS2IlGbYFVWFBMtoiUErxxsIl'
contact_sheet_test = '1eY0kR6QOYpC7Al9zthMm4I2E4BybwD2crupdgLlerSs'


def lambda_handler(event, context):
    # non aws-devs: event/context are mandatory even if not used
    drive_items = retrieve_items_from_folder(just_this_folder)
    filtered_files = filter_to_just_files(drive_items)

    filtered_sheets = filter_by_name_and_cooldown(filtered_files)

    converted_sheets, erred_sheets = retrieve_sheet_information(filtered_sheets)
    sheets_to_share, sheets_to_clean = filter_by_share_and_cleaning(converted_sheets)

    contact_reps = retrieve_contacts(contact_sheet_test)
    for sheet in sheets_to_share:
        # todo nope lol this needs to be verified first
        #  verify sheet emails. Only send to ones that properly exist
        #  - [done] grab emails from contacts to verify
        #  - [done] share to sheet, easy
        #  - share to discord [all users at once for that sheet]
        approved_contacts = find_reps_on_sheet(contact_reps, sheet)
        to_share_emails = fetch_emails_only(approved_contacts)
        #share_sheet_to_users(sheet.sheet_id, to_share_emails)
        #todo grab all user ids we want
        default_range = 'B4'
        update_shared_status(sheet.sheet_id, default_range, AccountSheetStatus.StatusShared)
        share_to_discord(sheet, fetch_discord_ids(approved_contacts))

    # todo
    #   [done] Split all the sheets that need to be shared
    #   [done] Split all the sheets that can be cleaned after 2 days
    #  Share mechanism ->
    #   - [done] Read out contact sheet info [one super sheet now]
    #   - [done] fetch contact(s) from sheet and match with contact
    #   - [done] share sheet to emails
    #   - [done] change status to shared
    #   - [done] inform users on discord with link/name
    #   - Error info flow for staff
    #  Clean/error mechanism ->
    #   - bundle up erred sheets + link/name + error-info
    #   - bundle up cleaned sheets + link/name
    #  Bonus ->
    #   - Show friendlier name instead of service account gibberish.
    #   - validate email again with some room of split-character-improvement?


    # sheets_to_share = filter_sheets_that_need_shared()
    # todo filter sheets from here
    print('tek')

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
