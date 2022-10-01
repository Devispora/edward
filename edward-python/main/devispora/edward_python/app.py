import json

from devispora.edward_python.constants.constants import Constants
from devispora.edward_python.exceptions.account_sheet_exceptions import AccountSheetException, \
    AccountSheetExceptionMessage
from devispora.edward_python.models.account_sheet import AccountSheetStatus
from devispora.edward_python.models.erred_sheet import ErredSheet
from devispora.edward_python.models.helpers.contact_sheet_helper import find_reps_on_sheet, fetch_emails_only, \
    fetch_discord_ids
from devispora.edward_python.service.discord_interaction_service import share_sheet_to_discord, \
    share_error_sheet_to_discord
from devispora.edward_python.service.drive_interaction_service import retrieve_items_from_folder, share_sheet_to_users
from devispora.edward_python.service.helpers.google_item_helper import filter_to_just_files, \
    filter_by_name_and_cooldown, filter_by_share_and_cleaning
from devispora.edward_python.service.rep_interaction_service import retrieve_contacts
from devispora.edward_python.service.sheets_interaction_service import retrieve_sheet_information, update_shared_status


just_this_folder = Constants.ovo_drive_folder
contact_sheet = Constants.ovo_drive_rep_sheet


def lambda_handler(event, context):
    # non aws-devs: event/context are mandatory even if not used
    drive_items = retrieve_items_from_folder(just_this_folder)
    filtered_files = filter_to_just_files(drive_items)

    filtered_sheets = filter_by_name_and_cooldown(filtered_files)

    converted_sheets, erred_sheets = retrieve_sheet_information(filtered_sheets)
    sheets_to_share, sheets_to_clean = filter_by_share_and_cleaning(converted_sheets)

    contact_reps = retrieve_contacts(contact_sheet)
    for sheet in sheets_to_share:
        approved_contacts = find_reps_on_sheet(contact_reps, sheet)
        to_share_emails = fetch_emails_only(approved_contacts)
        share_sheet_to_users(sheet.sheet_id, to_share_emails)
        default_range = 'B4'
        if len(to_share_emails) > 0:
            update_shared_status(sheet.sheet_id, default_range, AccountSheetStatus.StatusShared)
            retrieved_discord_ids = fetch_discord_ids(approved_contacts)
            share_sheet_to_discord(sheet, retrieved_discord_ids)
            if len(sheet.emails) != len(to_share_emails):
                erred_sheets.append(
                    ErredSheet(
                        sheet.sheet_id, sheet.sheet_name,
                        AccountSheetException(AccountSheetExceptionMessage.EmailNotFoundInRepSheet)
                    )
                )
        else:
            erred_sheets.append(
                ErredSheet(
                    sheet.sheet_id, sheet.sheet_name,
                    AccountSheetException(AccountSheetExceptionMessage.EmailNeverMatched)
                )
            )
    for sheet in erred_sheets:
        share_error_sheet_to_discord(sheet)
    # todo
    #  Clean/error mechanism ->
    #   - bundle up cleaned sheets + link/name
    #  Bonus ->
    #   - Show friendlier name instead of service account gibberish.
    #   - validate email again with some room of split-character-improvement?

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
