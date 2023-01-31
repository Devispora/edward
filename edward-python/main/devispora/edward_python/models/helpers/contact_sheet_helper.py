from typing import List

from devispora.edward_python.exceptions.rep_sheet_exceptions import RepSheetException, RepSheetExceptionMessage
from devispora.edward_python.models.account_sheet import AccountSheetResult
from devispora.edward_python.models.contact_sheet import Contact, RepType


expected_contact_columns = 9


def process_rep_sheet(contact_sheet_items: List[List[str]]) -> [Contact]:
    # Converts contact sheet into Contacts. Starting from list position 1 as 0 is titles
    resulting_reps: [Contact] = []
    rep_sheet_line = 1
    for contact in contact_sheet_items[1:]:
        rep_sheet_line = rep_sheet_line + 1
        try:
            if len(contact) >= expected_contact_columns:
                resulting_reps.append(Contact(
                    groups=retrieve_basic_information(contact[0], 'groups'),
                    char_name=retrieve_basic_information(contact[1], 'char_name'),
                    email=retrieve_basic_information(contact[2], 'email'),
                    discord_handle=retrieve_basic_information(contact[3], 'discord_handle'),
                    discord_id=retrieve_discord_id(contact),
                    rep_type=retrieve_rep_type(contact),
                    account_limit=retrieve_account_limit(contact)
                ))
        except RepSheetException as rse:
            additional_message = f'{rse.additional_message if rse.additional_message else ""} at rep #{rep_sheet_line}'
            raise RepSheetException(rse.message, additional_message)
    return resulting_reps


def retrieve_basic_information(info: str, subject: str):
    if len(info) < 1:
        raise RepSheetException(RepSheetExceptionMessage.MissingValueOnSheet, subject)
    else:
        return info


def retrieve_discord_id(contact: List[str]):
    try:
        return int(contact[4])
    except ValueError:
        raise RepSheetException(RepSheetExceptionMessage.DiscordIdNotInt)


def retrieve_rep_type(contact: List[str]) -> RepType:
    rep_type = contact[5]
    try:
        return RepType(rep_type)
    except KeyError:
        raise RepSheetException(RepSheetExceptionMessage.RepTypeNotRecognised, f'provided unknown rep type: {rep_type}')


# todo think about merging this if we're not expanding it later
def retrieve_account_limit(contact: List[str]):
    try:
        return int(contact[6])
    except ValueError:
        raise RepSheetException(RepSheetExceptionMessage.AccountLimitNotInt)


# todo consider how we can allow
def find_reps_on_sheet(contacts: [Contact], sheet: AccountSheetResult) -> [Contact]:
    retrieved_reps = []
    for sheet_email in sheet.emails:
        for contact in contacts:
            if contact.email == sheet_email:
                retrieved_reps.append(contact)
    return retrieved_reps


def fetch_emails_only(contacts: [Contact]):
    return [contact.email for contact in contacts]


def fetch_discord_ids(contacts: [Contact]):
    return [contact.discord_id for contact in contacts]
