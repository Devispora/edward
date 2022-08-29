from typing import List

from devispora.edward_python.models.helpers.contact_sheet_helper import process_rep_sheet
from devispora.edward_python.service.sheets_interaction_service import retrieve_sheet_values_by_range

desired_contact_sheet_range = 'A:I'
contact_sheet_tab = 'Contact Reps'


# todo move this call away from here. Or Maybe not.
def retrieve_contacts(contact_sheet_id: str):
    contact_sheet_items: List[List[str]] = retrieve_sheet_values_by_range(contact_sheet_id, desired_contact_sheet_range)
    return process_rep_sheet(contact_sheet_items)
