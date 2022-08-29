from typing import List

from devispora.edward_python.exceptions.rep_sheet_exceptions import RepSheetException, RepSheetExceptionMessage
from devispora.edward_python.models.contact_sheet import Contact, RepType


def process_rep_sheet(contact_sheet_items: List[List[str]]) -> [Contact]:
    # Converts contact sheet into Contacts. Starting from list position 1 as 0 is titles
    resulting_reps: [Contact] = []
    for contact in contact_sheet_items[1:]:
        if len(contact) >= 9:
            resulting_reps.append(Contact(
                groups=contact[0],
                char_name=contact[1],
                email=contact[2],
                discord_handle=contact[3],
                discord_id=retrieve_discord_id(contact),
                rep_type=retrieve_rep_type(contact),
                account_limit=retrieve_account_limit(contact)
            ))
    return resulting_reps


def retrieve_discord_id(contact: List[str]):
    try:
        return int(contact[4])
    except ValueError:
        raise RepSheetException(RepSheetExceptionMessage.DiscordIdNotInt)


# todo check if there's a better way to iterate through a python enum
def retrieve_rep_type(contact: List[str]) -> RepType:
    rep_type = contact[5]
    if rep_type == RepType.OutfitRep:
        return RepType.OutfitRep
    elif rep_type == RepType.CommunityRep:
        return RepType.CommunityRep
    elif rep_type == RepType.ObserverUser:
        return RepType.ObserverUser
    elif rep_type == RepType.ScrimTeam:
        return RepType.ScrimTeam
    else:
        raise RepSheetException(RepSheetExceptionMessage.RepTypeNotRecognised)


# todo think about merging this if we're not expanding it later
def retrieve_account_limit(contact: List[str]):
    try:
        return int(contact[6])
    except ValueError:
        raise RepSheetException(RepSheetExceptionMessage.AccountLimitNotInt)


# todo consider how we can allow
def find_reps_on_sheet(contacts: [Contact], sheet_emails: [str]) -> [Contact]:
    retrieved_reps = []
    for sheet_email in sheet_emails:
        for contact in contacts:
            if contact.email == sheet_email:
                retrieved_reps.append(contact)
    return retrieved_reps

